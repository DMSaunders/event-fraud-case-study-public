from flask import Flask, request, jsonify, Response
import pickle
import pandas as pd
import predict
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

app = Flask(__name__)

@app.route('/score', methods=['GET'])
def import_DB():
    #THE QUERY
    x = table.scan()
    items = x['Items']
    return items

#needs to output
# {causes:{1,2,3},
# datapoint:{all records incl pred, label}
# }

#so far it only does the datapoints, and the causes are hardcoded

if __name__ == '__main__':
    #connect to the dynamodb once
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table('fraud_detection')
    
    #run the app
    app.run(host='0.0.0.0', port=8080, debug=True)