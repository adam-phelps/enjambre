"""
ERM function to create IAM user.  Will need to be converted into a lambda.
Adam Phelps 7/11/2020
"""

import boto3


class EnjRoboAccess:
    """ Holds methods to control giving a new robot access to ERM. """
    def __init__(self):
        pass

    def setup_iam_user(self, robo_id):
        """ Create the IAM user for the created robot. """
        iam = boto3.client('iam')
        create_user_resp = iam.create_user(
            UserName='robot-' + robo_id
        )
        waiter = iam.get_waiter('user_exists')
        waiter.wait(UserName='robot-' + robo_id)
        create_access_key_resp = iam.create_access_key(
            UserName='robot-' + robo_id
        )
        attach_policy_resp = iam.attach_user_policy(
            PolicyArn='arn:aws:iam::aws:policy/AmazonAPIGatewayInvokeFullAccess',
            UserName='robot-' + robo_id)
        return (create_access_key_resp['AccessKey']['AccessKeyId'],
                create_access_key_resp['AccessKey']['SecretAccessKey'])
