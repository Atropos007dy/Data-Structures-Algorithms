class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    p1=llist_1.head #p1 points to llist_1
    p2=llist_2.head # p2 points to llist_2    
    seen=set()  # use a set to record the values we have seen, without duplicates
    while p1:
        if p1.value not in seen:
            seen.add(p1.value)
        p1=p1.next
    
    while p2:
        if p2.value not in seen:
            seen.add(p2.value)
        p2=p2.next
        
    # need to return a linked list:
    res=LinkedList()
        
    for element in seen:
        res.append(element)
    return res


def intersection(llist_1, llist_2):
    p1=llist_1.head #p1 points to llist_1
    p2=llist_2.head # p2 points to llist_2    
    seen1=set()  # use a set to record the values in list1, without duplicates
    seen2=set()  # use a set to record the values in list2, without duplicates
    while p1:
        if p1.value not in seen1:
            seen1.add(p1.value)
        p1=p1.next
        
    while p2:
        if p2.value not in seen2:
            seen2.add(p2.value)
        p2=p2.next
    
    res=LinkedList()    
    for val in seen1:    #check whether value in list1 is also in list2
        if val in seen2:
            res.append(val)
        
    return res

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print('Test 1')
print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))


# Test case 2

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)




print('Test 2')
print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))




# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('Test 3')
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
