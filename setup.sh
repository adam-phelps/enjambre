#!/bin/bash
#Let's form the clouds for this project!
#Adam Phelps Enjambre 7/3/20
#Must run as source setup.sh in order for environment var to set in main shell not sub shell

#Make the DB and zip the lambdas because you can only upload zipped lambdas not native .py files
python src/infrastructure/database.py
for x in $(ls src/lambdas | grep -v "zip"); do zip -j src/lambdas/$x.zip src/lambdas/$x; done

#Create the stack if it doesn't exist yet or update the existing one, use extra capabilities since we are making IAM roles
#Wait for the stack to exist "CREATE_COMPLETE" before updating the lambdas and environment vars the CFN JSON gets messy nesting the Lambdas in there so we send them seperately
set -x
if [ $1 == "create" ]; then
     aws cloudformation create-stack \
          --stack-name api-stack \
          --template-body file://$(pwd)/src/infrastructure/cfn_api.json \
          --capabilities CAPABILITY_NAMED_IAM
     aws cloudformation wait stack-create-complete --stack-name api-stack
elif [ $1 == "update" ]; then
     aws cloudformation update-stack \
          --stack-name api-stack \
          --template-body file://$(pwd)/src/infrastructure/cfn_api.json \
          --capabilities CAPABILITY_NAMED_IAM
     aws cloudformation wait stack-update-complete --stack-name api-stack
else
     echo "Not CREATING or UPDATING stack. "
fi
set +x
#Must run this as source setup.sh or this environment var won't set for main shell

TARGET_API=$(aws cloudformation describe-stacks | grep https | awk '{print $4}')
declare -x TARGET_API 

aws lambda update-function-code \
     --function-name robotsPostRobotslambda \
     --zip-file fileb://$(pwd)/src/lambdas/lambda_post_robots.py.zip

aws lambda update-function-code \
     --function-name robotsGetRobotslambda \
     --zip-file fileb://$(pwd)/src/lambdas/lambda_get_robots.py.zip

#Test the endpoint
echo "Testing if we can hit the endpoint..."
curl $TARGET_API -X POST -d '{"ID":"PostLambdaTestCURL"}' -H "Content-Type: application/json"
curl $TARGET_API

if [ $? -eq 0 ]; then
     echo "ENDPOINT READY"
else
     echo "ERROR Hitting endpoint.  Check if stack is in 'CREATE_COMPLETE'!"
fi

#Testing CLI
echo "Testing CLI."
python src/main.py --robot-name "PostLambdaTestCLI"