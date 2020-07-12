"""
ERM Lambda to add new robot to DDB table
Adam Phelps 7/11/2020
"""

import uuid
import boto3


def gen_id():
    """ Shorten the UUID for user friendliess. """
    robo_id = str(uuid.uuid4())
    robo_id = robo_id[:13]
    return robo_id


def create_queue(params, robo_id):
    """ For security we create an SQS queue for each robot. """
    sqsc = boto3.client('sqs')
    robo_id = str(robo_id)
    response = sqsc.create_queue(
        QueueName=robo_id + '-' + params['NAME'] + '-sqsq',
    )
    return response['QueueUrl']


def put_robot(event, robo_id, queueurl):
    """Create a unique ID for each robot to not give away how many we have. Then give it a name. """
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('Robots')
    try:
        table.put_item(Item={
            'ID': robo_id,
            'NAME': event['NAME'],
            'MODEL': event['MODEL'],
            'VIDEO': event['VIDEO'],
            'CONNECTION': event['CONNECTION'],
            'LOCATION': event['LOCATION'],
            'REGISTERED': event['REGISTERED'],
            'SQSQ': queueurl
        })
    except KeyError:
        table.put_item(Item={
            'ID': robo_id,
            'NAME': event['NAME']
        })
    return robo_id


def lambda_handler(event, context):
    """ Standard lambda handler. """
    roboid = gen_id()
    queueurl = create_queue(event, roboid)
    result = put_robot(event, roboid, queueurl)
    return {
        'statusCode': 200,
        'QueueUrl': queueurl,
        'robo_id': result
    }
