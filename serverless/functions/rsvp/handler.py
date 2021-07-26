import json
import os
from typing import Dict

import boto3


TARGET_BUCKET = 'wedding-website-angular-rsvp-bucket-s3-dev'
IS_DEPLOYED = False
DEFAULT_LAMBDA_RESPONSE = {
    'isBase64Encoded': False,
    'statusCode': 200,
    'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': True
    },
    'body': 'default response'
}

# Leverage built-in sls offline env var (this could change)
if os.getenv('IS_OFFLINE') != 'true':
    IS_DEPLOYED = True

if IS_DEPLOYED:
    s3 = boto3.client('s3')
else:
    print("Running non deployed, using sls-s3-local configuration.")
    s3 = boto3.client('s3',
                      endpoint_url='http://localhost:4569',
                      aws_access_key_id='S3RVER',
                      aws_secret_access_key='S3RVER')


def get(event, context) -> Dict:
    results = s3.list_objects(Bucket=TARGET_BUCKET, MaxKeys=1000)
    print(results)
    key_objects = results['Contents']
    parsed = [item['Key'] for item in key_objects]
    
    response = DEFAULT_LAMBDA_RESPONSE.copy()
    response['body'] = json.dumps(parsed, default=lambda o: o.__str__())
    print(response)
    return response


def post(event, context) -> Dict:
    # just write the key to s3
    payload = json.loads(event['body'])

    first_name = payload['first_name']
    last_name = payload['last_name']
    email = payload['email']
    attending = payload['attending']
    number_attending = payload['number_attending']

    key = f'rsvp/{first_name}-{last_name}-{email}-{attending}-{number_attending}'
    print(key)
    s3.put_object(Bucket=TARGET_BUCKET, Key=key, Body=b'')

    return {'message': 'success'}
