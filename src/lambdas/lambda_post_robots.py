import boto3
import uuid

def gen_id():
    id = str(uuid.uuid4())
    id = id[:13]
    return id

def create_queue(params, ID):
    sqsc = boto3.client('sqs')
    ID = str(ID)
    response = sqsc.create_queue(
        QueueName=ID+'-'+params['NAME']+'-sqsq',
    )
    return response['QueueUrl']

def put_robot(event, id, queueurl):
    '''Create a unique ID for each robot to not give away how many we have. Then give it a name. '''
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('Robots')
    try:
        response = table.put_item(Item={
        'ID': id,
        'NAME': event['NAME'],
        'MODEL': event['MODEL'],
        'VIDEO': event['VIDEO'],
        'CONNECTION': event['CONNECTION'],
        'LOCATION': event['LOCATION'],
        'REGISTERED': event['REGISTERED'],
        'SQSQ': queueurl
        })
    except KeyError:
        response = table.put_item(Item={
        'ID': id,
        'NAME': event['NAME']
        })
    return id

def lambda_handler(event, context):
    ''' Standard lambda handler. '''
    roboid = gen_id()
    queueurl = create_queue(event, roboid)
    result = put_robot(event, roboid, queueurl)
    return {
        'statusCode': 200,
        'QueueUrl': queueurl
    }

if __name__ == "__main__":
    pass