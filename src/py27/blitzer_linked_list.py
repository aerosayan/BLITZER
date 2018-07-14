# AUTHOR : SAYAN BHATTACHARJEE
# EMAIL  : aero.sayan@gmail.com
# LICENSE: DEFAULT, and will remain so.
# FILE   : blitzer_linked_list.py
# INFO   : linked list module for competitive programming.
# STYLE  : smaller case with underscore for speed

#===============================================================================
#                                MEMBERS
#===============================================================================
# node class
class node:
    """Node class for creating linked lists and designed for
    competetive programming.
    """
    #----------------------------------------
    # creating the object
    def __init__(self,data):
        self.data = data # assign data
        self.next = None # set next as null
        return
    #----------------------------------------
#end class node

# linked list class
class lnklst:
    """Linked list class for creating linked lists and designed
    for competitive programming
    """
    #----------------------------------------
    # Constructor
    def __init__(self):
        self.head = None # set the head of the linked list as null
        self.tail = None # set the last of the linked list as null
        self.size = 0 # set linked list size as 0
        return
    #----------------------------------------
    # Print the full list
    def print_all(self):
        node = self.head
        while(node):
            # at end of list
            if(node.next == None):
                print(node.data) # we print data and go to new line
                node = node.next # iterator
            else:
                print(node.data),
                node = node.next #iterator
        # end while
        return
    #----------------------------------------
    # Find and updata self.tail
    def update_tail(self):
        # incase tail is not already set
        if(self.tail == None):
            self.tail = self.head
        #then
        # and update varaible if necessary
        tail = self.tail
        # incase tail is already set
        while(tail.next):
            tail = tail.next #iterator
        #end while
        self.tail = tail
        return
    #----------------------------------------
    # Insert a new node at the begining
    def prepend(self,new_node):
        # ensure linked list size calculation is done to get correct sizes later
        self.get_size()
        # first point the head to the end of the new node
        new_node.next = self.head
        # then assign the head as new node
        self.head = new_node
        # if we are at the end then we have essentially performed an append
        # thus update last node
        if(new_node.next.next == None):
            self.tail = new_node.next

        # update size
        self.size = self.size + 1
        return
    #----------------------------------------
    # Insert after an object of the given data key
    def insert_after_key(self,data_key,new_data):
        # ensure linked list size calculation is done to get correct sizes later
        self.get_size()
        new_node  = node(new_data)            # call constructor to node class
        prev_node = None                      # placeholder

        _node = self.head                     # temp node variable

        while(_node.next):                    # run till tail
            if(_node.data == data_key):
                prev_node = _node
                break
            _node = _node.next
            # end if
        # end while

        # insert the new node after prev node
        new_node.next  = prev_node.next
        prev_node.next = new_node

        # if we are at the end then we have essentially performed an append
        # thus update last node
        if(new_node.next == None):
            self.tail = new_node

        # update size
        self.size += 1
        return
    #----------------------------------------
    # Insert after a certain node object
    def insert_after_node(self,prev_node,new_node):
        # ensure linked list size calculation is done to get correct sizes later
        self.get_size()
        # put the next node after new node assuming prev_node is present in list
        new_node.next = prev_node.next
        # put the new node after prev node
        prev_node.next = new_node

        # if we are at the end then we have essentially performed an append
        # thus update last node
        if(new_node.next == None):
            self.tail = new_node

        # update size
        self.size = self.size + 1
        return
    #----------------------------------------
    # Add a node at the end in O(1)
    def append(self,new_node):
        # ensure linked list size calculation is done to get correct sizes later
        self.get_size()
        # similar to vector
        if(self.head == None): # if zero nodes are present
            self.head = new_node
            self.tail = new_node
        else:
        # compare with self.tail and if it contains a next node then we have
        # appended something to the linked list and it contains more
        # than one node now; thus, go to the end
            self.update_tail()
            tail = self.tail
            while(tail.next):
                tail = tail.next #iterator
            # end while

            # at the end add the new node and update self.tail to point to it
            tail.next = new_node
            self.tail = new_node
        # end if else
        # update size
        self.size = self.size + 1
        return
    #----------------------------------------
    # Delete node with the data same as passed dataKey
    def delete(self,data_key):
        # if linked list is empty
        if(self.head == None):
            return

        # otherwise traverse over the full list to find the first occurence
        node = self.head
        if(node.data == data_key):                 # deleting head
            self.head = node.next                  # update new head
            node.next = None                       # delete old head
            self.size -= 1                         # decrease size count
            # if only head is present
            if(self.head and self.head.next == None):
                self.tail = None

        n    = node
        while(node.next):                          # complexity O(n)
            n = node # current node
            node = node.next # next node # iterator
            # if we find the node with the same data key then remove it
            if(node.data is not None and node.data == data_key):
                # link current node with the node after the node with datakey
                n.next = node.next
                if(n.next == None):                # we have only head left
                    self.tail = None

                # remove all links with the next node with data key
                node.next = None
                # update size count
                self.size -= 1
                return
        #end while

    #----------------------------------------
    # Delete the linked list
    def delete_all(self):
        self.head = None
        self.tail = None
        self.size = 0

    #----------------------------------------
    # Get the size of the singly linked link list
    def get_size(self,force_recount = False):
        # return the stored size if not forced with O(1) complexity
        if(self.size > 0 and force_recount == False):
            return self.size
        else:
            print("INF : pre forced calculation self.size : " + str(self.size))
            print("INF : performing linked list forced size count...")
            #else do forced recount with O(n) complexity
            node  = self.head
            count = 0
            while(node): # node is not None
                count += 1
                node = node.next
            # end while
            #  update size value if force_recount == false
            self.size = count
            return count
    #----------------------------------------
    # Search and return if we find an object with the same passed data key
    def search(self,data_key):
        # if head is null
        if(self.head == None):
            return False
        node = self.head
        while(node.next):
            if(node.data == data_key):
                return True
            else:
                node = node.next
        # end while
        return False
    #----------------------------------------
    # Go to nth position and get node
    def at(self,n):
        node  = self.head
        i = 0 # accessor
        I = 0 # iterator
        while(I <= n and node):
            i  = I
            I += 1
            if(i == n): # since zero indexed
                return node
            if(node): # if node is not None
                node = node.next
        # end while

        print("ERR : link list is smaller than required position " + str(n))
        print("ERR : asserting false to stop execution...")
        assert(False)
    #----------------------------------------
    # Go to nth position from the last
    def at_rev(self,n):
        # if n == 1 then return tail
        if(n == 1):                      # complexity O(1)
            return self.tail
        else:                            # complexity O(n)
            node = self.head
            i = 0 # accessor
            I = 0 # iterator
            len = self.get_size() # size of the linked list
            while(I < len-n):
                i = I
                I += 1
                node = node.next
            # end while
            return node
        # end if else
        print("ERR : link list is smaller than required reverse position " + str(n))
        print("ERR : asserting false to stop execution...")
        assert(False)
    #----------------------------------------
    # Floyd's cycle finding algorithm to detect loops in linked list
    def is_loop(self):
        # we use a fast and slow node
        slow_node = self.head
        fast_node = self.head
        # traverse over the linked list and try to detect loop
        while(slow_node and fast_node and fast_node.next):
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if( slow_node == fast_node):
                return True,slow_node
        # end while
        return False,None
    #----------------------------------------
    # Get loop size
    def get_loop_size(self,loop_start):
        # we iterate the loop and find the loop size
        if (loop_start == None):
            return 0
        count = 1  # we are starting count at 1 since we will not come
        # back to loop_start in the while loop
        node = loop_start.next
        print(loop_start.data),
        while(node is not loop_start ):
            count += 1 # update count
            print(node.data),
            node = node.next # go to next node
        # end while
        print(loop_start.data),
        print("")
        return count
    #----------------------------------------
    # Reverse the full linked list
    def reverse(self):
        old_head  = self.head            # save the current head
        prev_node = None                 # previous node
        curr_node = self.head            # current node
        next_node = None                 # next node

        # traverse the full list and reverse it
        while(curr_node):                    # Complexity of O(n)
            next_node = curr_node.next       # set next_node
            curr_node.next = prev_node       # break link and rotate it 90 deg
            prev_node = curr_node            # move prev_node to curr_node
            curr_node = next_node            # move curr_node to next_node
        #end while
        self.head = prev_node                # set the last element as head
        self.tail = old_head                 # set the first element as tail
        return
    #----------------------------------------
    # Print reverse without using any more space
    def print_reverse(self, node):
        if(node is None):
            return                         # return control back
        # end if
        self.print_reverse(node.next)      # call recursively next level
        print(node.data),                  # print in one line
        return
    #----------------------------------------
    # Swap nodes with the given dataKeys
    def swap(self,data_key_1,data_key_2):
        node  = self.head
        node1 = None
        node2 = None
        prev_node  = None
        prev_node1 = None
        prev_node2 = None
        # find both of the nodes
        while(node): # complexity O(n)
            # if one or both of them are not found
            if(node1 == None or node2 == None):
                if(node.data == data_key_1):
                    node1 = node # the first node encountered
                    prev_node1 = prev_node # the previous node of node1
                elif(node.data == data_key_2):
                    node2 = node # the second node encountered
                    prev_node2 = prev_node # the previous node of node2
            else: # if both of them are found
                node = self.tail # go to end , casue here node.next == None
            #end if
            prev_node = node
            node = node.next
            #print("DBG : changed node")
        # end while

        # error checking
        if(self.get_size() <= 1):
            print("ERR : can not swap with link list size <=1 ... ")
            print("INF : asserting false... ")
            assert(false)
        # end if
        if(node1 == None or node2 == None ):
            print("INF : nodes not found to swap with data keys...")
            print("INF : data_key_1 : " + str(data_key_1)),
            print("\t | data_key_2 : "  + str(data_key_2))
            print("INF : cancelling swap...")
            return
        elif( node1 == self.head ):
            print("DBG : swapping node1, which is self.head ....")
            next1 = node1.next
            next2 = node2.next
            # swap front to back
            self.head = node2 # bring node2 to front  # TODO : looped lists ?
            prev_node2.next = node1 # send node1 ot back
            node2.next = next1 # link next of node1
            node1.next = next2 # link next of node2
            return
        elif( node2 == self.tail):
            print("DBG :  swapping node2, which is self.tail ....")
            next1 = node1.next
            next2 = node2.next # probably null but not necessarily
            # swap front to back
            prev_node1.next = node2
            prev_node2.next = node1
            node2.next = next1
            node1.next = next2
            return
        elif(prev_node1 and prev_node2): # swap the nodes if prev_node is found
            next1 = node1.next
            next2 = node2.next
            # swap front to back
            prev_node1.next = node2
            prev_node2.next = node1
            node2.next = next1
            node1.next = next2
        else: # we have error
            print("ERR : all swap tests failed...")
            assert(False)
    #----------------------------------------
    # Swap head and tail
    def swap_ends(self):
        if(self.get_size() <=1): # compelexity O(1) or in very small cases O(n)
            print("ERR : can not swap with link list size <=1 ... ")
            print("INF : asserting false... ")
            assert(false)

        # we traverse list to find the node before tail
        prev_node = self.head
        while(prev_node.next is not self.tail): # causes complexity O(n)
            prev_node = prev_node.next
        # temporary variables
        node1 = self.head
        node2 = self.tail
        next1 = self.head.next
        next2 = self.tail.next
        # swap head and tail from front to back
        self.tail  = node1
        self.head  = node2
        # now we fix swapped connections,be very careful
        self.head.next = next1 # previously tail
        self.tail.next = next2 # previously head
        # most importantly point the prev_node.next to the new tail
        prev_node.next = self.tail
        return
    #----------------------------------------
    # Join two different linked lists
    def join(self,other):
        if(other.__class__.__name__ is not "lnklst"):
            raise TypeError("ERR : lnklst.join(self,other) :"
            + " other needs to be object of lnklst class")
        # end if
        self.tail.next = other.head                 # simply link them
        self.update_tail()                          # udpate tail to be correct
        self.get_size(force_recount = True)         # update size to be correct
        return
    #----------------------------------------
    # Are the two linked lists identical?
    def is_identical(self,other):
        if(other.__class__.__name__ is not "lnklst"):
            raise TypeError("ERR : lnklst.is_identical(self,other) :"
            + " other needs to be object of lnklst class")
        # end if

        n =  self.get_size()                # hopefully O(1) or worst O(n)
        m = other.get_size()                # hopefully O(1) or worst O(n)

        if (n != m):                        # first simple test hoping O(1)
            return False
        else:                     # n == m  # run test on both of the lists
            node1 = self.head
            node2 = other.head
            # traverse both linked lists
            while(node1 and node2):
                if(node1.data != node2.data):
                    return False
                node1 = node1.next
                node2 = node2.next
            # end while

        return True                         # if all tests fail means
    #----------------------------------------
