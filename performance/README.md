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
./deploy.sh asap-source Performance

```

