# Enjambre Robo Manager(ERM)
Manage your Robots in one central location using AWS!

## Solution Architecture
![bg](black)
![Solution Visual](imgs/EnjArchitecture.png?raw=true "Enjambre Solution")
![bg](white)

## Configuration Steps

1. git clone repo

`git clone https://github.com/adam-phelps/enjambre.git`

2. Create a local python virtual environment

`python3 -m venv venv`

3. Activate venv

`source venv/bin/activate`

4. Install required packages

`pip install -r requirements.txt`

5. Run setup.sh

`source setup.sh`

6. Issue commands with the CLI

`python src/main.py --robot-name "Adam"`
