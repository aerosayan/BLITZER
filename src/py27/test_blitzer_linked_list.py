import unittest
import blitzer_linked_list as lnk

msg = "UTST : running {t}  unit test..."
hr  = "------------------------------------------------------------------------"
class test_linked_list(unittest.case.TestCase):
    """ Unit test class for the linked list module
    """
    def test_init(self):
        # test constructor for linked list and node class
        print(msg.format(t="constructor"))
        llst = lnk.lnklst()
        self.assertEqual(llst.head,None)
        self.assertEqual(llst.tail,None)
        self.assertEqual(llst.size,0)

        node = lnk.node(1)
        self.assertEqual(node.data,1)
        self.assertEqual(node.next,None)
        print(hr)

    def test_update_tail(self):
        # test the tail tracking feature
        print(msg.format(t="update tail"))
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
        print(hr)

    def test_lnklst_size(self):
        # test to make sure the size calculation is correct
        print(msg.format(t="linked list size"))
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
        print(hr)

    def test_prepend(self):
        # test the prepend operation
        print(msg.format(t="prepend"))
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
        print(hr)

    def test_insert_after_key(self):
        # test the insert after key method
        print(msg.format(t="insert after key"))
        llst = lnk.lnklst()
        node1 = lnk.node(1)
        node2 = lnk.node(2)
        node3 = lnk.node(3)
        # this is the basic hard coded method and is not to be used
        # # since, this does not update the tail and the size of the linked list
        llst.head = node1
        llst.head.next = node2
        llst.head.next.next = node3
        self.assertEqual(llst.head,node1)
        # update_tail
        llst.update_tail()
        # call insert after key
        llst.insert_after_key(2,4)
        self.assertEqual(llst.head,node1)
        self.assertEqual(llst.head.next,node2)
        self.assertEqual(llst.head.next.next.data,4)
        self.assertEqual(llst.tail,node3)
        print(hr)

    def test_insert_after_node(self):
        # test the insert after node feature
        print(msg.format(t="insert after node"))
        llst = lnk.lnklst()
        node1 = lnk.node(1)
        node2 = lnk.node(2)
        node3 = lnk.node(3)
        node4 = lnk.node(4)
        # this is the basic hard coded method and is not to be used
        # # since, this does not update the tail and the size of the linked list
        llst.head = node1
        llst.head.next = node2
        llst.head.next.next = node3
        self.assertEqual(llst.head,node1)
        # update_tail
        llst.update_tail()
        # call insert after key
        llst.insert_after_node(node2,node4)
        self.assertEqual(llst.head,node1)
        self.assertEqual(llst.head.next,node2)
        self.assertEqual(llst.head.next.next,node4)
        self.assertEqual(llst.tail,node3)
        print(hr)


    def test_append(self):
        # test the append feature
        print(msg.format(t="append"))
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
        print(hr)

    def test_delete(self):
        # test the delete feature
        print(msg.format(t="delete"))
        llst = lnk.lnklst()
        node1 = lnk.node(1)
        node2 = lnk.node(2)
        node3 = lnk.node(3)
        node4 = lnk.node(4)

        # append is already verified
        llst.append(node1)
        llst.append(node2)
        llst.delete(2)                                # delete tail
        self.assertEqual(llst.head,node1)
        self.assertEqual(llst.tail,None)              # test if tail is null

        # run some more tests with delete
        llst.append(node2)
        llst.delete(1)                                # delete head
        print(llst.head.data)
        self.assertEqual(llst.head,node2)
        self.assertEqual(llst.tail,None)
        llst.delete(2)
        self.assertEqual(llst.head,None)
        self.assertEqual(llst.tail,None)
        self.assertEqual(llst.size,0)

        # run some more tests with delete
        llst.append(node1)
        llst.append(node2)
        llst.append(node3)
        llst.append(node4)

        llst.delete(2)
        self.assertEqual(llst.head,node1)
        self.assertEqual(llst.head.next,node3)
        llst.delete(3)
        self.assertEqual(llst.head.next,node4)
        self.assertEqual(llst.tail,node4)

    def test_delete_all(self):
        # test delete all
        pass

    def test_get_size(self):
        # test size of linked list
        pass


if(__name__ == "__main__"):
    unittest.main()
