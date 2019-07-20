from scipy import stats
import numpy as np
import descriptive_feature as tt
import coefficient as co
import json

# x = ["asd","dsa","asds"]
# y = ["asd","dsa","asddds"]
# # y = [2, 4, 5, 7, 8, 33, 11, 25, 26, 27, 36]
# print(x)
#
# m = co.cramers_v(x,y)
# print(m)
obj = {'content': 'something goes here'}
json_obj = json.dumps(obj)
json_size = len(json_obj)

