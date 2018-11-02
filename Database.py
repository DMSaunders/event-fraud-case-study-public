import psycopg2 as pg2
from config import config


conn = pg2.connect(dbname='postgres', host='localhost') ## "user" input option available if necessary
conn.autocommit = True   ## This is required to remove or create databases

## Generally DON'T have autocommit true! If you make mistakes in changing your future tables,
## you can only rollback if you haven't committed those changes!

cur = conn.cursor()
cur.execute('CREATE DATABASE fraud_detection;')  #to create a PSQL database

cur.close() # This is optional
conn.close() # Closing the connection also closes all cursors (DO NOT FORGET TO DO!!!!!)

# We are connecting to the fraud_detection database we just created 
conn = pg2.connect(dbname='fraud_detection', host='localhost')
cur = conn.cursor()

def create_tables():
    """ create tables in the PostgreSQL database"""
    query = (
        """
        CREATE TABLE fraud_proba (
            fraud_prob NUMERIC,
            body_length INTEGER,
            channels INTEGER,
            country TEXT,
            currency TEXT,
            delivery_method NUMERIC,
            description TEXT,
            email_domain TEXT,
            event_created INTEGER,
            event_end INTEGER,
            event_published NUMERIC,
            event_start NUMERIC,
            fb_published INTEGER,
            has_analytics INTEGER,
            has_header NUMERIC,
            has_logo INTEGER,
            listed TEXT,
            name INTEGER,
            name_length INTEGER,
            object_id INTEGER,
            org_desc TEXT,
            org_facebook NUMERIC,
            org_name TEXT,
            org_twitter NUMERIC,
            payee_name TEXT,
            payout_type TEXT,
            previous_payouts TEXT [],
            sale_duration NUMERIC,
            show_map INTEGER,
            ticket_types TEXT [],
            user_age INTEGER,
            user_created INTEGER,
            user_type INTEGER,
            venue_address TEXT,
            venue_country TEXT,
            venue_latitude NUMERIC,
            venue_longitude NUMERIC,
            venue_name TEXT,
            venue_state TEXT,
        );
        """
    
    cur.execute(query) 
    conn.commit()
        
        
        
'''
        'body_length': 327, 
        'channels': 6, 
        'country': 'GB', 
        'currency': 'GBP', 
        'delivery_method': 0.0, 
        'description': '<p>\xa0</p>\r\n<p>Make sure love is in, 
        'email_domain': 'yahoo.co.uk', 
        'event_created': 1359909172, 
        'event_end': 1361008800, 
        'event_published': 1359909816.0, 
        'event_start': 1360983600, 
        'fb_published': 0, 
        'has_analytics': 0, 
        'has_header': 0.0, 
        'has_logo': 1, 
        'listed': 'y', 
        'name': 'Valentines Weekend Dinner', 
        'name_length': 25, 
        'object_id': 5404222, 
        'org_desc': '<p>PARTY AND EVENTS ORGANISER.</p>', 
        'org_facebook': 0.0, 
        'org_name': 'RJ PARTY TIME', 
        'org_twitter': 0.0, 
        'payee_name': '', 
        'payout_type': 'ACH', 
        'previous_payouts': [], 
        'sale_duration': 12.0, 
        'show_map': 1, 
        'ticket_types': [{'event_id': 5404222, 'cost': 110.0, 'availability': 1, 'quantity_total': 180}], 
        'user_age': 0, 
        'user_created': 1359908855, 
        'user_type': 1, 
        'venue_address': 'Reservoir Road', 
        'venue_country': 'GB', 
        'venue_latitude': 52.4771249, 
        'venue_longitude': -1.9322993, 
        'venue_name': ' Tower ballroom', 
        'venue_state': 'Birmingham'}]
'''
        
        
        
        
def insert_to_database(example_data, prediction):
    
    '''
    Adds prediction to the example_data as the first column
    
    Inserts that row into the database fraud_proba
    
    '''
    
    dataframe = pd.read_json(example_data)
    dataframe['fraud_prob'] = prediction
    
    sqldata = pd.dataframe.to_sql('fraud_proba')
    
    
    sql = "INSERT INTO fraud_proba VALUES(%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, (prediction, example_data))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()