"""
Enj Manager Post Command lambda Python
Adam Phelps 7/6/2020
"""

import boto3


def post_command(event: dict) -> bool:
    """ Post to robot SQS queue. """
    try:
        sqs = boto3.client('sqs')
        queue_url = event['SQSQ']
        sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageAttributes={
                'Command': {
                    'DataType': 'String',
                    'StringValue': event['commandname']
                }
            },
            MessageBody=(event['commandbody'])
        )
        return "Command succeeded."
    except Exception:
        return "Command failed."


def lambda_handler(event, context):
    """ Standard lambda handler. """
    result = post_command(event)
    return {
        'statusCode': 200,
        'statusCommand': result
    }
