import json
import os
import uuid
from typing import Dict
from datetime import datetime
import boto3
import humps

from functions.common.http_ import http_event_handler

ENV = os.getenv('ENV', 'local')
SERVICE = os.getenv('SERVICE', 'wedding-website-angular')
TARGET_BUCKET = f'{SERVICE}-rsvp-bucket-s3-{ENV}'

IS_DEPLOYED = False

# Leverage built-in sls offline env var (this could change)
if os.getenv('IS_DEPLOYED') == 'true':
    IS_DEPLOYED = True

if IS_DEPLOYED:
    s3 = boto3.client('s3')
else:
    print("Running non deployed, using sls-s3-local configuration.")
    s3 = boto3.client('s3',
                      endpoint_url='http://localhost:4569',
                      aws_access_key_id='S3RVER',
                      aws_secret_access_key='S3RVER')


@http_event_handler
def get(event, context) -> Dict:
    results = s3.list_objects(Bucket=TARGET_BUCKET, MaxKeys=1000)
    print(results)
    key_objects = results['Contents']
    parsed = [item['Key'] for item in key_objects]
    return {'data': parsed}


@http_event_handler
def post(event, context) -> Dict:
    # just write the key to s3
    payload = humps.decamelize(json.loads(event['body']))
    payload['effective_at'] = str(datetime.now())
    key = f'rsvp/{uuid.uuid4()}.json'
    s3.put_object(Bucket=TARGET_BUCKET, Key=key, Body=json.dumps(payload).encode('utf-8'))
    return {'data': 'success'}
