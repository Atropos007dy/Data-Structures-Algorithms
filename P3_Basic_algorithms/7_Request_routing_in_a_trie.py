# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = 'root handler', default_handler = 'not found handler'):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler, default_handler)
        

    def Trieinsert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        # ['about', 'me']
        curr_node = self.root
        for part in path_list:
            if part not in curr_node.children:
                curr_node.insert(part, curr_node.default_handler)
            curr_node = curr_node.children[part]
        
    
        curr_node.handler = handler
            
    
    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr_node = self.root
        for part in path_list:
            if part in curr_node.children:
                curr_node = curr_node.children[part]
            else:
                return None
                break
            
        
        return curr_node.handler

class RouteTrieNode(object):
    def __init__(self, handler = 'root handler', default_handler = 'not found handler'):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
        self.default_handler = default_handler
        

    def insert(self, part, part_handler):
        # Insert the node as before
        # part - an item from path_list
        #part_handler - the corresponding handler for the current node
        
        if part not in self.children:
            self.children[part] = RouteTrieNode(handler = part_handler)

        
#The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler = 'root handler', default_handler = 'Not Found Handler'):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.RouterTrie = RouteTrie(handler, default_handler)
        self.RouterTrie.root_handler = handler

    def add_handler(self, new_path, path_handler):
        # Add a handler for a path
        # You will need to split the path and pass the path parts
        new_path_list = self.split_path(new_path)
        return self.RouterTrie.Trieinsert(new_path_list, path_handler)
        

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        if path_list == ['', '']:
            return self.RouterTrie.root_handler
        return self.RouterTrie.find(path_list)


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_parts = path.split('/')
        return path_parts


        
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/test", "test handler")  # add a route
router.add_handler("/home/about/delta", "delta handler")  # add a route


# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/test")) # should print 'test handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/delta")) # should print 'delta handler' 