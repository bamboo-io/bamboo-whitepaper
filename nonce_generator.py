# PRNG NONCE GENERATOR
# AUTHOR: Tom Smoker
# DATE: 15/01/2018

"""
The point of this code is to generate nonces for use in the
Proof of Solvency work Bamboo is doing.  It's not enough to
use random.randint(), as it's known to be relatively insecure.
The first implementation simply uses os.urandom.  The second is
taken from here (https://github.com/joestump/python-oauth2/issues/9),
and may be used in the future.
"""

import os
import base64
import random
import sha3

# Generate a basic PRN for use as a nonce
def generate_nonce(length = 8):
    #return os.urandom(length)
    return random.SystemRandom().random()

# Generates a random string of bytes, base64 encoded
def gen_nonce(length):
   if length < 1:
      return ''
   string=base64.b64encode(os.urandom(length),altchars=b'-_')
   b64len=4*floor(length,3)
   if length%3 == 1:
      b64len+=2
   elif length%3 == 2:
      b64len+=3
   return string[0:b64len].decode()

# Hashes the given data using SHA3
def hash_data(data):

    hashed_data = sha3.sha3_224(data.encode('utf-8')).hexdigest()

    return hashed_data

def main():

    indentifier = "tom@getbamboo.io"
    balance     = 10
    nonce       = generate_nonce()

    data = indentifier + str(balance) + str(nonce)

    print(hash_data(data))

if __name__=="__main__":
    main()
