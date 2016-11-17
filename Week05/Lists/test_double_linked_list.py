import unittest
from double_linked_list import DoubleLinkedList


class DoubleLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.d_ll = DoubleLinkedList()

    def test_add_last(self):
        self.d_ll.add_last(5)
        self.d_ll.add_last(8)
        self.assertEqual(self.d_ll.index(1), 8)

    def test_remove_last(self):
        self.d_ll.add_last(5)
        self.d_ll.add_last(8)
        self.d_ll.remove_last()
        last_ind = self.d_ll.size() - 1
        self.assertEqual(self.d_ll.index(last_ind), 5)


    def test_eq(self):
        d_ll_2 = DoubleLinkedList()
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        d_ll_2.add_element(5)
        d_ll_2.add_element(6)
        self.assertTrue(self.d_ll == d_ll_2)

    def test_adding_element(self):
        self.d_ll.add_element(4)
        self.assertEqual(self.d_ll.size(), 1)

    def test_remove_element(self):
        self.d_ll.add_element(4)
        size = self.d_ll.size()
        self.d_ll.remove(0)
        size2 = self.d_ll.size()
        self.assertFalse(size == size2)

    def test_remove_element_2(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        self.d_ll.add_element(7)
        self.d_ll.remove(1)
        self.assertEqual(self.d_ll.index(1), 7)

    def test_size_1(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(5)
        self.d_ll.add_element(5)
        self.assertEqual(self.d_ll.size(), 3)

    def test_size_2(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(5)
        self.d_ll.add_element(5)
        self.d_ll.pop()
        self.d_ll.pop()
        self.assertEqual(self.d_ll.size(), 1)

    def test_index(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(2)
        self.assertEqual(self.d_ll.index(0), 5)
        self.assertNotEqual(self.d_ll.index(1), 5)

    def test_remove_element_2(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        self.d_ll.add_element(7)
        self.d_ll.remove(1)
        self.assertEqual(self.d_ll.index(1), 7)

    def test_pprint(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        self.d_ll.add_element(7)
        self.assertEqual(self.d_ll.pprint(), "5 -> 6 -> 7")

    def test_to_list(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        self.d_ll.add_element(7)
        self.assertEqual(self.d_ll.to_list(), [5, 6, 7])

    def test_add_at_index(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        self.d_ll.add_at_index(1, 7)
        self.assertEqual(self.d_ll.index(1), 7)
        self.assertEqual(self.d_ll.index(2), 6)

    def test_add_first(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        self.d_ll.add_first(7)
        self.assertEqual(self.d_ll.index(0), 7)
        self.assertEqual(self.d_ll.index(1), 5)

    def test_add_linked_list(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        d_ll_2 = DoubleLinkedList()
        d_ll_2.add_element(7)
        d_ll_2.add_element(8)
        self.d_ll.add_linked_list(d_ll_2)
        self.assertEqual(self.d_ll.to_list(), [5, 6, 7, 8])

    def test_d_ll_from_to(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        self.d_ll.add_element(7)
        self.d_ll.add_element(8)
        from_to = self.d_ll.ll_from_to(1, 3)
        self.assertEqual(from_to.to_list(), [6, 7, 8])

    def test_pop(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        self.d_ll.add_element(7)
        self.d_ll.pop()
        size = self.d_ll.size()
        self.assertEqual(self.d_ll.index(size - 1), 6)

    def test_reduce_to_unique(self):
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        self.d_ll.add_element(7)
        self.d_ll.add_element(5)
        self.d_ll.add_element(6)
        self.d_ll.add_element(7)
        self.d_ll.reduce_to_unique()
        self.assertEqual(self.d_ll.to_list(), [5, 6, 7])

if __name__ == '__main__':
    unittest.main()
