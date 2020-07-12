"""
Allows the enj agent to get tasks
Adam Phelps 7/5/2020
"""

import boto3

def get_task(event: dict):
    """ Receive an SQSQ message (if any) for the robot to process. """
    try:
        sqs = boto3.client('sqs')
        queue_url = event['SQSQ']
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=[
                'Command'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'ALL'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )
        print(response['Messages'][0])
        print(response['Messages'][0]['ReceiptHandle'])
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=response['Messages'][0]['ReceiptHandle']
        )
        return response
    except Exception as e:
        print(e)

def lambda_handler(event, context):
    """ Standard lambda handler. """
    result = get_task(event)
    return {
        'statusCode': 200,
        'response': result
    }
