import os
import json
import boto3
import datetime
import hashlib
from risk_score import *

dynamodb = boto3.resource('dynamodb')

def calculate_hash(event):
    m = hashlib.sha3_512()
    for key in event:
        m.update(bytes(str(event[key]),'utf-8'))
    return m.hexdigest()

def lambda_handler(event, context):
    table = dynamodb.Table(os.environ['DYNAMO_TBL'])
    
    score = calculate_score(event)
    
    event['timestamp'] = datetime.utcnow().isoformat()
    event['score'] = score
    event['risk_level'] = risk_level(score)
    
    data = {
        'hash_id': calculate_hash(event),
        'data': event
    }
    
    table.put_item(
        Item = data
    )
    
    response = {
            "hash_id": data['hash_id'],
            "timestamp": event['timestamp'],
            "risk_score": event['risk_score'],
            "risk_level": event['risk_level']
        }
            
    return {
        'statusCode': 200,
        'body': response
    }
