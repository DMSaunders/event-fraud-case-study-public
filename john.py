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
            
    #Drops all columns that we cannot use
    data = data.drop(['approx_payout_date', 'body_length', 'gts', 'num_order', 'num_payouts', 'sale_duration2'], axis = 1)
    

#    'channels', 'country', 'currency', 'delivery_method', 'description', 'email_domain', 'event_created', #'event_end', 'event_published', 'event_start', 'fb_published', 'has_analytics', 'has_header', 'has_logo', #'listed', 'name', 'name_length', 'object_id', 'org_desc', 'org_facebook', 'org_name', 'org_twitter', #'payee_name', 'previous_payouts', 'show_map', 'ticket_types', 'user_age', 'user_created', 'user_type', #'venue_address', 'venue_country', 'venue_latitude', 'venue_longitude', 'venue_name', 'venue_state'

    
    #Drops all columns that are non-numerical
    data = data(['Fraud', 'channels', 'delivery_method', 'event_created', 'event_end', 'event_published', 'event_start', 'fb_published', 'has_analytics', 'has_header',	'has_logo', 'object_id', 'org_facebook', 'org_twitter', 'sale_duration', 'show_map', 'user_age', 'user_created', 'user_type', 'venue_latitude',	'venue_longitude'])
    return data

    #Only numeric columns
    

def rand_for(X, y):
    
    #Split the data
    
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    #Create RandomForestClassifier and train it
    clf = RandomForestClassifier(n_estimators=100, max_depth=3)
    clf.fit(X_train, y_train)
    clf.predict(X_test)
    
    return print(clf.feature_importances_())