import json


def hello(event, context):
    body = {
        "message": "This is our first hello world function",
        "input": event
    }

    print(body['message'])

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response