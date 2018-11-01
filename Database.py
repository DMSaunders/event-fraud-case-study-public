import psycopg2
from config import config


CREATE DATABASE fraud_detection

conn = psycopg2.connect(host="localhost",database="fraud_detection", user="postgres", password="postgres")


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE fraud_proba (
            fraud_prob INTEGER NOT NULL,
            body_length
            channels
            country
            currency
            delivery_method
            description
            email_domain
            event_created
            event_end
            event_published
            event_start
            fb_published
            has_analytics
            has_header
            has_logo
            listed
            name
            name_length
            object_id
            org_desc
            org_facebook
            org_name
            org_twitter
            payee_name
            payout_type
            previous_payouts
            sale_duration
            show_map
            ticket_types
            
            user_age
            user_created
            user_type
            venue_address
            venue_country
            venue_latitude
            venue_longitude
            venue_name
            venue_state
            
            
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """
        
'''
        'body_length': 327, 'channels': 6, 'country': 'GB', 'currency': 'GBP', 'delivery_method': 0.0, 'description': '<p>\xa0</p>\r\n<p>Make sure love is in the air in February with an array of Valentines weekend ideas to choose from. If you’re looking for something slightly more adventurous than flowers and chocolates come Celebrate your achievement with a glass or two of champagne, and toast a memorable Valentines weekend 2013 Dinner party.</p>', 'email_domain': 'yahoo.co.uk', 'event_created': 1359909172, 'event_end': 1361008800, 'event_published': 1359909816.0, 'event_start': 1360983600, 'fb_published': 0, 'has_analytics': 0, 'has_header': 0.0, 'has_logo': 1, 'listed': 'y', 'name': 'Valentines Weekend Dinner', 'name_length': 25, 'object_id': 5404222, 'org_desc': '<p>PARTY AND EVENTS ORGANISER.</p>', 'org_facebook': 0.0, 'org_name': 'RJ PARTY TIME', 'org_twitter': 0.0, 'payee_name': '', 'payout_type': 'ACH', 'previous_payouts': [], 'sale_duration': 12.0, 'show_map': 1, 'ticket_types': [{'event_id': 5404222, 'cost': 110.0, 'availability': 1, 'quantity_total': 180}], 'user_age': 0, 'user_created': 1359908855, 'user_type': 1, 'venue_address': 'Reservoir Road', 'venue_country': 'GB', 'venue_latitude': 52.4771249, 'venue_longitude': -1.9322993, 'venue_name': ' Tower ballroom', 'venue_state': 'Birmingham'}]
'''