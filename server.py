from flask import Flask, request, jsonify, Response
import pickle
import pandas as pd
import predict
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/score', methods=['GET'])
def import_DB():
    #THE QUERY
    #feature_importances = feature_table.scan()      uncomment when feature table ready
    x = table.scan()
    return x
    #return {feature_importances, x}     uncomment when feature table ready, not sure about format


#needs to output
# {causes:{1,2,3
#   },
# datapoint:{all records incl pred, label
#   }
# }

#so far it only does the datapoints, and the causes are hardcoded  del this line when feature table ready

if __name__ == '__main__':
    #connect to the dynamodb once
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table('fraud_detection')
    #feature_table = dynamo.Table('feature_table')    uncomment when feature table ready
    
    #run the app
    app.run(host='0.0.0.0', port=8080, debug=True)