import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def data_clean():
    
    data = pd.read_json('data/data.zip')
    
    #Creates a Fraud column of True or False for each event.
    data['Fraud'] = ((data['acct_type'] == 'fraudster_event') | 
                    (data['acct_type'] == 'fraudster') | 
                    (data['acct_type'] == 'fraudster_att'))
    
    #Fill Na with 0 - not a good solution
    data.fillna(0, inplace =True)
    
    #Target variable
    y = data['Fraud']

    #Only numeric columns
    X = data[['delivery_method', 'event_created', 'event_end', 'event_published', 'event_start', 'fb_published', 'has_analytics', 'has_header',	'has_logo', 'object_id', 'org_facebook', 'org_twitter', 'show_map', 'user_age', 'user_created', 'user_type', 'venue_latitude',	'venue_longitude']] 
    
    return X, y

def rand_for(X, y):
    
    #Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    #Create RandomForestClassifier and train it
    clf = RandomForestClassifier(n_estimators=175, max_depth=20)
    clf.fit(X_train, y_train)

    return clf

def predict_proba(model, new_X):
    
    X = new_X[['delivery_method', 'event_created', 'event_end', 'event_published', 'event_start', 'fb_published', 'has_analytics', 'has_header',	'has_logo', 'object_id', 'org_facebook', 'org_twitter', 'show_map', 'user_age', 'user_created', 'user_type', 'venue_latitude',	'venue_longitude']] 
    
    X.fillna(0, inplace=True)
    
    return model.predict_proba(X)