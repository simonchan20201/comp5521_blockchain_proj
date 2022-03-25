'''
standard library
'''
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

'''
Install pycryptodome instead of pycrypto
'''
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


transactions = []
TPCoins = []
last_block_hash = ""


class Client:
    def __init__(self):
        random = Crypto.Random.new()
        self._private_key = RSA.generate(1024, random.read)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')


class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        identity = self.sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time})

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')


class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        

def sha256(message):
   return hashlib.sha256(message.encode('ascii')).hexdigest()


def display_transaction(transaction):
   #for transaction in transactions:
   dict = transaction.to_dict()
   print ("sender: " + dict['sender'])
   print ('-----')
   print ("recipient: " + dict['recipient'])
   print ('-----')
   print ("value: " + str(dict['value']))
   print ('-----')
   print ("time: " + str(dict['time']))
   print ('-----')


def blockchain (self):
        print ("Number of blocks in the chain: " + str(len (self)))
        for x in range (len(TPCoins)):
            block_temp = TPCoins[x]
            print ("block # " + str(x))
            for transaction in block_temp.verified_transactions:
                display_transaction (transaction)
                print ('--------------')
            print ('=====================================')


def mine(message, difficulty=1):
   assert difficulty >= 1
   prefix = '1' * difficulty
   for i in range(1000):
      digest = sha256(str(hash(message)) + str(i))
      if digest.startswith(prefix):
         print ("after " + str(i) + " iterations found nonce: "+ digest)
      return digest





def main():

   # Two 2 client
   Dinesh = Client()
   Ramesh = Client()
   # print (Dinesh.identity)

   # First transaction made
   t0 = Transaction(
      Dinesh,
      Ramesh.identity,
      5.0
   )

   block0 = Block()

   block0.previous_block_hash = None
   Nonce = None
   block0.verified_transactions.append(t0)

   digest = hash(block0)
   last_block_hash = digest


if __name__ == "__main__":
   main()