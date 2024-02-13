import hashlib
import uuid

class Transaction:
    def __init__(self, sender, sender_address, receiver, receiver_address, type, amount, message, nonce, signature=None):
        self.sender = sender
        self.receiver = receiver
        self.sender_address = sender_address
        self.receiver_address = receiver_address
        self.type = type
        self.amount = amount
        self.message = message
        self.nonce = nonce
        self.transaction_id = uuid.uuid4()
        self.signature = signature
        """if (id):
            self.id = id
        else:
            self.id = self.hash_transaction()
            """
        """def hash_transaction(self):

        # The hash is a random integer, at most 256 bits long.
        return Crypto.Random.get_random_bytes(256).decode("ISO-8859-1")"""

        # def hash_transaction(self):
        #     hash_string = str(self.sender) + str(self.receiver) + str(self.type) + str(self.amount) + str(self.message)
        #     return hashlib.sha256(hash_string.encode()).hexdigest()



    def __eq__(self, transaction):
        """Overrides the default method and checks the equality of 2 Transaction
        objects by comparing their hashes"""
        return self.id == transaction.id


    def __str__(self):
        """String representation of a Transaction"""
        return str(self.__class__) + ": " + str(self.__dict__)
    

    def convert_to_list(self):
        """List representation of a Transaction"""
        return [self.sender_id, self.receiver_id, self.amount, self.total, self.total - self.amount]

    


#   def verify_transaction(self, transaction, signature):
