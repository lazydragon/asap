from concurrent import futures

import boto3

# concurrent worker number
MAX_WORKERS = 20 
# total times to run the lambda
INVOKE_TIMES = 30

client = boto3.client('lambda')

def invoke_code_start():
    """
    invoke lambda function and print out the result

    """

    response = client.invoke(
        FunctionName='code_start',
        InvocationType='RequestResponse',
    )
    record = response['Payload'].read()
    print "This is the %s time this container is used" % record


# concurrently call lambda function
with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
    for i in range(INVOKE_TIMES):
        pool.submit(invoke_code_start)
