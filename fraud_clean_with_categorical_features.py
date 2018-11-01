import pandas as pd
import numpy as np

def drop_cols():
    
    data = pd.read_json('data/data.zip')
    
    #Creates a Fraud column of True or False for each event.
    data['Fraud'] = (data['acct_type'] == 'fraudster_event') | (data['acct_type'] == 'fraudster') | (data['acct_type'] == 'fraudster_att')
            
    #Drops all columns that we cannot use due to API
    data = data.drop(['acct_type','approx_payout_date', 'body_length', 'gts', 'num_order', 'num_payouts', 'sale_duration2'], axis = 1)
    
    #drop columns we cannot use at the time of prediction
    data = data.drop(['payout_type', 'sale_duration', 'delivery_method'], axis = 1)
    
    #drop cols I cannot categorize
    data = data.drop(['description', 'name', 'org_desc', 'org_name', 'payee_name', 'previous_payouts', 'ticket_types', 'venue_address', 'venue_name'], axis=1)
    
    #drop cols too cumbersome to categorize
    data = data.drop(['email_domain', 'org_facebook', 'org_twitter'], axis=1)
    
    return data


#create dummy of header before removing missing vals
def one_hot_with_nan(input_df):
    '''
    One-hot encode the provided list of columns and return a new copy of the data frame
    '''
    df = input_df.copy()

    columns = ['has_header', 'country', 'venue_country', 'venue_state']

    for col in columns:
        dummies = pd.get_dummies(df[col], prefix=col,dummy_na=True, drop_first=True)
        #dummies.drop(dummies[col], axis=1, inplace=True)
        df = df.drop(col, axis=1).merge(dummies, left_index=True, right_index=True)
    
    return df


def one_hot_without_nan(input_df):
    '''
    One-hot encode the provided list of columns and return a new copy of the data frame
    '''
    df = input_df.copy()
    columns = ['listed', 'currency', 'user_type', 'channels']

    for col in columns:
        dummies = pd.get_dummies(df[col], prefix=col, drop_first=True)
        #dummies.drop(dummies[col], axis=1, inplace=True)
        df = df.drop(col, axis=1).merge(dummies, left_index=True, right_index=True)
    
    return df


def drop_nan(data):
    df = data.dropna(how='any')
    
    return df
