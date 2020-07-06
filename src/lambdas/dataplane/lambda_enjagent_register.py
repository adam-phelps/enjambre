# Allows the enj agent to register itself
# Adam Phelps 7-5-2020

import boto3

def post_register(event):
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('Robots')
    try:
        response = table.update_item(
            Key={
                'ID': event['ID'],
                'NAME': event['NAME']
            },
            UpdateExpression="set REGISTERED=:r",
            ExpressionAttributeValues={
                ':r': 'YES'
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
        '''response = ddb.get_item(
        TableName='Robots',
        Key={
            'ID': {
                'S': event['ID']
            },
            'NAME': {
                'S': event['NAME']
            }
        }'''
    except KeyError:
        response = table.put_item(Item={
        'ID': id,
        'EVENT': event['EVENT']
        })
    return response

def lambda_handler(event, context):
    ''' Standard lambda handler. '''
    result = post_register(event)
    return {
        'statusCode': 200
    }

if __name__ == "__main__":
    pass