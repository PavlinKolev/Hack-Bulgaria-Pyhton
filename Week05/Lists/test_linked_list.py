import unittest
from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_eq(self):
        ll_2 = LinkedList()
        self.ll.add_element(5)
        self.ll.add_element(6)
        ll_2.add_element(5)
        ll_2.add_element(6)
        self.assertTrue(self.ll == ll_2)

    def test_adding_element(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.size(), 1)

    def test_remove_element(self):
        self.ll.add_element(4)
        size = self.ll.size()
        self.ll.remove(0)
        size2 = self.ll.size()
        self.assertFalse(size == size2)

    def test_remove_element_2(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.ll.remove(1)
        self.assertEqual(self.ll.index(1), 7)

    def test_size_1(self):
        self.ll.add_element(5)
        self.ll.add_element(5)
        self.ll.add_element(5)
        self.assertEqual(self.ll.size(), 3)

    def test_size_2(self):
        self.ll.add_element(5)
        self.ll.add_element(5)
        self.ll.add_element(5)
        self.ll.pop()
        self.ll.pop()
        self.assertEqual(self.ll.size(), 1)

    def test_index(self):
        self.ll.add_element(5)
        self.ll.add_element(2)
        self.assertEqual(self.ll.index(0), 5)
        self.assertNotEqual(self.ll.index(1), 5)

    def test_remove_element_2(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.ll.remove(1)
        self.assertEqual(self.ll.index(1), 7)

    def test_pprint(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.assertEqual(self.ll.pprint(), "5 -> 6 -> 7")

    def test_to_list(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.assertEqual(self.ll.to_list(), [5, 6, 7])

    def test_add_at_index(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_at_index(1, 7)
        self.assertEqual(self.ll.index(1), 7)
        self.assertEqual(self.ll.index(2), 6)

    def test_add_first(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_first(7)
        self.assertEqual(self.ll.index(0), 7)
        self.assertEqual(self.ll.index(1), 5)

    def test_add_linked_list(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        ll_2 = LinkedList()
        ll_2.add_element(7)
        ll_2.add_element(8)
        self.ll.add_linked_list(ll_2)
        self.assertEqual(self.ll.to_list(), [5, 6, 7, 8])

    def test_ll_from_to(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.ll.add_element(8)
        from_to = self.ll.ll_from_to(1, 3)
        self.assertEqual(from_to.to_list(), [6, 7, 8])

    def test_pop(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.ll.pop()
        size = self.ll.size()
        self.assertEqual(self.ll.index(size - 1), 6)

    def test_reduce_to_unique(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.ll.reduce_to_unique()
        self.assertEqual(self.ll.to_list(), [5, 6, 7])

if __name__ == '__main__':
    unittest.main()
