import client as cli
import transaction as trans
import block as block

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