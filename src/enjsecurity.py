# Contains a central store for the security funtionality 
# Adam Phelps 7/04/2020

import boto3
import botocore.session
from os import environ


from aws_requests_auth.aws_auth import AWSRequestsAuth

class EnjSecurity:

    def __init__(self):
        pass

    def get_aws_auth(self):
        '''Use pip package to get IAM creds.'''
        session = botocore.session.get_session()
        aws_credentials = session.get_credentials()
        auth = AWSRequestsAuth(aws_access_key=aws_credentials.access_key,
                            aws_secret_access_key=aws_credentials.secret_key,
                            aws_host=environ['TARGET_API_AWS_AUTH'],
                            aws_region=session.get_config_variable('region'),
                            aws_service="execute-api")
        return auth