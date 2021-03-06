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
        r = r.json()
        return r['robo_id']

    def get_robots(self):
        r = requests.get(environ['TARGET_API'],auth=self.aws_auth)
        responsejson = r.json()
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
            robot_count +=1
        return robots, robot_count

    def send_command(self, command, sqsq):
        r = requests.post(environ['TARGET_API']+'/command',auth=self.aws_auth,
        json={
            "SQSQ": sqsq,
            "commandname": command,
            "commandbody": command
            }
        )
        return r.text
        
    def display_robots(self):
        robots, robot_count = self.get_robots()
        for robot in robots:
            print(robot)
        print(f"Total Robots {robot_count}")