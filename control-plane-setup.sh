#!/bin/bash
#Let's form the clouds for this project!
#Adam Phelps Enjambre 7/3/20
#Must run as source setup.sh in order for environment var to set in main shell not sub shell

#Make the DB and zip the lambdas because you can only upload zipped lambdas not native .py files
python src/infrastructure/enjdatabase.py
for x in $(ls src/lambdas | grep -v "zip"); do zip -j src/lambdas/$x.zip src/lambdas/$x; done

#Create the stack if it doesn't exist yet or update the existing one, use extra capabilities since we are making IAM roles
#Wait for the stack to exist "CREATE_COMPLETE" before updating the lambdas and environment vars the CFN JSON gets messy nesting the Lambdas in there so we send them seperately
if [ $1 == "create" ]; then
     aws cloudformation create-stack \
          --stack-name enj-controlplane-stack \
          --template-body file://$(pwd)/src/infrastructure/enj-controlplane-stack.json \
          --capabilities CAPABILITY_NAMED_IAM
     aws cloudformation wait stack-create-complete --stack-name enj-controlplane-stack
elif [ $1 == "update" ]; then
     aws cloudformation update-stack \
          --stack-name enj-controlplane-stack \
          --template-body file://$(pwd)/src/infrastructure/enj-controlplane-stack.json \
          --capabilities CAPABILITY_NAMED_IAM
     aws cloudformation wait stack-update-complete --stack-name enj-controlplane-stack
else
     echo "Not CREATING or UPDATING stack. "
fi
#Must run this as source setup.sh or this environment var won't set for main shell

TARGET_API=$(aws cloudformation describe-stacks --stack-name enj-controlplane-stack | grep https | awk '{print $4}')
declare -x TARGET_API 

#In order to use aws-requests-auth PIP package I need a santized version of the URL
TARGET_API_AWS_AUTH=$(echo $TARGET_API | awk -F "/" '{print $3}')
declare -x TARGET_API_AWS_AUTH

aws lambda update-function-code \
     --function-name robotsPostRobotslambda \
     --zip-file fileb://$(pwd)/src/lambdas/lambda_post_robots.py.zip

aws lambda update-function-code \
     --function-name robotsGetRobotslambda \
     --zip-file fileb://$(pwd)/src/lambdas/lambda_get_robots.py.zip

#Test the endpoint, if these fail it means we are secure from public requests:)
echo "These tests sould FAIL and return 'missing auth token'. "
curl $TARGET_API -X POST -d '{"NAME":"PostLambdaTestCURL"}' -H "Content-Type: application/json"
curl $TARGET_API

#Testing CLI
echo "Testing CLI. These tests should PASS."
python src/main.py --add-robot "TestLambdaCLI"