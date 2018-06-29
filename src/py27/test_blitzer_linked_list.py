import unittest
import blitzer_linked_list as lnk

class test_linked_list(unittest.case.TestCase):
    """ Unit test class for the linked list module
    """
    def test_init(self):
        # test constructor for linked list and node class
        llst = lnk.lnklst()
        self.assertEqual(llst.head,None)
        self.assertEqual(llst.tail,None)
        self.assertEqual(llst.size,0)

        node = lnk.node(1)
        self.assertEqual(node.data,1)
        self.assertEqual(node.next,None)

    def test_update_tail(self):
        # test the tail tracking feature
        llst = lnk.lnklst()
        node1 = lnk.node(1)
        node2 = lnk.node(2)
        # this is the basic hard coded method and is not to be used
        # # since, this does not update the tail and the size of the linked list
        llst.head = node1
        llst.head.next = node2
        # the tail is not updated and also the size
        self.assertNotEqual(llst.tail,node2)
        self.assertNotEqual(llst.size,2)

        # call the update_tail method
        llst.update_tail()
        self.assertEqual(llst.tail,node2)

    def test_lnklst_size(self):
        # test to make sure the size calculation is correct
        llst = lnk.lnklst()
        node1 = lnk.node(1)
        node2 = lnk.node(2)
        node3 = lnk.node(3)
        # this is the basic hard coded method and is not to be used
        # # since, this does not update the tail and the size of the linked list
        llst.head = node1
        llst.head.next = node2
        llst.head.next.next = node3
        # the tail is not updated and also the size
        self.assertNotEqual(llst.tail,node3)
        self.assertNotEqual(llst.size,2)

        # call the update_tail method to track the tail
        llst.update_tail()
        # call the get_size() method to track size
        llst.get_size()
        self.assertEqual(llst.tail,node3)
        self.assertEqual(llst.size,3)

    def test_prepend(self):
        # test the prepend operation
        llst = lnk.lnklst()
        node1 = lnk.node(1)
        node2 = lnk.node(2)
        node3 = lnk.node(3)
        # this is the basic hard coded method and is not to be used
        # # since, this does not update the tail and the size of the linked list
        llst.head = node1
        llst.head.next = node2
        self.assertEqual(llst.head,node1)

        # update_tail
        llst.update_tail()
        # call prepend
        llst.prepend(node3)
        self.assertEqual(llst.head,node3)
        self.assertEqual(llst.head.next,node1)
        self.assertEqual(llst.head.next.next,node2)
        self.assertEqual(llst.tail,node2)

    def test_append(self):
        # test the append feature
        llst = lnk.lnklst()
        node1 = lnk.node(1)
        llst.append(node1)
        self.assertEqual(llst.head,node1)
        self.assertEqual(llst.tail,node1)
        self.assertEqual(llst.size,1)

        node2 = lnk.node(2)
        llst.append(node2)
        self.assertEqual(llst.head,node1)
        self.assertEqual(llst.tail,node2)
        self.assertEqual(llst.size,2)




if(__name__ == "__main__"):
    unittest.main()
