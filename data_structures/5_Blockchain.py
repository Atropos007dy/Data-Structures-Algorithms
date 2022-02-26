import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None
      
    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()
      
    def __repr__(self):
        return str(self.timestamp) + str(" | ") + \
        str(self.data) + str(" | ") + \
        str(self.previous_hash) + str(" | ") + str(self.hash)
        

# use Block as the node in the linked list     
class BlockChain(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        if data is None or data =="":
            return
        if self.head is None:
            self.head = Block(datetime.datetime.now(), data, 0)
            self.tail = self.head
        else:
            self.tail.next = Block(datetime.datetime.now(), data, self.tail.hash)
            self.tail = self.tail.next
        return
    def covert2list(self):
        res=[]
        p=self.head
        while p:
            res.append(p)
            p=p.next
        return res
        

        
#Test 1:
chain1 = BlockChain()
data1 = ""
data2 = "ABC"
chain1.append(data1)
chain1.append(data2)
chain1_list=chain1.covert2list()
print("Test 1:\nBlockchain: {:}, Number of blocks: {:}".format(chain1_list,len(chain1_list))) # prints block chain
#Test 2:
chain2 = BlockChain()
data1 = "123"
data2 = "456"
chain2.append(data1)
chain2.append(data2)
chain2_list=chain2.covert2list()
print("Test 2:\n Blockchain: {:}, Number of blocks: {:}".format(chain2_list,len(chain2_list))) # prints block chain
#Test 3:
chain3 = BlockChain()
data1 = None
data2 = None
chain3.append(data1)
chain3.append(data2)
chain3_list=chain3.covert2list()
print("Test 3:\n Blockchain: {:}, Number of blocks: {:}".format(chain3_list,len(chain3_list))) # prints block chain





