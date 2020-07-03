# Main entry point for the Enjambre robot manager CLI
# Adam Phelps 6/29/2020

import argparse
import requests
import json
from os import environ

def create_parser():
    ''' Create CLI with sensible defaults.'''
    parser = argparse.ArgumentParser(description='Enjambre robot manager')
    parser.add_argument('--robot-name', help='String name of robot.', required=False)
    parser.add_argument('--get-robots', help="Use this option to get existing robots", required=False)
    args = parser.parse_args()
    return vars(args)

class RobotMethods:
    def __init__(self, parameters):
        self.robo_name = parameters['robot_name']
        pass

    def post_robot(self):
        r= requests.post(environ['TARGET_API'], json={"ID":str(self.robo_name)})
        print(r.text)

    def get_robots(self):
        r = requests.get(environ['TARGET_API'])
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
    roboMethods = RobotMethods(robot_params)
    if robot_params['robot_name']:
        roboMethods.post_robot()
        print(f"Your robot {robot_params} has been created.")
    if robot_params['get_robots']:
        roboMethods.display_robots()
