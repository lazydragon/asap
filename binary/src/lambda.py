import os
import subprocess
import shlex

def lambda_handler(event, context):
    # config build path to include binary in the package
    os.environ['PATH'] += os.environ['LAMBDA_TASK_ROOT']

    # run binary 
    command = './myecho hello binary'
    args = shlex.split(command)
    print(subprocess.Popen(args))

    return 'done'
