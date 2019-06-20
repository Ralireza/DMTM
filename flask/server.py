from flask import Flask
from flask import request
from flask import jsonify
import coefficient as coef
import descriptive_feature as df
import pandas
import json
import math

app = Flask(__name__)


# request
# {
#     "data_file": "<Downloadable File Address>",
#     "parameters": {
#         "param1": "value1",
#         "param2": "value2"
#     }
# }
# response
# {
#     "result_file": "Downlodable File Address>",
#     "results": ["1", "2", "3"]
# }


@app.route("/api/v1/coefficient/pearson", methods=['GET', 'POST'])
def pearson():
    if request.method == 'POST':
        req_data = request.get_json()
        data_url = req_data['data_file']
        csv = pandas.read_csv(data_url)
        headers = csv.columns.values
        num_list1 = list(csv[headers[0]])
        num_list2 = list(csv[headers[0]])

        # delete outlyer by impute zero
        for i in range(len(num_list1)):
            if math.isinf(num_list1[i]):
                num_list1[i] = 0
        for i in range(len(num_list2)):
            if math.isinf(num_list2[i]):
                num_list2[i] = 0
        try:

            correlation, p_value = coef.pearson_correlation(num_list1, num_list2)
            result = {"correlation": correlation, "p_value": p_value}
        except KeyError and ValueError:
            result = "ERROR"
            pass

        with open('data_pearson.json', 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': './data.json',
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/desfeature/tmean", methods=['GET', 'POST'])
def mean():
    if request.method == 'POST':
        req_data = request.get_json()
        data_url = req_data['data_file']
        csv = pandas.read_csv('./files/sample.csv')
        num_list1 = csv['Q1']
        params = None
        try:
            # Here are the optional json parameters inside a try
            params = req_data['parameters']
            mean1 = df.trimmed_mean(num_list1, params['limit'])
            result = {"tmean": mean1}
        except KeyError or ValueError:
            result = {"error": "bad param or no param"}
            pass
        if params is None:

            data = {
                'result_file': data_url,
                'results': "need a parameter"
            }
        else:
            with open('data_mean.json', 'w') as outfile:
                json.dump(result, outfile)
            data = {
                'result_file': data_url,
                'results': result
            }
        resp = jsonify(data)
        return resp
