# Main entry point for the Enjambre robot manager CLI
# Adam Phelps 6/29/2020

import argparse

def create_parser():
    ''' Create CLI with sensible defaults.'''
    parser = argparse.ArgumentParser(description='Enjambre robot manager')
    parser.add_argument('--robot-name', help='String name of robot.', required=True)
    args = parser.parse_args()
    return vars(args)


def endpoint_request(robot_name) -> bool:
    ''' Reach out to endpoint to enter in robot.'''
    return True

if __name__ == "__main__":
    print(f"Your robot name: {create_parser()}")