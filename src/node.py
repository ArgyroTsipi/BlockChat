from copy import deepcopy
import time
from block import Block, Blockchain
from transaction import Transaction
from wallet import Wallet
import pickle
import itertools
import time
from collections import deque
from threading import Lock, Thread
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

    def __str__(self):
        """String representation of a node"""
        return str(self.__class__) + ": " + str(self.__dict__)

    def create_new_block(self):
        """Creates a new block"""
        
        if len(self.chain.blocks) == 0:
            # Genesis block
            self.current_block = Block(0, 1)
        else:
            # Filled out later
            self.current_block = Block(None, None)
        return self.current_block
    
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

        
    # def create_transaction(self, receiver, receiver_address, amount):
