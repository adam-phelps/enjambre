# Enjambre Robo Manager(ERM)
Manage your Robots in one central location using AWS!

## Configuration Steps

1. git clone repo

`git clone https://github.com/adam-phelps/enjambre.git`

2. Create a local python virtual environment

`python3 -m venv venv`

3. Activate venv

`source venv/bin/activate`

4. Install required packages

`pip install -r requirements.txt`

5. CD into src directory and run main.py

`python main.py`

6. Take note of the EC2 instance IP returned

7. Configure the S3 bucket using the s3_bucket_policy.json updating to include the correct VPC dynamically created
8. Create an IAM role for the EC2 instance to have S3 Read Access in the account
9. SSH to EC2 server and run install_server.sh