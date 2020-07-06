# Contains DDB health check class & methods
# Adam Phelps 7/04/2020

import boto3

class EnjDatabaseChecker:
    ''' Offload database health checking from other classes. '''
    def __init__(self):
        pass

    def dbcheck_for_duplicates(self):
        pass

    def dbcheck_for_status(self):
        ddbc = boto3.client('dynamodb')
        response = ddbc.list_tables()
        return response