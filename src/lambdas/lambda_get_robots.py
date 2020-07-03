import boto3
import json

def get_robots() -> list:
    ddbr = boto3.resource('dynamodb')
    ddbc = boto3.client('dynamodb')
    table = ddbr.Table('Robots')
    """response = ddbc.get_item(
        TableName='Robots',
        Key={
            'ID': {
                'S': '4165ff5f-0cc9'
            },
            'NAME': {
                'S': 'Yo44165ff5f-0cc9'
            }
        }
    )"""
    response = ddbc.scan(
        TableName='Robots'
    )
    print(response['Items'])
    """
    robots = []
    robot_count = 0
    for robot in response['Items']:
        robots.append((robot['ID']['S'],robot['NAME']['S']))
        robot_count +=1
    print(json.dumps(robots))
    """
    return response

def lambda_handler(event, context):
    result = get_robots()
    return {
        'statusCode': 200,
        'robots': result
    }

if __name__ == "__main__":
    robots = get_robots()
    '''print("ID | NAME")
    for robot in robots[0]:
        print(robot)
    print(f"Total Robots {robots[1]}")'''
