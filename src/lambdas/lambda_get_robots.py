import boto3

def get_robots():
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('Robots')
    response = table.put_item(Item={
        'ID': id,
        'Name': 'Robot-'+id
        })
    return response

def lambda_handler(event, context):
    result = get_robots()
    return {
        'statusCode': 200
    }

if __name__ == "__main__":
    get_robots()