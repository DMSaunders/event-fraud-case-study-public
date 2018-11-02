import pickle
import requests
import sys
import pandas as pd
import fraud_clean_with_categorical_features as f

# load in the model
model = pickle.load(open('clf.p', 'wb'))

# get new data point
api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'
url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'
sequence_number = 1
response = requests.post(url, json={'api_key': api_key,
                                    'sequence_number': sequence_number})
raw_data = response.json()

# keep = ['event_created', 'event_end', 'event_published', 'event_start', 'fb_published','has_analytics', 'has_header', 'has_logo', 'object_id', 'org_facebook','org_twitter', 'show_map', 'user_age', 'user_created', 'user_type','venue_latitude' 'venue_longitude']

# def select_features(data_point):
#     '''
#     takes in a new data point and keeps only relevant features
#     '''
#     clean = {}
#     data_point = data_point['data'][0]
#     for key, value in data_point.items():
#         if key in keep:
#             clean.update({key: value})
#     return data_point

data_point = pd.DataFrame.from_dict(raw_data['data'])
data_point = f.drop_cols(raw_data)
data_point

# transformations
data = select_features(raw_data)
data = f.one_hot_with_nan(data)
data = f.one_hot_without_nan(data)
data = f.drop_nan(data)

# get prediction
prediction = model.predict(data)

# output prediction
sys.stdout.write(prediction)