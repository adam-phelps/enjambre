import boto3
import uuid

def put_robot(event):
    '''Create a unique ID for each robot to not give away how many we have. Then give it a name. '''
    id = str(uuid.uuid4())
    id = id[:13]
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
        'REGISTERED': event['REGISTERED']
        })
    except KeyError:
        response = table.put_item(Item={
        'ID': id,
        'NAME': event['NAME']
        })
    return response

def lambda_handler(event, context):
    ''' Standard lambda handler. '''
    result = put_robot(event)
    return {
        'statusCode': 200
    }

if __name__ == "__main__":
    put_robot()