# Main entry point for the Enjambre robot manager CLI
# Adam Phelps 6/29/2020

import argparse
import requests
from os import environ

def create_parser():
    ''' Create CLI with sensible defaults.'''
    parser = argparse.ArgumentParser(description='Enjambre robot manager')
    parser.add_argument('--robot-name', help='String name of robot.', required=True)
    args = parser.parse_args()
    return vars(args)

class RobotMethods:
    def __init__(self, parameters):
        robo_name = parameters
        pass

    def post_robot(self):
        r= requests.post(environ['TARGET_API'])
        print(r.text)

if __name__ == "__main__":
    robot_params = create_parser()
    roboMethods = RobotMethods(robot_params)
    roboMethods.post_robot()
    print(f"Your robot name: {robot_params}")