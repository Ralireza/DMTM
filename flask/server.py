from flask import Flask
from flask import request
from flask import jsonify
import descriptive_feature as df

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


@app.route("/api/v1/var", methods=['GET', 'POST'])
def covar():
    if request.method == 'POST':
        req_data = request.get_json()
        numberlist = [1, 1, 1, 11, 1, 1, 3, 3, 33, 3, 33, 33, 4, 4, 4, 4, 4, 4, 4]
        data_url = req_data['data_file']

        params = None
        try:
            # Here are the optional json parameters inside a try
            params = req_data['parameters']
            result = df.trimmed_mean(numberlist, params["limit"])
        except KeyError and ValueError:
            result = "ERROR"
            pass
        if params is None:

            data = {
                'result_file': data_url,
                'results': "need a parameter"
            }
        else:
            data = {
                'result_file': data_url,
                'results': result
            }
        resp = jsonify(data)
        return resp





