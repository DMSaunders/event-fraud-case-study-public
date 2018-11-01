import pickle
import requests

# load in the model
model = pickle.load(open('clf.p', 'wb'))

# get new data point
api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'
url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'
sequence_number = 1
response = requests.post(url, json={'api_key': api_key,
                                    'sequence_number': sequence_number})
raw_data = response.json()

# vectorize input


# get prediction


# output prediction