# AUTHOR : SAYAN BHATTACHARJEE
# EMAIL  : aero.sayan@gmail.com
# LICENSE: DEFAULT, and will remain so.
# FILE   : blitzer_linked_list.py
# INFO   : linked list module for competitive programming.
# STYLE  : smaller case with for speed

#===============================================================================
#                             MEMBERS
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

#end class node

# linked list class
class lnklst:
    """Linked list class for creating linked lists and designed
    for competitive programming
    """
    #----------------------------------------
    # creating the object
    def __init__(self):
        self.head = None # set the head of the linked list as null
        self.tail = None # set the last of the linked list as null
        self.size = 0 # set linked list size as 0

    # print the full list
    def print_list(self):
        node = self.head
        while(node):
            # at end of list
            if(node.next == None):
                print(node.data) # we print data and go to new line
                node = node.next #iterator
            else:
                print(node.data),
                node = node.next #iterator
        # end while

    #----------------------------------------
    # find and updata self.tail
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

    #----------------------------------------
    # insert a new node at the begining
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

    #----------------------------------------
    # insert after a certain node
    def insert_after(self,prev_node,new_node):
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

    #----------------------------------------
    # add a node at the end in O(1)
    def append(self,new_node):
        # ensure linked list size calculation is done to get correct sizes later
        self.get_size()
        # similar to vector
        if(self.head == None): # if zero nodes are present
            self.head = new_node
            self.tail = new_node
        else:
        # compare with self.tail and if it contains a next node then
        # we have appended something to the linked list and it contains more
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
    # delete node with the data same as passed dataKey
    def delete(self,data_key):
        # if linked list is empty
        if(self.head == None):
            return

        # otherwise traverse over the full list to find the first occurence
        node = self.head
        n    = node
        while(node.next):
            n = node # current node
            node = node.next # next node # iterator
            # if we find the node with the same data key then remove it
            if(node.data is not None and node.data == data_key):
                # link current node with the node after the node with datakey
                n.next = node.next
                # remove all links with the next node with data key
                node.next = None
                # update size
                self.size = self.size - 1
                return
        #end while

    #----------------------------------------
    # delete the linked list
    def delete_all(self):
        self.head = None
        self.tail = None
        self.size = 0

    #----------------------------------------
    # return the size of the singly linked link list
    def get_size(self,force_recount = False):
        # return the stored size if not forced with O(1) complexity
        if(self.size > 0 and force_recount == False):
            return self.size
        else:
            print("INF : pre forced calculation self.size : "+str(self.size))
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
    # search and return if we find an object with the same passed data key
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
    # go to nth position and get node
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
    # go to nth position from the last
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

    #----------------------------------------
    # Floyd's cycle finding algorithm to detect loops in linked list
    def find_loop(self):
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

#===============================================================================
#                                TESTS
#===============================================================================
def test_all():
    """Run all unit tests to ensure everything is okay with the library
    """
    test1()

def test1():
    """Linked list creation test
    """
    print("INF : running cplnklst.test1()...")
    # create linked list and assign head
    llist = lnklst()
    llist.head = node(1)

    # create separate nodes which will be put in the linked list
    second = node(2)
    third  = node(3)
    fourth = node(4)
    fifth  = node(5)
    sixth  = node(6)
    seventh= node(7)
    eighth = node(8)


    # complete the linked list
    llist.head.next = second #  bug : the tail is not updated
    second.next = third
    # third.next = None # is automatically set
    llist.append(fourth) # add a new node at the end
    llist.append(fifth) # add a new node at the end
    llist.append(sixth) # add a new node at the end
    llist.append(seventh)
    llist.append(eighth)
    # print all
    llist.print_list()
    print("size : " + str(llist.get_size()))
    print(llist.search(5))
    print(llist.search(3))
    print(llist.at(0).data)
    print(llist.at(1).data)
    print(llist.at_rev(1).data)
    print(llist.at_rev(4).data)
    print(llist.at_rev(5).data)
    llist.prepend(third)
    print("loop size : " +str(llist.get_loop_size(llist.find_loop()[1])))
