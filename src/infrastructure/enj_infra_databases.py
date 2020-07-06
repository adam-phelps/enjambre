#Create our DynamoDB tables for control and data plane.
#Adam Phelps 7/5/2020

import json
import boto3


def create_table(config_file):
    """ Seperate the config from logic in JSON file and create our table. """
    try:
        with open(config_file) as ddb_config:
            my_ddb_config = json.load(ddb_config)
    except FileNotFoundError:
        print(f"Could not load '{config_file}' File not found.")

    ddb = boto3.resource('dynamodb')
    try:
        ddb.create_table(
        TableName=my_ddb_config['TableName'],
        KeySchema=[
            {
                'AttributeName': my_ddb_config['Attributes'][0]['AttributeName'],
                'KeyType': my_ddb_config['Attributes'][0]['KeyType']
            },
            {
                'AttributeName': my_ddb_config['Attributes'][1]['AttributeName'],
                'KeyType': my_ddb_config['Attributes'][1]['KeyType']
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': my_ddb_config['Attributes'][0]['AttributeName'],
                'AttributeType': my_ddb_config['Attributes'][0]['AttributeType']
            },
            {
                'AttributeName': my_ddb_config['Attributes'][1]['AttributeName'],
                'AttributeType': my_ddb_config['Attributes'][0]['AttributeType']
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 3,
            'WriteCapacityUnits': 3
        }
        )
        print("Creating table.")
        return True
    except ddb.meta.client.exceptions.ResourceInUseException:
        print("The table already exists.")
        return False


if __name__ == "__main__":
    create_table('src/infrastructure/ddb_robots_table.json')
    create_table('src/infrastructure/ddb_events_table.json')
