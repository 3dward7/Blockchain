#import the necessary libraries for encrypting the hashes and recording the time of the transactions
import hashlib
import time

# create the class block with all the required attributes
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, nonce):
		    # the index is the position from the genesis block
        self.index = index
        # the hash from the previous block
        self.previous_hash = previous_hash
        # the time the block was created
        self.timestamp = timestamp
	      # the transaction information
        self.data = data
        # the hash of the current block
        self.hash = hash
        # required for the proof of work algorithm
        self.nonce = nonce

# creating the blockchain class
class Blockchain:
    def __init__(self):
		    # an array of all the blocks in the chain
        self.chain = []
        # creating the genesis block to be the beginning of the chain
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(0, "0", int(time.time()), "Genesis Block", self.calculate_hash(0, "0", int(time.time()), "Genesis Block", 0), 0)
        # append the genesis block to the array of blocks
        self.chain.append(genesis_block)
		
		# a function to add blocks to the array which includes all the data required for the block
    def add_block(self, data):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        previous_hash = previous_block.hash
        nonce = self.proof_of_work(index, previous_hash, timestamp, data)
        new_hash = self.calculate_hash(index, previous_hash, timestamp, data, nonce)
        new_block = Block(index, previous_hash, timestamp, data, new_hash, nonce)
        self.chain.append(new_block)
		
		# a function to run a proof of work algorithm
    def proof_of_work(self, index, previous_hash, timestamp, data):
        nonce = 0
        # running a proof of work algorithm constantly to be perpeptually ensuring the chain is accurate
        while True:
            new_hash = self.calculate_hash(index, previous_hash, timestamp, data, nonce)
            if new_hash[:4] == "0000":
                return nonce
            nonce += 1
		# a function to calculate the hash of the current block
    def calculate_hash(self, index, previous_hash, timestamp, data, nonce):
		    # value is the variable that is going to be encrypted so it includes all relevant information
        value = str(index) + str(previous_hash) + str(timestamp) + str(data) + str(nonce)
        # return the encryption of "value"
        return hashlib.sha256(value.encode('utf-8')).hexdigest()
		# print out the blocks to help visualise the chain
    def print_chain(self):
        for block in self.chain:
            print(vars(block))

# adding blocks to the chain with data simplify saying what transaction number it is
if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.add_block("Transaction Data 1")
    blockchain.add_block("Transaction Data 2")
    blockchain.print_chain()
