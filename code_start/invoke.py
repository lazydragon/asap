from concurrent import futures
import json

import boto3

import argparse

# parse parameters
parser = argparse.ArgumentParser()
parser.add_argument("-mw", "--max-worker",  help='max number of parallel workers', required=True)
parser.add_argument("-it", "--invoke-time", help='total times to invoke the lambda', required=True)
parser.add_argument("-l", "--lambda-name", help='lambda name', required=True)
args = vars(parser.parse_args())

# concurrent worker number
max_worker = int(args['max_worker']) 
# total times to run the lambda
invoke_time = int(args['invoke_time'])
# lambda name
lambda_name = args['lambda_name']



client = boto3.client('lambda')

def invoke_code_start():
    """
    invoke lambda function and print out the result

    """

    response = client.invoke(
        FunctionName=lambda_name,
        InvocationType='RequestResponse',
    )
    result = json.loads(response['Payload'].read())
    container_id = result[0]
    count = result[1]
    print "%s: This is the %s time this container is used\n" % (container_id, count)


# concurrently call lambda function
with futures.ThreadPoolExecutor(max_workers=max_worker) as pool:
    for i in range(invoke_time):
        pool.submit(invoke_code_start)
