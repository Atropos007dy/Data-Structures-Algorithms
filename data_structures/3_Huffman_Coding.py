import heapq
import sys
class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        if not other:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.freq < other.freq
        
    def __repr__(self):
        return ("{:}:{:}".format(self.symbol,self.freq))

def huffman_encoding(data):
    def codes(tree):
        def codes_core(root, recent):
            codes = {}
            if root is None:
                return {}
            if root.symbol is not None:
                codes[root.symbol] = recent
            codes.update(codes_core(root.left, recent + "0"))
            codes.update(codes_core(root.right, recent + "1"))
            return codes
        
        if tree.left == None and tree.right == None:
            return {tree.char:'0'}
            
        return codes_core(tree, "")
        
    if data == "":
        return "", None
    freq_dict = {}
        
    for char in data:
        freq_dict[char]=freq_dict.get(char,0)+1
    #print(freq_dict)
    dict_items = list(freq_dict.items())
    #print(dict_items)
    freq_dict = dict(sorted(dict_items, key=lambda x: x[1]))
    #print(freq_dict)
    heap = []
    for key in freq_dict:
        #print(heap)
        node = Node(key, freq_dict[key])
        heapq.heappush(heap,node)#
    
    # combine the 2 element with the smallest frequency
    if len(heap) == 1:
        node = heapq.heappop(heap)
        new_node = Node(None, node.freq)
        new_node.left = node
        heapq.heappush(heap, new_node)
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        new_node = Node(None, node1.freq + node2.freq)
        new_node.left = node1
        new_node.right = node2
        heapq.heappush(heap, new_node)
    
    tree = heapq.heappop(heap)
    #get the dictionary of the char encoding
    c = codes(tree) 
    print('encoding',c)
    encoded_data = ""
    for char in data:
        encoded_data += c[char]
    return encoded_data, tree


def huffman_decoding(encoded_data, tree):
        if encoded_data == "":
            return ""
        node = tree
        decoded_data = ""
        for char in encoded_data:
            if char == '0':
                node = node.left
            else:
                node = node.right
            if node.symbol is not None:
                decoded_data += node.symbol
                node = tree
        return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    
    print('Test 1: normal case')
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    
    print('Test 2: repetitive character')
    a_great_sentence = "AAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    
    print('Test 3:')
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
