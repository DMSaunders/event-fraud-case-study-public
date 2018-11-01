import pickle
import requests
import sys

# load in the model
model = pickle.load(open('clf.p', 'wb'))

# get new data point
api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'
url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'
sequence_number = 1
response = requests.post(url, json={'api_key': api_key,
                                    'sequence_number': sequence_number})
raw_data = response.json()

keep = ['event_created', 'event_end', 'event_published', 'event_start', 'fb_published','has_analytics', 'has_header', 'has_logo', 'object_id', 'org_facebook','org_twitter', 'show_map', 'user_age', 'user_created', 'user_type','venue_latitude' 'venue_longitude']

def select_features(data_point):
    '''
    takes in a new data point and keeps only relevant features
    '''
    clean = {}
    data_point = data_point['data'][0]
    for key, value in data_point.items():
        if key in keep:
            clean.update({key: value})
    return data_point

# select relevant features
data = select_features(raw_data)

# one-hot categorical features


# get prediction
prediction = model.predict(data)

# output prediction
sys.stdout.write(prediction)