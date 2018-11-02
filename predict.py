import pickle
import requests
import sys
import pandas as pd
# import fraud_clean_with_categorical_features as f
import fraud_model_building as f

features = model.feature_

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
    data = pd.DataFrame.from_dict(raw_data['data'])
    # data_point = f.drop_cols(raw_data)
    # data = select_features(raw_data)
    # data = f.one_hot_with_nan(data)
    # data = f.one_hot_without_nan(data)
    # data = f.drop_nan(data)
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

    # output prediction, whole record

    full_data = pd.DataFrame.from_dict(raw_data['data'])
    full_data['fraud_probablility'] = prediction
    full_data['fraud_label'] = label
    sys.stdout.write(full_data.to_json())

