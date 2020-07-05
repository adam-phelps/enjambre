# Contains all the api manager api calls.
# Adam Phelps 7/04/2020


import requests
from os import environ


class EnjRobotMethods:
    def __init__(self, parameters, aws_auth):
        if parameters['add_robot']:
            self.robo_name = parameters['add_robot']
        self.aws_auth = aws_auth

    def post_robot(self, name):
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