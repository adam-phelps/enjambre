"""
Lambda to return all robots in the DDB table.
Adam Phelps 7/11/20
"""

import boto3


def get_robots(event) -> list:
    ''' Return all robots in the table. '''
    ddbc = boto3.client('dynamodb')
    response = ddbc.scan(
        TableName='Robots'
    )
    return response


def lambda_handler(event, context):
    ''' Standard lambda handler. '''
    result = get_robots(event)
    return {
        'statusCode': 200,
        'robots': result
    }


if __name__ == "__main__":
    robots = get_robots()
