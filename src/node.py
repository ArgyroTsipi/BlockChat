from block import Blockchain
from transaction import Transaction
from wallet import Wallet

class Node:
    def __init__(self):
        self.blockchain = Blockchain()
        self.wallet = Wallet()

    def create_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        transaction.signature = self.wallet.sign_transaction(transaction)
        return transaction

    def add_transaction_to_pending(self, transaction):
        if self.wallet.verify_transaction(transaction, transaction.signature):
            self.blockchain.add_transaction(transaction)
            return True
        return False

    def mine_pending_transactions(self):
        self.blockchain.mine_pending_transactions(self.wallet.public_key)
