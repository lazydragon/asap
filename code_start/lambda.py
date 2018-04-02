import time

# global varaiable to record how many times this container is reused
record = 0

def lambda_handler(event, context):
    global record
    # count add 1
    record += 1

    return record
