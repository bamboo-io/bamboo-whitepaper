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
import random
import base64

# Generate a basic PRN for use as a nonce
def generate_nonce(length = 8):
    return os.urandom(length)

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

print(str(generate_nonce(8)))
