# Enjambre Robo Manager (ERM)
Manage your Robots in one central location using AWS!

## Solution Architecture
![Solution Visual](imgs/EnjambreArchitecture.png?raw=true "Enjambre Solution")

## Getting Started 

### Add a new robot

`python src/main.py --robot-name "Adam"`

### Get a list of existing robots

`python src/main.py --get-robots all`

## Installation & Configuration 

Configure AWS environment, will need perms to create DDB, create/run Cloudformation stacks, create/run Lambda functions, create/use API gateway.

`aws configure`

Git clone repo

`git clone https://github.com/adam-phelps/enjambre.git`

Create a local python virtual environment

`python3 -m venv venv`

Activate venv

`source venv/bin/activate`

Install required packages

`pip install -r requirements.txt`

Run setup.sh

`source setup.sh create`

ERM is now ready!


