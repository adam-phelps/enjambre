"""
Contains a central store for the security funtionality
Adam Phelps 7/04/2020
"""

from os import environ
import botocore.session


from aws_requests_auth.aws_auth import AWSRequestsAuth


class EnjSecurity:
    """ Methods to make the ERM more secure. """

    def __init__(self):
        pass

    def get_aws_auth(self):
        """ Use pip package to get IAM creds. """
        try:
            session = botocore.session.get_session()
            aws_credentials = session.get_credentials()
            auth = AWSRequestsAuth(
                aws_access_key=aws_credentials.access_key,
                aws_secret_access_key=aws_credentials.secret_key,
                aws_host=environ['TARGET_API_AWS_AUTH'],
                aws_region=session.get_config_variable('region'),
                aws_service="execute-api")
            return auth
        except Exception:
            return 1
