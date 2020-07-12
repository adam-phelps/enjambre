"""
Create our SQS queue for data plane to get tasks
Adam Phelps 7/5/2020
"""

import boto3


class EnjSQS:
    def __init__(self, params):
        self.sqsc = boto3.client('sqs')
        self.create_queue(params)

    def create_queue(self, params):
        response = self.sqsc.create_queue(
            QueueName=params['ID'] + '-' + params['NAME'] + '-sqsq',
        )
        return response['QueueUrl']

