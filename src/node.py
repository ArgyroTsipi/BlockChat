from copy import deepcopy
import hashlib
import random
import time
from block import Block, Blockchain
from transaction import Transaction
from wallet import Wallet
import time
from collections import deque
from threading import Lock, Thread
import pickle
import itertools
import time

from copy import deepcopy
from collections import deque
from threading import Lock, Thread

from wallet import Wallet
from block import Block, Blockchain
from transaction import Transaction

MINING_DIFFICULTY = 4


class Node:
    """
    Class for a node of the ring

    id: id of the node
    chain: blockchain of the node
    wallet: wallet of the node
    ring: information about others (id, ip, port, public_key, balance)

    filter_lock: lock in order to provide mutual exclusion while filtering blocks
    chain_lock: lock in order to provide mutual exclusion while updating the chain
    block_lock: lock in order to provide mutual exclusion while updating blocks
    
    unconfirmed_blocks: queue that contains all the blocks waiting to be mined
    current_block: the block that the node currently fills with transactions
    capacity: max number of transactions in each block
    stop_mining: flag to stop mining when a confirmed block arrives
    """
     
    def __init__(self):
        """Initializes a node"""
        
        self.id = None
        self.chain = Blockchain()
        self.wallet = Wallet()
        self.ring = []

        self.filter_lock = Lock()
        self.chain_lock = Lock()
        self.block_lock = Lock()

        self.unconfirmed_blocks = deque()
        self.current_block = None
        self.capacity = None
        self.stop_mining = False
####################################################################################################################################
    def __str__(self):
        """String representation of a node"""
        return str(self.__class__) + ": " + str(self.__dict__)
####################################################################################################################################
    def create_new_block(self):
        """Creates a new block"""
        
        if len(self.chain.blocks) == 0:
            # Genesis block
            self.current_block = Block(0, 1)
        else:
            # Filled out later
            self.current_block = Block(None, None)
        return self.current_block
  ############################################################################################################## 
    def register_node_to_ring(self, id, ip, port, public_key, balance):
        """Registers a new mode in the ring, called only by the bootstrap node"""
        self.ring.append(
            {
                'id': id,
                'ip': ip,
                'port': port,
                'public_key': public_key,
                'balance': balance
            }
        )

####################################################################################################################################        
    # def create_transaction(self, receiver, receiver_address, amount):








####################  mine block  ########################################################################################
    def mine_block(self, block):
        """Implements the proof-of-stake algorithm"""

        selected_validator = self.select_validator()

        block.nonce = 0
        block.index = self.chain.blocks[-1].index + 1
        block.previous_hash = self.chain.blocks[-1].hash

        while not self.stop_mining:
            if self.proof_of_stake(block, selected_validator):
                return True
            block.nonce += 1

        return False

    def proof_of_stake(self, block, validator):
        """Calculates hash and validates if the hash meets the proof-of-stake requirements"""
        
        # Concatenate block data and validator information
        block_data = str(block.index) + str(block.transactions) + str(block.previous_hash) + str(validator)
        
        # Calculate the hash of the concatenated data
        block_hash = self.hash(block_data + str(block.nonce))

        # Check if the hash meets the proof-of-stake requirements
        return block_hash.startswith('0' * MINING_DIFFICULTY)

    def select_validator(self):
        """Selects a validator based on their stake"""
        # Example: Select a validator randomly weighted by their stake
        return random.choice(list(self.stakeholders.keys()))

    def hash(self, data):
        """Computes the SHA-256 hash of the data"""
        return hashlib.sha256(str(data).encode()).hexdigest()
    ####################################################################################################################################