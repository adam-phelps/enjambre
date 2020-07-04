import boto3
import json

def get_robots() -> list:
    ''' Return all robots in the table. '''
    ddbc = boto3.client('dynamodb')
    response = ddbc.scan(
        TableName='Robots'
    )
    return response

def lambda_handler(event, context):
    ''' Standard lambda handler. '''
    result = get_robots()
    return {
        'statusCode': 200,
        'robots': result
    }

if __name__ == "__main__":
    robots = get_robots()

