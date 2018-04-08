# deploy code start function
## prerequisite
- SAM is installed
- awscli credential is correctly configured
- has access to s3, cloudformation, lambda etc.

## deployment step
```
# create s3 bucket and deploy
./deploy.sh [source s3 bucket name] [stack name]

# example
./deploy.sh asap-source CodeStart

```

# cold start experiment
## environment 
- python 2.7 
- boto3

## how to use invoke.py
```
python inovke.py -mw [max worker] -it [invoke times] -l [lambda function name]
# example
python invoke.py -mw 2 -it 20 -l CodeStart-CodeStart-MSXKXA7GPK7B
```
