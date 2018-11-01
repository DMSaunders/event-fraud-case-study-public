import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def data_clean():
    
    data = pd.read_json('data/data.zip')
    
    #Creates a Fraud column of True or False for each event.
    data['Fraud'] = (data['acct_type'] == 'fraudster_event') | 
                    (data['acct_type'] == 'fraudster') | 
                    (data['acct_type'] == 'fraudster_att')
            
    #Drops all columns that we cannot use
    data = data.drop(['approx_payout_date', 'body_length', 'gts', 'num_order', 'num_payouts', 'sale_duration2'], axis = 1)
    
    return data


def rand_for(X, y):
    
    #Train and split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    #Create RandomForestClassifier and train it
    clf = RandomForestClassifier(n_estimators=100, max_depth=3)
    clf.fit(X_train, y_train)
    
    return clf.predict(X_test)