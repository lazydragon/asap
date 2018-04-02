import random
import string
import time

# global varaiable to count how many times this container is reused
count = 0

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    generate random id

    """
    return ''.join(random.choice(chars) for _ in range(size))

# random container id
container_id = id_generator()

def lambda_handler(event, context):
    global count, container_id
    # count add 1
    count += 1

    return (container_id, count)
