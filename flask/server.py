from flask import Flask, abort, request, jsonify, send_from_directory, current_app
import pandas
import json
import math
import time
import os
import frequency as freq
import descriptive_feature as df
import coefficient as co
import statistical_test as stt
import clustering as cls
import imputation as imp
import outlier
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
ip = "127.0.0.1"
dmtm_url = "http://" + ip + ":5000"


def bad_request():
    abort(400)


app = Flask(__name__)
app.config["dmtm_responses"] = "./dmtm_responses"


@app.route('/dmtm_responses/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    path = os.path.join(current_app.root_path, app.config['dmtm_responses'])
    return send_from_directory(directory=path, filename=filename)


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

            result = []
            # my_list = [1, 1, 2, 2, 3, 3, 4, 4, 2, 2, 8, 8, 8, 8, 9]
            # my_list2 = [1, 2, 8]
            num_list2 = list(set(num_list2))  # delete same value
            for index, question in enumerate(num_list2):
                dict = {"id": (index),
                        "relative": freq.relative_frequency(num_list1, question, True),
                        "absolute": freq.absolute_frequency(num_list1, question)}
                result.append(dict)

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'

        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
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
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            min_result = []
            result = []
            for column in num_list1:
                min_result.append(df.min_num(column))
            for j in range(len(num_list1)):
                result.append({j: min_result[j]})


        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
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
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.max_num(column))
            for j in range(len(num_list1)):
                result.append({j: res[j]})
        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
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
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.range_domain(column))
            for j in range(len(num_list1)):
                result.append({j: res[j]})

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
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
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.mean(column))
            for j in range(len(num_list1)):
                result.append({j: res[j]})
        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
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
        params = None
        try:
            params = req_data['parameters']
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.trimmed_mean(column, params['limit']))
            for j in range(len(num_list1)):
                result.append({j: res[j]})

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
            response_url = dmtm_url + '/dmtm_responses'
            if not os.path.exists(response_dir):
                os.makedirs(response_dir)
            current_milli_time = lambda: int(round(time.time() * 1000))
            res_path = response_dir + '/' + str(current_milli_time()) + '.json'
            response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
            with open(res_path, 'w') as outfile:
                json.dump(result, outfile)
            data = {
                'result_file': response_complete_url,
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
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.mode(column))
            for j in range(len(num_list1)):
                result.append({j: res[j]})

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
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
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.median(column))
            for j in range(len(num_list1)):
                result.append({j: res[j]})

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/desfeature/wmedian", methods=['POST'])
def wmedian():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            result = {"wmedian": df.wighted_median(num_list1, num_list2)}

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
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
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.variance(column))
            for j in range(len(num_list1)):
                result.append({j: res[j]})

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
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
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.deviation(column))
            for j in range(len(num_list1)):
                result.append({j: res[j]})

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
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
            q = params["q"]
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.quantile(column, q))
            for j in range(len(num_list1)):
                result.append({j: res[j]})


        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/desfeature/skewness", methods=['POST'])
def population_skewness():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.population_skewness(column))
            for j in range(len(num_list1)):
                result.append({j: res[j]})

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/desfeature/kurtosis", methods=['POST'])
def kurtosis():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                res.append(df.kurtosis(column))
            for j in range(len(num_list1)):
                result.append({j: res[j]})

        except Exception:
            bad_request()
        response_dir = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = response_dir + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


# </editor-fold>

# <editor-fold desc="coefficients">

@app.route("/api/v1/coefficient/pearson", methods=['POST'])
def pearson():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            correlation, p_value = co.pearson_correlation(num_list1, num_list2)
            result = {"correlation": correlation, "p_value": p_value}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/spearman", methods=['POST'])
def spearman_correlation():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            correlation, p_value = co.spearman_correlation(num_list1, num_list2)
            result = {"correlation": correlation, "p_value": p_value}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/kendall", methods=['POST'])
def kendalltau_correlation():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            correlation, p_value = co.kendalltau_correlation(num_list1, num_list2)
            result = {"correlation": correlation, "p_value": p_value}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/cramers", methods=['POST'])
def cramers_v():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            correlation = co.cramers_v(num_list1, num_list2)
            result = {"correlation": correlation}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/tavafogh", methods=['POST'])
def tavafoghi():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            correlation = co.tavafoghi(num_list1, num_list2)
            result = {"correlation": correlation}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/somersd", methods=['POST'])
def somersd():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            correlation = co.somersd(num_list1, num_list2)
            result = {"correlation": correlation}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/etaomg", methods=['POST'])
def anova_eta_omg():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            eta, omg = co.anova_eta_omg(num_list1, num_list2)
            result = {"eta": eta, "omg": omg}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/sem", methods=['POST'])
def structural_equation_modeling():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            model = req_data['model']
            model = "\n".join(model)

            csv = pandas.read_csv(data_url)

            beta, lam, psi, theta, sigma, cov = co.structural_equation_modeling(csv, model)
            result = {"beta": beta, "lambda": lam, "psi": psi, "theta": theta, "sigma": sigma, "cov": cov}

        except KeyboardInterrupt:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/cronbachalpha", methods=['POST'])
def cronbachalpha():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            cronbachalpha = co.payaii(num_list1, num_list2)
            result = {"correlation": cronbachalpha}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/pbiserial", methods=['POST'])
def point_biserial():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            rval, pval = co.point_biserial(num_list1, num_list2)
            result = {"rval": rval, "pval": pval}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/mpbiserial", methods=['POST'])
def get_matrix_point_biserial():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            lists = []
            for l in headers:
                lists.append(csv[l])

            mpbiserial = co.get_matrix_point_biserial(*lists)
            result = mpbiserial
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/biserial", methods=['POST'])
def biserial():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            params = req_data['parameters']
            p1 = params['p1']
            p2 = params['p2']
            y = params['y']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            bserial = co.biserial(num_list1, num_list2, p1, p2, y)
            result = {"bserial": bserial}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/mbiserial", methods=['POST'])
def get_matrix_biserial():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            params = req_data['parameters']
            p1 = params['p1']
            p2 = params['p2']
            y = params['y']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            lists = []
            for l in headers:
                lists.append(csv[l])

            mpbiserial = co.get_matrix_biserial(p1, p2, y, *lists)
            result = mpbiserial
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/point_sum", methods=['POST'])
def get_kol_sum():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            data = pandas.read_csv(data_url)

            if 'weights' in req_data.keys():
                weights = req_data['weights']
                w = pandas.read_csv(weights)
            else:
                w = None

            result = co.get_nomre_kol_sum(data, w)
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/coefficient/point_mean", methods=['POST'])
def get_kol_mean():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            data = pandas.read_csv(data_url)

            if 'weights' in req_data.keys():
                weights = req_data['weights']
                w = pandas.read_csv(weights)
            else:
                w = None

            result = co.get_nomre_kol_mean(data, w)
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


# </editor-fold>

# <editor-fold desc="tests">

@app.route("/api/v1/test/chisquare", methods=['POST'])
def chisquare_test():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                chsq, pval = stt.chisquare_test(column)
                res.append({"chsq": chsq, "pval": pval})

            for j in range(len(num_list1)):
                result.append({j: res[j]})

        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/t", methods=['POST'])
def t():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = list(csv[headers[0]])
            num_list2 = list(csv[headers[1]])

            t, pval = stt.t_test(num_list1, num_list2)
            result = {"t": t, "pval": pval}

        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/anova", methods=['POST'])
def anova():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            lists = []
            for l in headers:
                lists.append(csv[l])

            fval, pval = stt.anova(*lists)
            result = {"fval": fval, "pval": pval}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/kruskal", methods=['POST'])
def kruskal():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            lists = []
            for l in headers:
                lists.append(csv[l])

            krusk, pval = stt.kruskal_test(*lists)
            result = {"krusk": krusk, "pval": pval}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/manwhit", methods=['POST'])
def mannwhitney_test():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            lists = []
            for l in headers:
                lists.append(csv[l])

            manwhit, pval = stt.mannwhitney_test(*lists)
            result = {"manwhit": manwhit, "pval": pval}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/median", methods=['POST'])
def mediantest():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            lists = []
            for l in headers:
                lists.append(csv[l])

            median, pval, m, table = stt.median_test(*lists)
            result = {"median": median, "pval": pval}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/normal", methods=['POST'])
def normalt():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values
            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                normal, pval = stt.normal_test(column)
                res.append({"normal": normal, "pval": pval})

            for j in range(len(num_list1)):
                result.append({j: res[j]})

        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/korvit", methods=['POST'])
def korvit():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            chi_square_value, p_value = stt.korvit(csv)
            result = {"chival": chi_square_value, "pval": p_value}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/kmo", methods=['POST'])
def kmo():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values

            lists = []
            for l in headers:
                lists.append(csv[l])

            kmo_all, kmo_model = stt.kmo(csv)
            result = {"kmo": kmo_model}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/efa", methods=['POST'])
def exploratory_factor_analyzer():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values

            lists = []
            for l in headers:
                lists.append(csv[l])

            loadings, communalities = stt.exploratory_factor_analyzer(csv)
            loads = []
            for row in loadings:
                for num in row:
                    loads.append(num)

            result = {"loadings": loads
                , "communalities": list(communalities)}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/cfa", methods=['POST'])
def confirmatory_factor_analyzer():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values

            lists = []
            for l in headers:
                lists.append(csv[l])

            loadings, varcovs, trans = stt.confirmatory_factor_analyzer(csv)

            varcovs = np.array(varcovs).flatten()
            trans = np.array(trans).flatten()
            loadings = np.array(loadings).flatten()

            result = {"loadings": loadings.tolist(), "trans": trans.tolist(), "varcovs": varcovs.tolist()}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/pearson", methods=['POST'])
def pearson_test():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            p_value = req_data['p_value']
            if "alpha" in req_data:
                alpha = req_data['alpha']
            else:
                alpha = 0.05

            correlation = stt.pearson_test(p_value, alpha)
            result = {"correlation": correlation}

        except Exception:
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/spearman", methods=['POST'])
def spearman_test():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            p_value = req_data['p_value']
            if "alpha" in req_data:
                alpha = req_data['alpha']
            else:
                alpha = 0.05

            correlation = stt.spearman_test(p_value, alpha)
            result = {"correlation": correlation}

        except Exception:
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/kendalltau", methods=['POST'])
def kendalltau_test():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            p_value = req_data['p_value']
            if "alpha" in req_data:
                alpha = req_data['alpha']
            else:
                alpha = 0.05

            correlation = stt.kendalltau_test(p_value, alpha)
            result = {"correlation": correlation}

        except Exception:
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/cramersv", methods=['POST'])
def cramersv_test():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            coeff = req_data['coefficient']
            if "alpha" in req_data:
                alpha = req_data['alpha']
            else:
                alpha = 0.95

            correlation = stt.cramersv_test(coeff, alpha)
            result = {"association": correlation}

        except Exception:
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/somersd", methods=['POST'])
def somersd_test():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            coeff = req_data['coefficient']
            if "alpha" in req_data:
                alpha = req_data['alpha']
            else:
                alpha = 0.95

            association, direction = stt.somersd_test(coeff, alpha)
            result = {"association": association, "direction": direction}

        except Exception:
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/tavafoghi", methods=['POST'])
def tavafoghi_test():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            coeff = req_data['coefficient']
            if "alpha" in req_data:
                alpha = req_data['alpha']
            else:
                alpha = 0.8

            agreement = stt.cohen_test(coeff, alpha)
            result = {"agreement": agreement}

        except Exception:
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/test/random", methods=['POST'])
def random_test():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)

            list = (csv[csv.columns[0]].values.tolist())

            if "alpha" in req_data:
                alpha = req_data['alpha']
            else:
                alpha = 0.05

            z, z_alpha = stt.random_test(list, alpha)
            result = {"z": z, "z_alpha": z_alpha}

        except Exception:
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
            'results': result
        }
        resp = jsonify(data)
        return resp


# </editor-fold>

# <editor-fold desc="clustering">
@app.route("/api/v1/clustering/kmeans", methods=['POST'])
def kmeans():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            parameter = req_data['parameters']
            ncluster = parameter['ncluster']
            csv = pandas.read_csv(data_url)

            labels, centroids = cls.kmeans(csv, ncluster)

            result = {"labels": labels, "centroids": centroids}

        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/clustering/dbscan", methods=['POST'])
def dbscan():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            parameter = req_data['parameters']
            eps = parameter['eps']
            minsample = parameter['minsample']
            csv = pandas.read_csv(data_url)
            labels = cls.dbscan(csv, eps, minsample)
            result = {"labels": labels.tolist()}

        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


# TODO its bullshit and dont use in production
@app.route("/api/v1/clustering/kmode", methods=['POST'])
def kmode():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            parameter = req_data['parameters']
            eps = parameter['eps']
            minsample = parameter['minsample']
            csv = pandas.read_csv(data_url)
            headers = csv.columns.values

            lists = []
            for l in headers:
                lists.append(csv[l])

            labels = cls.kmode(lists[1], 4, 5, 1)
            labels = np.array(labels).T.tolist()
            result = {"labels": labels}

        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


# </editor-fold>

# <editor-fold desc="imputation">
@app.route("/api/v1/imputation/knn", methods=['POST'])
def knn():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            parameters = req_data['parameters']
            k = parameters['k']
            csv = pandas.read_csv(data_url)

            labels = imp.imputation(csv, "knn", k)
            labels = labels.to_dict('dict')
            result = labels
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/imputation/regression", methods=['POST'])
def regression_imputation():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)

            labels = imp.imputation(csv, "regression")
            result = labels
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/imputation/person_mean", methods=['POST'])
def fard_imputation():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)

            labels = imp.imputation(csv, "fard")
            result = labels
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/imputation/q_mean", methods=['POST'])
def porsesh_imputation():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)

            labels = imp.imputation(csv, "porsesh")
            result = labels
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/imputation/hambaste", methods=['POST'])
def hambaste_imputation():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)

            labels = imp.imputation(csv, "hambaste")
            result = labels
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/imputation/corrected", methods=['POST'])
def corrected_imputation():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)

            labels = imp.imputation(csv, "corrected")
            result = labels
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/imputation/random", methods=['POST'])
def random():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            for column in csv:
                if csv[column].isnull().values.all():
                    csv.drop(columns=column, axis=1, inplace=True)
            headers = csv.columns.values

            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                labels = imp.imputation(column, "random")
                res.append(list(labels))
            for j in range(len(num_list1)):
                result.append({j: res[j]})

            # lists = []
            # for l in headers:
            #     lists.append(csv[l])
            #
            # labels = imp.imputation(lists[0], "random")
            # result = {"data": list(np.array(labels).flat)}
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/imputation/frequency", methods=['POST'])
def frequency_impute():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            for column in csv:
                if csv[column].isnull().values.all():
                    csv.drop(columns=column, axis=1, inplace=True)
            headers = csv.columns.values

            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                labels = imp.imputation(column, "frequency")
                res.append(list(labels))
            for j in range(len(num_list1)):
                result.append({j: res[j]})


        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


@app.route("/api/v1/imputation/mean", methods=['POST'])
def mean_impute():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            csv = pandas.read_csv(data_url)
            for column in csv:
                if csv[column].isnull().values.all():
                    csv.drop(columns=column, axis=1, inplace=True)
            headers = csv.columns.values

            num_list1 = []
            for head in headers:
                num_list1.append(list(csv[head]))
            res = []
            result = []
            for column in num_list1:
                labels = imp.imputation(column, "mean")
                res.append(list(labels))
            for j in range(len(num_list1)):
                result.append({j: res[j]})
        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


# </editor-fold>

# <editor-fold desc="outlier">
@app.route("/api/v1/outlier/isofarest", methods=['POST'])
def isofarest():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            data_url = req_data['data_file']
            parameter = req_data['parameters']
            max_samples = parameter['max_samples']
            csv = pandas.read_csv(data_url)
            labels = outlier.iso_farest(csv, max_samples)
            result = {"labels": (labels.tolist())}

        except Exception:
            # result = {"error": "bad param or no param"}
            bad_request()
        directory = current_path + '/dmtm_responses'
        response_url = dmtm_url + '/dmtm_responses'
        if not os.path.exists(directory):
            os.makedirs(directory)
        current_milli_time = lambda: int(round(time.time() * 1000))
        res_path = directory + '/' + str(current_milli_time()) + '.json'
        response_complete_url = response_url + '/' + str(current_milli_time()) + '.json'
        with open(res_path, 'w') as outfile:
            json.dump(result, outfile)
        data = {
            'result_file': response_complete_url,
        }
        resp = jsonify(data)
        return resp


# </editor-fold>


if __name__ == '__main__':
    app.run()
