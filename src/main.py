# Main entry point for the Enjambre robot manager CLI
# Adam Phelps 6/29/2020
import botocore.session
import argparse
import requests
import json
from os import environ
from aws_requests_auth.aws_auth import AWSRequestsAuth

def create_parser():
    ''' Create CLI with sensible defaults.'''
    parser = argparse.ArgumentParser(description='Enjambre robot manager')
    parser.add_argument('--robot-name', help='String name of robot.', required=False)
    parser.add_argument('--get-robots', help="Use this option to get existing robots", required=False)
    args = parser.parse_args()
    return vars(args)

def get_aws_auth():
    '''Use pip package to get IAM creds.'''
    session = botocore.session.get_session()
    aws_credentials = session.get_credentials()
    auth = AWSRequestsAuth(aws_access_key=aws_credentials.access_key,
                           aws_secret_access_key=aws_credentials.secret_key,
                           aws_host=environ['TARGET_API_AWS_AUTH'],
                           aws_region=session.get_config_variable('region'),
                           aws_service="execute-api")
    return auth

class RobotMethods:
    def __init__(self, parameters, aws_auth):
        self.robo_name = parameters['robot_name']
        self.aws_auth = aws_auth

    def post_robot(self):
        r= requests.post(environ['TARGET_API'], 
        json=
        {
            "NAME": str(self.robo_name),
            'MODEL': "software",
            'VIDEO': "no",
            'CONNECTION': "good",
            'LOCATION': "USA",
            'REGISTERED': "NO"
        },
        auth=self.aws_auth)
        print(r.text)

    def get_robots(self):
        r = requests.get(environ['TARGET_API'],auth=self.aws_auth)
        print(r.text)
        responsejson = r.json()
        robots = []
        robot_count = 0
        for robot in responsejson['robots']['Items']:
            robots.append((robot['ID']['S'],robot['NAME']['S']))
            robot_count +=1
        return robots, robot_count
    def display_robots(self):
        robots, robot_count = self.get_robots()
        for robot in robots:
            print(robot)
        print(f"Total Robots {robot_count}")

if __name__ == "__main__":
    robot_params = create_parser()
    print(robot_params)
    aws_auth = get_aws_auth()
    roboMethods = RobotMethods(robot_params, aws_auth)
    if robot_params['robot_name']:
        roboMethods.post_robot()
        print(f"Your robot {robot_params['robot_name']} has been created.")
    if robot_params['get_robots']:
        roboMethods.display_robots()
