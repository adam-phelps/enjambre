import argparse

class EnjCLI:

    def __init__(self):
        pass

    def create_parser(self):
        ''' Create CLI with sensible defaults.'''
        parser = argparse.ArgumentParser(description='Enjambre robot manager')
        parser.add_argument('--add-robot', help='String name of robot.', required=False)
        parser.add_argument('--list-robots', help="Use this option to get existing robots", required=False)
        parser.add_argument('--command', help="Send command to robot.", required=False)
        parser.add_argument('--robot-id', help="Robot ID for session", required=False)
        args = parser.parse_args()
        return vars(args)

if __name__ == "__main__":
    myCli = EnjCLI()
    myvars = myCli.create_parser()
    print(myvars)