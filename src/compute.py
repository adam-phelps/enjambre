def create_instances(ec2_r,sg_id,sub_id,lab_tag,instance_info,instance_name):
    instance = ec2_r.create_instances(
        TagSpecifications=[{'ResourceType':'instance',
            'Tags': [{
            'Key' : 'Name',
            'Value' : instance_name
            }]
        }],
        ImageId=instance_info['ImageId'],
        InstanceType=instance_info['InstanceType'],
        MinCount=1,
        MaxCount=1,
        KeyName=instance_info['KeyName'],
        UserData= """
        #!/bin/bash
        yum install ansible
        """,
        NetworkInterfaces=[{
        "Groups": [sg_id.id],
        "SubnetId": sub_id.id,
        "DeviceIndex": 0,
        "AssociatePublicIpAddress": True
        }]
    )
    instance[0].wait_until_running()
    instance[0].reload()
    return instance
