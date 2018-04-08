import hashlib
from datetime import datetime
import string
import random

N=102400
 
def lambda_handler(event, context):
    
    m = hashlib.sha512()
    # Generate a random long string
    rstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
   
    t1 = datetime.now()
    print("Start time: " + str(t1))
 
    # repeatedly compute the digest
    for i in range(10000):
        m.update(rstr.encode())
        m.digest()
 
    t2 = datetime.now()
    print("End time: " + str(t2))
    print("Difference: " + str(t2 - t1))
