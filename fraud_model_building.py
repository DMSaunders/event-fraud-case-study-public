import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import recall_score, classification_report, confusion_matrix, roc_auc_score
from sklearn.metrics import make_scorer
import pickle


def data_clean(data):
        
    #Creates a Fraud column of True or False for each event.
    data['Fraud'] = ((data['acct_type'] == 'fraudster_event') | 
                    (data['acct_type'] == 'fraudster') | 
                    (data['acct_type'] == 'fraudster_att'))
            
    #Drops all columns that we cannot use
    data = data.drop(['approx_payout_date', 'body_length', 'gts', 'num_order', 'num_payouts', 'sale_duration2', 'payout_type', 'sale_duration'], axis = 1)
    
#    'channels', 'country', 'currency', 'delivery_method', 'description', 'email_domain', 'event_created', #'event_end', 'event_published', 'event_start', 'fb_published', 'has_analytics', 'has_header', 'has_logo', #'listed', 'name', 'name_length', 'object_id', 'org_desc', 'org_facebook', 'org_name', 'org_twitter', #'payee_name', 'previous_payouts', 'show_map', 'ticket_types', 'user_age', 'user_created', 'user_type', #'venue_address', 'venue_country', 'venue_latitude', 'venue_longitude', 'venue_name', 'venue_state'

    
    #Drops all columns that are non-numerical
    data = data[['Fraud','delivery_method', 'event_created', 'event_end', 'event_published', 'event_start', 'fb_published', 'has_analytics', 'has_header',	'has_logo', 'object_id', 'org_facebook', 'org_twitter', 'show_map', 'user_age', 'user_created', 'user_type', 'venue_latitude',	'venue_longitude']]
    
    
#     set up new features event_duration and event_work_duration
    data['event_duration']=(data['event_end']-data['event_start'])/86400
    # data['event_work_duration']=(data['event_published']-data['event_created'])/86400
    data = data.drop(['event_start','event_end','event_published','event_created'],axis=1)
    data = data.dropna(axis=1)
    
#     data = feature.drop_cols()
#     data = feature.one_hot_with_nan(data)
#     data = feature.one_hot_without_nan(data)
#     data= feature.drop_nan(data)

    return data
     
def clean_new_data_point(data_point):
    # Drops all columns that are non-numerical
    data = data_point[['event_created', 'event_end', 'event_published', 'event_start', 'fb_published', 'has_analytics', 'has_logo', 'object_id',  'show_map', 'user_age', 'user_created', 'user_type']]
    
    
    # set up new features event_duration and event_work_duration
    data['event_duration']=(data['event_end']-data['event_start'])/86400
    # data['event_work_duration']=(data['event_published']-data['event_created'])/86400
    data = data.drop(['event_start','event_end','event_published','event_created'],axis=1)
    data = data.dropna(axis=1)

    return data

def define_features_and_target(dataframe, target):
    X = dataframe.drop(target, axis=1)
    y = dataframe[target]
    return X, y

def split_data(X, y):
    # split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return X_train, X_test, y_train, y_test

def g_boost(X_train, y_train):
    #Create Gradient Boosted Classifier and train it
    clf = GradientBoostingClassifier()
    clf.fit(X_train, y_train)
    print(clf.feature_importances_)
    return clf

def get_predictions(fit_model, X_test):
    return fit_model.predict(X_test)

def score_model(y_test, predictions):
    return recall_score(y_test, predictions)


################################################################
if __name__ == '__main__':
    data = pd.read_json('data/data.zip')
    data = data_clean(data)
    X, y = define_features_and_target(data, 'Fraud')
    X_train, X_test, y_train, y_test = split_data(X, y)

    # p = Pipeline([
    #     ('filter', FilterColumns()),
    #     ('type_change', DataType()),
    #     ('replace_outliers', ReplaceOutliers()),
    #     ('compute_age', ComputeAge()),
    #     ('nearest_average', ComputeNearestMean()),
    #     ('columns', ColumnFilter()),
    #     ('lm', LinearRegression())
    # ])
    # df = df.reset_index()

    # GridSearch
    params = {
        'learning_rate' : [0.1],
        'n_estimators' : [1000, 2000],
        'subsample' : [0.5, 0.3],
        'min_samples_split' : [2, 3],
        'max_depth' : [5, 7],
    }

    # Turns our recall func into a scorer of the type required
    # by gridsearchcv.
    recall_scorer = make_scorer(score_model, greater_is_better=True)
    gb = GradientBoostingClassifier()
    gscv = GridSearchCV(gb, param_grid=params,
                        scoring='recall',
                        cv=3,
                        n_jobs=-1)
    clf = gscv.fit(X_train, y_train)

    print('Best parameters: {}'.format(clf.best_params_))
    print('Best Recall: {}'.format(clf.best_score_))
    
    gb = GradientBoostingClassifier(learning_rate= clf.best_params_['learning_rate'],max_depth=clf.best_params_['max_depth'],n_estimators=clf.best_params_['n_estimators'],subsample = clf.best_params_['subsample'])

    gb.fit(X_train, y_train)
    print("Out of sample Recall: {}".format(cross_val_score(gb, X_test, y_test, cv = 3, scoring='recall')))
    
# pickle.dump(gb,open('fraud_model.p','wb'))