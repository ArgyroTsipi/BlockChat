# Create the blockchain
import datetime as date
import time
from block import Block, Blockchain
from wallet import Wallet
from transaction import Transaction
from node import Node


blockchain = Blockchain()# Add blocks to the blockchain
blockchain.add_block(Block(1, date.datetime.now(), [], None,  ""))
blockchain.add_block(Block(2, date.datetime.now(), [], None, ""))
blockchain.add_block(Block(3, date.datetime.now(), [],None, ""))


# Print the contents of the blockchain
for block in blockchain.chain:
    print("Block #" + str(block.index))
    print("Timestamp: " + str(block.timestamp))
    print("Transactions: " + str(block.transactions))
    print("Hash: " + block.hash)
    print("Previous Hash: " + block.previous_hash)
    print("\n")


