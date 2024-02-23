import datetime as date
from hashlib import sha256
import hashlib
import json
# from Crypto.Hash import SHA256
import time
from Exceptions.InvalidBlockException import InvalidBlockException
from Exceptions.InvalidCapacityException import InvalidCapacityException
import config
from transaction import Transaction
# import blockchain

# TUTORIALS

# Blockchain tutorial in python
#  https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

# GitHub tutorial for blockchain using proof-of-stake
#  https://github.com/hvuhsg/yoyocoin/tree/main/src/blockchain

# PoS info
#  https://www.blockchain-council.org/blockchain/exactly-proof-stake-implemented/

# JS tutorial using proof of stake
#  https://medium.com/coinmonks/implementing-proof-of-stake-e26fa5fb8716
#  https://medium.com/coinmonks/implementing-proof-of-stake-part-2-748156d5c85e
#  https://medium.com/coinmonks/implementing-proof-of-stake-part-3-c68b953a50be
#  https://medium.com/coinmonks/implementing-proof-of-stake-part-4-2107bb07dfed
#  https://medium.com/coinmonks/implementing-proof-of-stake-part-5-7e3d5b6cdc31
#  https://medium.com/coinmonks/implementing-proof-of-stake-part-6-c811ce78ab0f

class Block:
    """ Class for a Block of the blockchain

    index: index of the Block
    timestamp: timestamp of the Block's creation
    transactions: list of the Block's transactions
    validator: node object that creates block
    previous_hash: hash of the previous Block
    hash: hash of the Block """

    def __init__(self, index, timestamp, transactions, validator, previous_hash):
        """ Initializes a block """

        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.validator = validator
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """ Calculates block's hash using sha """
        hash_string = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.validator) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def __str__(self):
        """ String representation of a Block.
        toString() function that will 
        print the details of the block in a readable format."""
        return str(self.__class__) + ": " + str(self.__dict__)

    def __eq__(self, block):
        """ Overrides the default method and checks the equality of 2 Block
        objects by comparing their hashes """
        return self.hash == block.hash

    def add_transaction(self, transaction, capacity):
        """ Adds a new transaction to the block """
        self.transactions.append(transaction)
        """ Check if the block has reached its max capacity """
        if len(self.transactions) < capacity:
            self.transactions.append(transaction)
        else: 
            raise InvalidCapacityException("Reached maximum capacity.")
            
        return True

    def is_valid(self):
            """ Checks if block is valid """
            return True


# class Blockchain:
#     """Class for a blockchain

#     blocks: list of validated blocks in the chain"""

#     def __init__(self):
#         """Initializes a Blockchain"""
        
#         self.blocks = []

class Blockchain:
    """ Class of the Blockchain """

    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = [] ####

    def __str__(self):
        """ String representation of a Blockchain """
        return str(self.__class__) + ": " + str(self.__dict__)

    def create_genesis_block(self): 
        """ Create the first block """
        return Block(0, date.datetime.now(), [], None, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        """ Add a new block to the chain """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        # we need to validate block before adding it to chain
        if new_block.is_valid():
            self.chain.append(new_block)
        else: raise InvalidBlockException("The new block is not valid.")

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
    
##############################
    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    # def mine_pending_transactions(self, miner_address):
    #     block = Block(len(self.chain), date.datetime.now(), self.pending_transactions, self.get_latest_block().hash)
    #     block.mine_block(self.difficulty)
    #     print("Block mined successfully!")
    #     self.chain.append(block)
    #     self.pending_transactions = [Transaction(None, miner_address, 1)]