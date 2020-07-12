"""
Contains all the api manager api calls.
Adam Phelps 7/04/2020
"""

from os import environ
import requests


class EnjRobotMethods:
    """ Contains web API methods for ERM. """
    def __init__(self, parameters, aws_auth):
        if parameters['add_robot']:
            self.robo_name = parameters['add_robot']
        self.aws_auth = aws_auth

    def post_robot(self, robo_name):
        """ Post initial robot info. """
        response = requests.post(environ['TARGET_API'],
                          json={
            "NAME": str(robo_name),
            'MODEL': "software",
            'VIDEO': "no",
            'CONNECTION': "good",
            'LOCATION': "USA",
            'REGISTERED': "NO"
        },
            auth=self.aws_auth)
        response = response.json()
        return response['robo_id']

    def get_robots(self):
        """ Get a list of all robots. """
        response = requests.get(environ['TARGET_API'], auth=self.aws_auth)
        responsejson = response.json()
        robots = []
        robot_count = 0
        for robot in responsejson['robots']['Items']:
            robots.append(
                [robot['ID']['S'],
                 robot['NAME']['S'],
                 robot['CONNECTION']['S'],
                 robot['LOCATION']['S'],
                 robot['MODEL']['S'],
                 robot['REGISTERED']['S'],
                 robot['SQSQ']['S'],
                 robot['VIDEO']['S']
                 ])
            robot_count += 1
        return robots, robot_count

    def send_command(self, command, sqsq):
        """ Send a command to an SQS queue. """
        response = requests.post(
            environ['TARGET_API'] +
            '/command',
            auth=self.aws_auth,
            json={
                "SQSQ": sqsq,
                "commandname": command,
                "commandbody": command})
        return response.text

    def display_robots(self):
        """ Human friendly format show all robots. """
        robots, robot_count = self.get_robots()
        for robot in robots:
            print(robot)
        print(f"Total Robots {robot_count}")
