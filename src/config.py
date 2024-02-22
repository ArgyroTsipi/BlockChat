# All nodes in the network know the ip address
# and the port of the bootstrap node.
BOOTSTRAP_IP = "127.0.0.1"
BOOTSTRAP_PORT = "9876"

block_capacity = 5 #this is by default
total_nodes = 0 #initialization

def set_block_capacity(value):
    """Updates the global variable block_capacity with the given value."""
    global block_capacity
    block_capacity = value

def set_total_nodes(value):
    """Updates the global variable total_nodes with the given value."""
    global total_nodes
    total_nodes = value