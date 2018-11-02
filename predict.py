import pickle
import requests
import sys
import pandas as pd
# import fraud_clean_with_categorical_features as f
import fraud_model_building as f
from time import sleep
import requests
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

key_features = ['user_age', 'user_type', 'has_logo']

# recursively delete empty strings
def del_empty(d):
    """
    Delete keys with the value ``None`` in a dictionary, recursively.
    This alters the input so you may wish to ``copy`` the dict first.
    """
    # For Python 3, write `list(d.items())`; `d.items()` won't work
    # For Python 2, write `d.items()`; `d.iteritems()` won't work
    for key, value in list(d.items()):
        if value == '':
            del d[key]
        elif isinstance(value, dict):
            del_empty(value)
    return d  # For convenience

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('fraud_detection')

if __name__ == "__main__":
    while True:
        time.sleep(60)

        # load in the model
        # model = pickle.load(open('clf.p', 'wb'))

        # get new data point
        api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'
        url =   'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'
        sequence_number = 1
        response = requests.post(url, json={'api_key': api_key,
                                            'sequence_number':      sequence_number})
        raw_data = response.json()

        # check if already in data base

        # transformations
        data = pd.DataFrame.from_dict(raw_data['data'])
        data = f.clean_new_data_point()

        # get prediction probability
        prediction = model.predict_proba(data)


        # get prediction label (Low, Med, High)
        if prediction < 0.01:
            label = 'Low'
        elif prediction < 0.02
            label = "Medium"
        else:
            label = "High"

        # combine predictions with original record
        full_data = pd.DataFrame.from_dict(raw_data['data'])
        full_data['fraud_probablility'] = prediction
        full_data['fraud_label'] = label

        # write to database
        json_str = json.dumps(full_data.to_json())

        # convert floats to string
        item = json.loads(json_str, parse_float=str) 

        # Adding an item to the database
        table.put_item(
           Item=
                del_empty(item)
        )

