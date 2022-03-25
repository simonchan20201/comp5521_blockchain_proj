import client as cli
import transaction as trans
import block as block
import hashlib

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

def blockchain ():
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
   transactions = []
   TPCoins = []
   last_block_hash = ""


   # Two 2 client
   Dinesh = cli.Client()
   Ramesh = cli.Client()
   # print (Dinesh.identity)


   # First transaction made
   t0 = trans.Transaction(
      Dinesh,
      Ramesh.identity,
      5.0
   )

   block0 = block.Block()

   block0.previous_block_hash = None
   Nonce = None
   block0.verified_transactions.append(t0)

   digest = hash(block0)
   last_block_hash = digest

if __name__ == "__main__":
   main()