import json

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


def http_event_handler(func):
    def wrapper(event, context):
        result = func(event, context)
        response = DEFAULT_LAMBDA_RESPONSE.copy()
        response['body'] = json.dumps(result, default=lambda o: o.__str__())
        return response

    return wrapper
