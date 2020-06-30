import boto3
import uuid

def put_robot():
    id = str(uuid.uuid4())
    id = id[:13]
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('Robots2')
    response = table.put_item(Item={
        'ID': id,
        'NAME': 'Robot-'+id
        })
    return response

def lambda_handler(event, context):
    result = put_robot()
    return {
        'statusCode': 200
    }

if __name__ == "__main__":
    put_robot()