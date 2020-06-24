def create_vpc(ec2_r, cidr_block, lab_tag):
    """ Create VPC using EC2 resource. """
    vpc = ec2_r.create_vpc(CidrBlock=cidr_block)
    vpc.wait_until_available()
    vpc.create_tags(Tags=[{
        "Key": "Name",
        "Value": lab_tag
    }])
    return vpc


def create_internet_gateway(ec2_r, vpc):
    """ Create IGW and attach to allow SSH in. """
    igw = ec2_r.create_internet_gateway()
    vpc.attach_internet_gateway(InternetGatewayId=igw.id)
    return igw


def create_route_table(vpc, igw):
    """ Set the default route out the IGW. """
    rt_table = vpc.create_route_table(VpcId=vpc.id)
    rt_table.create_route(
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=igw.id
    )
    return rt_table


def create_subnet(ec2_c, vpc, rt_table, networks, lab_tag):
    """ Must have a least one subnet to provision EC2 instances. """
    subnet = ec2_c.create_subnet(CidrBlock=networks, VpcId=vpc.id)
    rt_table.associate_with_subnet(SubnetId=subnet.id)
    return subnet


def create_security_group(ec2_r, vpc, lab_tag):
    """ Must have a security group to apply SSH allow policies. """
    sg = ec2_r.create_security_group(
        GroupName=lab_tag,
        Description=lab_tag,
        VpcId=vpc.id)
    return sg


def authorize_security_group_ingress(ec2_c, sg_id, port):
    """ Alows us to open a TCP port. """
    try:
        ec2_c.authorize_security_group_ingress(
            GroupId=sg_id.id,
            IpPermissions=[{
                'IpProtocol': 'tcp',
                'FromPort': int(port),
                'ToPort': int(port),
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }]
            )
    except Exception as e:
        print(e)
    return 0
