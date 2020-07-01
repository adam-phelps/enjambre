#!/bin/bash
#Let's form the clouds for this project!


for x in $(ls src/lambdas | grep -v "zip"); do zip -j src/lambdas/$x.zip src/lambdas/$x; done

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
sleep 10s
aws lambda update-function-code \
     --function-name robotsGetRobotslambda \
     --zip-file fileb://$(pwd)/src/lambdas/lambda_get_robots.py.zip
