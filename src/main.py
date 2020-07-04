# Main entry point for the Enjambre robot manager CLI
# Adam Phelps 6/29/2020


from enjrobotmethods import EnjRobotMethods
from enjdatabasechecker import EnjDatabaseChecker
from enjmanager import EnjManager
from enjsecurity import EnjSecurity


if __name__ == "__main__":
    myEnjManager = EnjManager(console="no")
    myEnjSecurity = EnjSecurity()
    myEnjDBChecker = EnjDatabaseChecker()
    myEnjDBChecker.dbcheck_for_status()
    robot_params = myEnjManager.launch_cli()
    aws_auth = myEnjSecurity.get_aws_auth()
    myEnjRobotMethods = EnjRobotMethods(robot_params, aws_auth)
    if robot_params['add_robot']:
        myEnjRobotMethods.post_robot(robot_params['add_robot'])
        print(f"Your robot {robot_params['add_robot']} has been created.")
    if robot_params['list_robots']:
        myEnjRobotMethods.display_robots()
