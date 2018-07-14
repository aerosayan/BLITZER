# AUTHOR : SAYAN BHATTACHARJEE
# EMAIL  : aero.sayan@gmail.com
# LICENSE: DEFAULT, and will remain so.
# FILE   : blitzer_search_tree.py
# INFO   : binary search tree module for competitive programming.
# STYLE  : smaller case with underscore for speed

import blitzer_tree_utilities as tu

#===============================================================================
#                                MEMBERS
#===============================================================================

# node class
class node:
    """ Node class for binary search tree containing value,left and right node
    """
    #----------------------------------------
    def __init__(self,_val):
        # Constructor
        self.val   = _val                            # assign value
        self.left  = None                            # left node
        self.right = None                            # right node
        return
    #----------------------------------------

# binary search tree
class bst:
    """ Binary search tree class
    """
    #----------------------------------------
    def __init__(self):
        # Constructor
        self.root  = None                            # assign root node
        self.size  = 0                               # size of bst
        return
    #----------------------------------------
    # Increment size
    def incsize(self):
        self.size += 1
        return
    #----------------------------------------
    # Search and find the node we want from the binary search tree
    def search(self,_node,_key):
        if(_node is None or node.val == _key):            # base case
            return node
        # key value is lesser than node's value
        if(_key < _node.val ):                            # search left node
            return search(_node.left,_key)
        # key value is greater than node's value
        elif(_key > _node.val):                           # search right node
            return search(_node.right,_key)
    #----------------------------------------
    # Add new node to the tree using recursion
    def insert(self, _val, _node = None):
        # Awesome default argument
        if(_node == None):
            _node = self.root
        # If the node is null then add new node with the given value
        if(_node == None):
            self.root = node(_val)                    # assign new node to root
            _node = self.root                         # assign root to _node
            print(_node.val),
            self.incsize()                            # increment size
            return
        # else check if the left and right exist and add new nodes
        if(_val < _node.val):
            if(_node.left == None):                   # if node is null
                _node.left = node(_val)               # assign new node to left
                print(_node.left.val),
                self.incsize()                        # increment size
                return
            else:                                     # we can not pass None
                self.insert(_val,_node = _node.left)  # recurse to insert node
            # end if
        elif(_val > _node.val):
            if(_node.right == None):                  # if node is null
                _node.right = node(_val)              # assign new node to right
                print(_node.right.val),
                self.incsize()                        # increment size
                return
            else:
                self.insert(_val, _node = _node.right) # recurse to insert node
            # end if
        # end if
    #----------------------------------------
    # Delete node matching the given key value
    def delete(self ,_node , _key):
        # base case
        if(_node == None):
            return None

        # delete from left side of tree if the key is smaller than _node
        if(_key < _node.val):
            _node.left = _node.delete(_node.left,_key)
        # else if the value is higher, the node is in the right side of _node
        elif(_key > _node.val):
            _node.right = _node.delete(_node.right,_key)

if __name__ == "__main__":
    b = bst()
    print("TREE :"),
    b.insert(50)
    b.insert(30)
    b.insert(20)
    b.insert(40)
    b.insert(70)
    b.insert(60)
    b.insert(80)
    print("")
    print("SIZE : " + str(b.size))

    tu.trav_inorder(b.root)
