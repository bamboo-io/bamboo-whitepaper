# NODE CREATOR
# AUTHOR: Tom Smoker
# DATE: 15/01/2018

"""
The point of this code is to generate nodes for use in the
Proof of Solvency work Bamboo is doing.  It creates a nonce and hashes
it with an identifier and the user balance.
It's not enough to use random.randint(), as it's known to be relatively insecure.
The first implementation uses SystemRandom, which uses os.random.
The second is taken from here:
(https://github.com/joestump/python-oauth2/issues/9),
and may be used in the future.
"""

import os
import base64
import random

import sys
import hashlib
if sys.version_info < (3, 6):
    import sha3

# Generate a basic PRN for use as a nonce
def generate_nonce(length = 8):
    #return os.urandom(length)
    return random.SystemRandom().random()

# Generates a random string of bytes, base64 encoded
# Took it from here: https://github.com/joestump/python-oauth2/issues/9
# Note using it currently, might in the future but SystemRandom is good for now
def generate_nonce_base64(length):

   if length < 1:
      return ''

   string = base64.b64encode(os.urandom(length), altchars = b'-_')
   b64len = 4 * floor(length,3)

   if length % 3 == 1:
      b64len += 2
   elif length % 3 == 2:
      b64len += 3
   return string[0:b64len].decode()

# Hashes the given data using SHA3
def hash_data(identifier, balance, nonce):

    data = b"".join([
             identifier.encode('utf-8'),
             b'\00',
             str(balance).encode('utf-8'),
             b'\00',
             str(nonce).encode('utf-8')
           ])

    # Encode the data in bytes before hashing with SHA512
    hashed_data = hashlib.sha3_512(data).hexdigest()

    return hashed_data

def main():

    # Nonces for use in the whitepaper
    test_users = [
        "tom@bambooteam.com",
        "peter@bambooteam.com",
        "alex@bambooteam.com",
        "simone@bambooteam.com"]

    test_balances = [
        6.853,
        27.431,
        545.972,
        0.563
    ]

    for user in test_users:
        print(generate_nonce())

    toms_nonce    = 0.22920468032703945
    peters_nonce  = 0.682051988865186
    alexs_nonce   = 0.20229544353438245
    simones_nonce = 0.31631206564466663

    toms_hash = hash_data(test_users[0], test_balances[0], toms_nonce)
    peters_hash = hash_data(test_users[1], test_balances[1], peters_nonce)
    alexs_hash = hash_data(test_users[2], test_balances[2], alexs_nonce)
    simones_hash = hash_data(test_users[3], test_balances[3], simones_nonce)

    print(toms_hash)
    print(peters_hash)
    print(alexs_hash)
    print(simones_hash)

    ################################################

    # Working example
    identifier  = "tom@bambooteam.com"
    balance     = 10
    nonce       = generate_nonce()

    hashed_data = hash_data(identifier, balance, nonce)

    print("Node")
    print("Balance:",balance)
    print("Hash:",hashed_data)

if __name__=="__main__":
    main()
