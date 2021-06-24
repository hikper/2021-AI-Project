# # -*- coding: utf-8 -*-
# """ai_fp_route_optimization.ipynb
#
# Automatically generated by Colaboratory.
#
# Original file is located at
#     https://colab.research.google.com/drive/1mkd8zWzcmFTUBYzIR-kt1emzqieAt2Uz
#
# import 函式庫
# """
#
# import glob
# import json
# import numpy as np
# from tensorflow import keras
# from tensorflow.keras.layers import Dense
# from tensorflow.keras.models import Sequential
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.layers import Dropout
# from sklearn.preprocessing import MaxAbsScaler
# from sklearn.preprocessing import OneHotEncoder
# from keras.models import load_model
#
# ALL_CHARACTERS = ['DEFECT', 'IRONCLAD', 'THE_SILENT', 'WATCHER']
#
# class Route_ai:
#     """docstring for Route_ai."""
#
#     def __init__(self):
#         self.model=load_model('AI_FP_ROUTE.h5')
#
#     def encode_single(self, value, category):
#       np_array = np.array([[value]])
#       encoder = OneHotEncoder(categories=[category], sparse=False)
#       onehot_encoded = encoder.fit_transform(np_array)
#       collapsed = np.sum(onehot_encoded, axis=0)
#       # inverse = encoder.inverse_transform(collapsed[np.newaxis, ...])
#       # print(np.array_equal(np_array, inverse))
#       return collapsed
#
#     def encode_character(self):
#       """
#       Encode the chosen character into a one-hot vector of length ALL_CHARACTERS
#       """
#       return np.array([0,0,0,0])
#
#     def encode_sample_with_loop(self, sample):
#       """
#       Encode a single sample into a 1D vector
#       [{"cards": 10, "relics": 1, "ascension": 20, "character": "IRONCLAD", "floor": 0, "potions": 0, "path": "M", "max_hp": 82, "current_hp": 82, "gold": 99, "value": 2884.076040777472, "upgrade_cards": 0, "curse_cards": 1}
#       """
#       # character=self.encode_character()
#      # print(character)
#       num_data = np.array([sample['cards'],sample['relics'],sample['ascension'],sample['floor'],sample['potions'],ord(sample['path']),sample['max_hp'],sample['current_hp'],sample['gold'],sample['upgrade_cards'],sample['curse_cards']])
#       # x=np.concatenate((character, num_data))
#       #print(len(x))
#       # return  x
#       return num_data
#
#     def preprocess_with_loop(self, data):
#       preprocess_list=[]
#       y=[]
#       for i,sample in enumerate(data):
#         if sample['path']!= None:
#           preprocess_list.append(self.encode_sample_with_loop(sample))
#           y.append(sample['value'])
#       X=np.vstack(preprocess_list)
#       #print(len(X))
#       Y=np.array(y,dtype='float64')
#       #print(len(Y))
#       return X,Y
#
#     def scale_X(self, X_data):
#       """
#       Used with one hot encoded model
#       """
#       X_copy = np.copy(X_data)
#       max_abs_scaler = MaxAbsScaler()
#       X_maxabs = max_abs_scaler.fit_transform(X_copy)
#     #  with open('input_scales.json', 'w') as out_file:
#      #   json.dump(max_abs_scaler.scale_.tolist(), out_file)
#       return X_maxabs
#
#     def scale_Y(self, Y_data):
#       Y_copy = np.copy(Y_data)
#
#       # Scale Y
#       Y_copy /= 10
#
#       # To allow healing (negative damage), uncomment `Y[Y < -1] = -1` and comment out `Y[Y < 0] = 0`
#       #Y_copy[Y_copy < -1] = -1 # Healing (negative damage)
#       # Y_copy[Y_copy < 0] = 0 # No healing
#
#       # Cap damage taken at 100
#       Y_copy[Y_copy > 800] = 800
#       return Y_copy
#
#     def predict(self, data):
#       return self.model.predict(scale_X(encode_sample_with_loop(data)))*10

class Route_ai:
    def __init__(self):
        self.d = {'R': 1000, 'E': 10, '$': 100, '?': 100, 'M': 1, 'T': 0}
    def predict(self, state):
        return self.d[state['path']]
