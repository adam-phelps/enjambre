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

1. git clone repo

`git clone https://github.com/adam-phelps/enjambre.git`

2. Create a local python virtual environment

`python3 -m venv venv`

3. Activate venv

`source venv/bin/activate`

4. Install required packages

`pip install -r requirements.txt`

5. Run setup.sh

`source setup.sh create`

ERM is now ready!


