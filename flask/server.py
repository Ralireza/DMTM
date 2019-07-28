from flask import Flask, abort, request, jsonify
import pandas
import json
import math
import time
import os
from scipy import stats as ss
import frequency as freq
import descriptive_feature as df

current_path = os.path.dirname(os.path.abspath(__file__))


def pearson_correlation(list_number1, list_number2):
    return ss.pearsonr(list_number1, list_number2)


def trimmed_mean(number_list, limitation):
    # limitation is float number like 0.3 and delete 0.3 of outlier data
    return ss.trim_mean(number_list, limitation)


def bad_request():
    abort(400)


app = Flask(__name__)


# <editor-fold desc="frequency">
@app.route("/api/v1/frequency", methods=['POST'])
def frequency():
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
                string_value = str(num_list1[i])
                if string_value.isdigit():
                    if math.isinf(float(num_list1[i])):
                        num_list1[i] = 0
            for i in range(len(num_list2)):
                string_value = str(num_list1[i])
                if string_value.isdigit():
                    if math.isinf(float(num_list2[i])):
                        num_list2[i] = 0
            result = []
            # my_list = [1, 1, 2, 2, 3, 3, 4, 4, 2, 2, 8, 8, 8, 8, 9]
            # my_list2 = [1, 2, 8]

            for index, question in enumerate(num_list2):
                dict = {"id": (index),
                        "relative": freq.relative_frequency(num_list1, question, True),
                        "absolute": freq.absolute_frequency(num_list1, question)}
                result.append(dict)

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
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


# </editor-fold>


# <editor-fold desc="descriptive_feature">

@app.route("/api/v1/desfeature/min", methods=['POST'])
def min():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])

            # delete outlier by impute zero
            for i in range(len(num_list1)):
                if math.isinf(float(num_list1[i])):
                    num_list1[i] = 0

            result = {"min": df.min_num(num_list1)}

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
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


@app.route("/api/v1/desfeature/max", methods=['POST'])
def max():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])

            # delete outlier by impute zero
            for i in range(len(num_list1)):
                if math.isinf(float(num_list1[i])):
                    num_list1[i] = 0

            result = {"max": df.max_num(num_list1)}

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
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


@app.route("/api/v1/desfeature/domainrange", methods=['POST'])
def range_domain():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])

            # delete outlier by impute zero
            for i in range(len(num_list1)):
                if math.isinf(float(num_list1[i])):
                    num_list1[i] = 0

            result = {"domainrange": df.range_domain(num_list1)}

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
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


@app.route("/api/v1/desfeature/mean", methods=['POST'])
def mean():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])

            # delete outlier by impute zero
            for i in range(len(num_list1)):
                if math.isinf(float(num_list1[i])):
                    num_list1[i] = 0

            result = {"mean": df.mean(num_list1)}

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
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


@app.route("/api/v1/desfeature/tmean", methods=['GET', 'POST'])
def tmean():
    if request.method == 'POST':
        req_data = request.get_json()
        data_url = req_data['data_file']
        csv = pandas.read_csv(data_url)
        headers = csv.columns.values
        num_list1 = csv[headers[0]]
        params = None
        try:
            params = req_data['parameters']
            mean1 = trimmed_mean(num_list1, params['limit'])
            result = {"tmean": mean1}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        if params is None:

            # data = {
            #     'result_file': data_url,
            #     'results': "need a parameter"
            # }
            bad_request()
        else:

            response_dir = current_path + '/dmtm_responses'
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


@app.route("/api/v1/desfeature/mode", methods=['POST'])
def mode():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])

            # delete outlier by impute zero
            for i in range(len(num_list1)):
                if math.isinf(float(num_list1[i])):
                    num_list1[i] = 0

            result = {"mode": df.mode(num_list1)}

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
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


@app.route("/api/v1/desfeature/median", methods=['POST'])
def median():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])

            # delete outlier by impute zero
            for i in range(len(num_list1)):
                if math.isinf(float(num_list1[i])):
                    num_list1[i] = 0

            result = {"median": df.median(num_list1)}

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
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


@app.route("/api/v1/desfeature/variance", methods=['POST'])
def variance():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])

            # delete outlier by impute zero
            for i in range(len(num_list1)):
                if math.isinf(float(num_list1[i])):
                    num_list1[i] = 0

            result = {"variance": df.variance(num_list1)}

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
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


@app.route("/api/v1/desfeature/deviation", methods=['POST'])
def deviation():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])

            # delete outlier by impute zero
            for i in range(len(num_list1)):
                if math.isinf(float(num_list1[i])):
                    num_list1[i] = 0

            result = {"deviation": df.deviation(num_list1)}

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
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


@app.route("/api/v1/desfeature/quantile", methods=['POST'])
def quantile():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            params = req_data['parameters']
            q=params["q"]
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])

            # delete outlier by impute zero
            for i in range(len(num_list1)):
                if math.isinf(float(num_list1[i])):
                    num_list1[i] = 0

            result = {"quantile": df.quantile(num_list1,q)}

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
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


# </editor-fold>

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


if __name__ == '__main__':
    app.run()
