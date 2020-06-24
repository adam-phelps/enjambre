import os
import stat


def create_key_pair(ec2_c, my_key):
    """ Change CHMOD of key so its useable after we generate it. """
    try:
        response = ec2_c.create_key_pair(KeyName=my_key)
        with open(my_key + ".pem", "w") as f:
            f.write(response['KeyMaterial'])
        os.chmod(my_key + ".pem", stat.S_IRWXU)
        return response
    except Exception:
        print("Key {} already exists.".format(my_key))
        return 0
