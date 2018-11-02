import pickle
import requests
import sys
import pandas as pd
import fraud_clean_with_categorical_features as f


if __name__ == "__main__":

    # load in the model
    # model = pickle.load(open('clf.p', 'wb'))

    # get new data point
    api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'
    url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'
    sequence_number = 1
    response = requests.post(url, json={'api_key': api_key,
                                        'sequence_number':  sequence_number})
    raw_data = response.json()

    # check if already in data base


    # transformations
    data_point = pd.DataFrame.from_dict(raw_data['data'])
    data_point = f.drop_cols(raw_data)
    data = select_features(raw_data)
    data = f.one_hot_with_nan(data)
    data = f.one_hot_without_nan(data)
    data = f.drop_nan(data)


    # get prediction probability
    prediction = model.predict_proba(data)


    # get prediction label (Low, Med, High)


    # get feature importances, top 3?


    # output prediction
    sys.stdout.write(prediction)