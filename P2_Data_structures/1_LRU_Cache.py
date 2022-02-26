class DLinkedNode(): 
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.head=DLinkedNode()
        self.tail=DLinkedNode()
        self.head.next=self.tail
        self.tail.prev=self.head
        
        self.capacity=capacity
        self.number_elements=0
        self.cache=dict()
    
        
    def add_node(self,node):
        # always add right after the pseudo head, since it's the most recently used entry.
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        
    def remove_node(self,node):
        # remove an existing node from the linked list
        prev=node.prev
        next=node.next
        
        prev.next=next
        next.prev=prev
        
    def pop_tail(self):
        #remove the tail and return the removed entry.
        LRU_node=self.tail.prev
        self.remove_node(LRU_node)
        return LRU_node
        
    def move_to_head(self,node):
        # Move certain node after right behind the pseudo head.
        self.remove_node(node)
        self.add_node(node)


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1
        #else:
        node=self.cache[key]
        self.move_to_head(node)
        return node.value
            

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        node = self.cache.get(key)
        #
        if not node: 
            #print(key,value)
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value
            #print(newNode.key,newNode.value,newNode.prev,newNode.next)

            self.cache[key] = newNode
            
            #print(self.cache[key].next)
            self.add_node(newNode)
            
            #print(self.cache[key].next.key)
            
            self.number_elements += 1

            if self.number_elements > self.capacity:
                # pop the tail
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.number_elements -= 1
        else:
            # update the value.
            node.value = value
            self.move_to_head(node)
            





our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

 #check the entries in the cache
#print('Current entries in the cache')
#for key in our_cache.cache:
 #   print(our_cache.get(key))

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)
#print('Current entries in the cache')
#for key in our_cache.cache:
 #   print(our_cache.get(key))

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

