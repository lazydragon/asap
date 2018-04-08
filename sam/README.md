# sam installation
prerequisite: 
- docker installed

```
#https://github.com/awslabs/aws-sam-local/issues/66
npm config set unsafe-perm=true

# install https://docs.aws.amazon.com/lambda/latest/dg/sam-cli-requirements.html
npm install -g aws-sam-local

# check sam is installed
sam --version

```

# sam local commands

```
# write a template.yaml config of your serverless application
# please check here for property details: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html
# sync invoke a lambda called HelloWorld 
echo '{}' | sam local invoke "HelloWorld"

```

# sam deployment commands
```
# package and upload source code to s3
sam package --template-file template.yaml --s3-bucket <BUCKET NAME> --output-template-file output.yaml

# deploy the serverless application
sam deploy --template-file output.yaml --stack-name <YOUR STACK NAME> --capabilities CAPABILITY_IAM

# describe output of the function
aws cloudformation describe-stacks --stack-name <YOUR STACK NAME>

# test invoke of lambda
aws lambda invoke --function-name <LAMBDA FUNCTION NAME> <OUTPUT FILE NAME>

# delete stack
aws cloudformation delete-stack --stack-name <YOUR STACK NAME>
```


