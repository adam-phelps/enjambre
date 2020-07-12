"""
Main entry point for the Enjambre robot manager CLI
Adam Phelps 6/29/2020
"""


import sys
from enjrobotmethods import EnjRobotMethods
from enjgetroboaccess import EnjRoboAccess
from enjdatabasechecker import EnjDatabaseChecker
from enjmanager import EnjManager
from enjsecurity import EnjSecurity


if __name__ == "__main__":
    myEnjManager = EnjManager(console="no")
    myEnjRoboAccess = EnjRoboAccess()
    myEnjSecurity = EnjSecurity()
    myEnjDBChecker = EnjDatabaseChecker()
    if myEnjDBChecker.dbcheck_for_status() == 1:
        print("The database has not been detected. Exiting. Please initialize databases.")
        sys.exit()
    robot_params = myEnjManager.launch_cli()
    aws_auth = myEnjSecurity.get_aws_auth()
    myEnjRobotMethods = EnjRobotMethods(robot_params, aws_auth)
    session_robots, robots_count = myEnjRobotMethods.get_robots()
    if robot_params['add_robot']:
        robo_id = myEnjRobotMethods.post_robot(robot_params['add_robot'])
        myAccessK, mySecretK = myEnjRoboAccess.setup_iam_user(
            robot_params['add_robot'])
        print(f"Robot with ID {robo_id} created.")
        print(
            f"On your robot configure the \n Access Key: {myAccessK} \n Secret Key: {mySecretK}")
        print(f"Your robot {robot_params['add_robot']} has been created.")
    if robot_params['list_robots']:
        myEnjRobotMethods.display_robots()
    if robot_params['command'] and robot_params['robot_id']:
        print("Let's command!")
        for robot in session_robots:
            if robot[0] == robot_params['robot_id']:
                robo_sqsq = robot[6]
        send_cmd_result = myEnjRobotMethods.send_command(
            robot_params['command'], robo_sqsq)
        print(send_cmd_result)
