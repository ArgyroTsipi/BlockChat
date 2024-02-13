from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15  
from Crypto.Hash import SHA256
from Crypto.Signature import pss

class Wallet:
    def __init__(self):
        # Generate a private key of key length of 2048 bits
        key = RSA.generate(2048)
        self.private_key = key.exportKey().decode("ISO-8859-1")

        # Generate the public key from the above private key
        self.public_key = key.publickey().exportKey().decode("ISO-8859-1")

        self.transactions = []

    def __str__(self):
        """String representation of a Wallet"""
        return str(self.__class__) + ": " + str(self.__dict__)
    
    def sign_transaction(self, transaction):
        h = SHA256.new(str(transaction).encode())
        signature = pkcs1_15.new(self.private_key).sign(h)
        return signature
    
    # def sign_transaction(self, private_key):
    #     """Signs the Transaction using a private key"""

    #     temp = self.id.encode("ISO-8859-1")
    #     key = RSA.importKey(private_key.encode("ISO-8859-1"))
    #     hashed = SHA256.new(temp)
    #     signer = pss.new(key)
    #     self.signature = signer.sign(hashed).decode("ISO-8859-1")