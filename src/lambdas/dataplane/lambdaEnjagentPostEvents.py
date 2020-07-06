# Allow enjagent to update the events table
# Adam Phelps 7-5-2020

import boto3

def update_event(event):
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('Events')
    try:
        response = table.put_item(Item={
        'ID': event['ID'],
        'EVENT': event['EVENT'],
        'TIME': event['TIME'],
        'DESC': event['DESC']
        })
    except KeyError:
        response = table.put_item(Item={
        'ID': id,
        'EVENT': event['EVENT']
        })
    return response

def lambda_handler(event, context):
    ''' Standard lambda handler. '''
    result = update_event(event)
    return {
        'statusCode': 200
    }

if __name__ == "__main__":
    pass