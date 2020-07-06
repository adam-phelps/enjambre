# Main entry point for the Enjambre robot manager CLI
# Adam Phelps 6/29/2020


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
    myEnjDBChecker.dbcheck_for_status()
    robot_params = myEnjManager.launch_cli()
    aws_auth = myEnjSecurity.get_aws_auth()
    myEnjRobotMethods = EnjRobotMethods(robot_params, aws_auth)
    localrobots = myEnjRobotMethods.get_robots()
    if robot_params['add_robot']:
        myEnjRobotMethods.post_robot(robot_params['add_robot'])
        myAccessK,mySecretK = myEnjRoboAccess.setup_iam_user(robot_params['add_robot'])
        print(f"On your robot configure the \n Access Key: {myAccessK} \n Secret Key: {mySecretK}")
        print(f"Your robot {robot_params['add_robot']} has been created.")
    if robot_params['list_robots']:
        myEnjRobotMethods.display_robots()