"""
Contains DDB health check class & methods
Adam Phelps 7/04/2020
"""

import boto3
from botocore import exceptions


class EnjDatabaseChecker:
    """ Offload database health checking from other classes. """

    def __init__(self):
        pass

    def dbcheck_for_duplicates(self):
        pass

    def dbcheck_for_status(self):
        try:
            ddbc = boto3.client('dynamodb')
            response = ddbc.list_tables()
            return response
        except exceptions.ClientError:
            print("EXCEPTION. Have you set up the control-plane?")
            return 1
