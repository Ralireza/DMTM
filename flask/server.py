from flask import Flask, abort, request, jsonify
import pandas
import json
import math
import time
import os
from scipy import stats as ss

current_path = os.path.dirname(os.path.abspath(__file__))


def pearson_correlation(list_number1, list_number2):
    return ss.pearsonr(list_number1, list_number2)


def trimmed_mean(number_list, limitation):
    # limitation is float number like 0.3 and delete 0.3 of outlier data
    return ss.trim_mean(number_list, limitation)


def bad_request():
    abort(400)


app = Flask(__name__)


@app.route("/api/v1/coefficient/pearson", methods=['GET', 'POST'])
def pearson():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            # delete outlier by impute zero
            for i in range(len(num_list1)):
                if math.isinf(num_list1[i]):
                    num_list1[i] = 0
            for i in range(len(num_list2)):
                if math.isinf(num_list2[i]):
                    num_list2[i] = 0

            correlation, p_value = pearson_correlation(num_list1, num_list2)
            result = {"correlation": correlation, "p_value": p_value}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = 'dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': res_path,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/desfeature/tmean", methods=['GET', 'POST'])
def mean():
    if request.method == 'POST':
        req_data = request.get_json()
        data_url = req_data['data_file']
        csv = pandas.read_csv(data_url)
        print(current_path)
        headers = csv.columns.values
        num_list1 = csv[headers[0]]
        params = None
        try:
            params = req_data['parameters']
            mean1 = trimmed_mean(num_list1, params['limit'])
            result = {"tmean": mean1}
        except Exception :
            # result = {"error": "bad param or no param"}
            bad_request()
        if params is None:

            # data = {
            #     'result_file': data_url,
            #     'results': "need a parameter"
            # }
            bad_request()
        else:

            response_dir = current_path+'/dmtm_responses'
            if not os.path.exists(response_dir):
                os.makedirs(response_dir)
            current_milli_time = lambda: int(round(time.time() * 1000))
            res_path = response_dir + '/' + str(current_milli_time()) + '.json'
            with open(res_path, 'w') as outfile:
                json.dump(result, outfile)
            data = {
                'result_file': res_path,
                'results': result
            }
        resp = jsonify(data)
        return resp


if __name__ == '__main__':
    app.run()
