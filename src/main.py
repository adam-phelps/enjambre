import boto3
import json
from network import create_subnet, create_route_table, create_vpc, \
    create_security_group, authorize_security_group_ingress, \
    create_internet_gateway
from security import create_key_pair
from compute import create_instances


def read_config_file():
    """ Load from a JSON to made user customization easier. """
    try:
        with open('lab_config.json') as lab_config_file:
            myconfig = json.load(lab_config_file)
            return myconfig
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    instances = []
    myconfig = read_config_file()
    lab_tag = myconfig['lab_tag']
    ec2_r = boto3.resource('ec2')
    ec2_c = boto3.client('ec2')
    vpc = create_vpc(ec2_r, myconfig['networks']['vpc-lab'], lab_tag)
    kp = create_key_pair(ec2_c, myconfig['keys']['ssh-key'])
    sg = create_security_group(ec2_r, vpc, lab_tag)
    authorize_security_group_ingress(ec2_c, sg, myconfig['ports']['ssh'])
    igw = create_internet_gateway(ec2_r, vpc)
    rt_table = create_route_table(vpc, igw)
    sub = create_subnet(ec2_r, vpc, rt_table,
                        myconfig['networks']['public-sub-lab'], lab_tag)
    for instance in range(0, int(myconfig['instance_info']['amount'])):
        instances.append(create_instances(ec2_r, sg, sub, lab_tag,
                         myconfig['instance_info'],
                         'Public-Linux-' + str(instance)))
        print(instances[instance][0].public_ip_address)
