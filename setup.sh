#!/bin/bash
#Let's form the clouds for this project!

#Make the DB and zip the lambdas then wait for a few seconds
python src/infrastructure/database.py
for x in $(ls src/lambdas | grep -v "zip"); do zip -j src/lambdas/$x.zip src/lambdas/$x; done
sleep 5s

#Create the stack if it doesn't exist yet or update the existing one
aws cloudformation create-stack \
     --stack-name api-stack \
     --template-body file://$(pwd)/src/infrastructure/cfn_api.json \
     --capabilities CAPABILITY_NAMED_IAM

if [ $? -eq 255 ]; then
     aws cloudformation update-stack \
          --stack-name api-stack \
          --template-body file://$(pwd)/src/infrastructure/cfn_api.json \
          --capabilities CAPABILITY_NAMED_IAM
fi

#Wait for the stack to exist before updating the lambdas, the CFN JSON gets messy nesting the Lambdas in there so we send them seperately
sleep 20s
aws lambda update-function-code \
     --function-name robotsGetRobotslambda \
     --zip-file fileb://$(pwd)/src/lambdas/lambda_get_robots.py.zip
