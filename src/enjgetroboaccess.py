import boto3

class EnjRoboAccess:
    def __init__(self):
        pass
    def setup_iam_user(self, id):
        iam = boto3.client('iam')
        create_user_resp = iam.create_user(
            UserName='robot-'+id
        )
        waiter = iam.get_waiter('user_exists')
        waiter.wait(UserName='robot-'+id)
        create_access_key_resp = iam.create_access_key(
            UserName='robot-'+id
        )
        attach_policy_resp = iam.attach_user_policy(
            PolicyArn='arn:aws:iam::aws:policy/AmazonAPIGatewayInvokeFullAccess',
            UserName='robot-'+id
        )
        return create_access_key_resp['AccessKey']['AccessKeyId'],create_access_key_resp['AccessKey']['SecretAccessKey']

