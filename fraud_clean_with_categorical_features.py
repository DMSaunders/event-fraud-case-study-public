import pandas as pd
import numpy as np

def drop_cols():
    
    data = pd.read_json('data/data.zip')
    
    #Creates a Fraud column of True or False for each event.
    data['Fraud'] = (data['acct_type'] == 'fraudster_event') | (data['acct_type'] == 'fraudster') | (data['acct_type'] == 'fraudster_att')
            
    #Drops all columns that we cannot use due to API
    data = data.drop(['acct_type','approx_payout_date', 'body_length', 'gts', 'num_order', 'num_payouts', 'sale_duration2'], axis = 1)
    
    #drop columns we cannot use at the time of prediction
    data = data.drop(['payout_type', 'sale_duration', ], axis = 1)
    
    #drop cols I cannot categorize
    data = data.drop(['description', 'name', 'org_desc', 'org_name', 'payee_name', 'previous_payouts', 'ticket_types', 'venue_address', 'venue_name'], axis=1)
    
    #drop cols too cumbersome to categorize
    data = data.drop(['email_domain'], axis=1)
    
    #drop cols with too much missing data
    data = data.drop(['has_header'], axis=1)
    
    return data