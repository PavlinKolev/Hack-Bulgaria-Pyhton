import unittest
from double_linked_list import DoubleLinkedList


class DoubleLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.dll = DoubleLinkedList()

    def test_eq(self):
        dll_2 = DoubleLinkedList()
        self.dll.add_element(5)
        self.dll.add_element(6)
        dll_2.add_element(5)
        dll_2.add_element(6)
        self.assertEqual(self.dll, dll_2)

    def test_add_last(self):
        self.dll.add_last(5)
        self.dll.add_last(8)
        self.assertEqual(self.dll.index(1), 8)

    def test_remove_last(self):
        self.dll.add_last(5)
        self.dll.add_last(8)
        self.dll.remove_last()
        last_ind = self.dll.size() - 1
        self.assertEqual(self.dll.index(last_ind), 5)

    def test_adding_element(self):
        self.dll.add_element(4)
        self.assertEqual(self.dll.size(), 1)

    def test_remove_element(self):
        self.dll.add_element(4)
        size = self.dll.size()
        self.dll.remove(0)
        size2 = self.dll.size()
        self.assertFalse(size == size2)

    def test_remove_element_2(self):
        self.dll.add_element(5)
        self.dll.add_element(6)
        self.dll.add_element(7)
        self.dll.remove(1)
        self.assertEqual(self.dll.index(1), 7)

    def test_size_1(self):
        self.dll.add_element(5)
        self.dll.add_element(5)
        self.dll.add_element(5)
        self.assertEqual(self.dll.size(), 3)

    def test_size_2(self):
        self.dll.add_element(5)
        self.dll.add_element(5)
        self.dll.add_element(5)
        self.dll.pop()
        self.dll.pop()
        self.assertEqual(self.dll.size(), 1)

    def test_index(self):
        self.dll.add_element(5)
        self.dll.add_element(2)
        self.assertEqual(self.dll.index(0), 5)
        self.assertNotEqual(self.dll.index(1), 5)

    def test_remove_element_2(self):
        self.dll.add_element(5)
        self.dll.add_element(6)
        self.dll.add_element(7)
        self.dll.remove(1)
        self.assertEqual(self.dll.index(1), 7)

    def test_pprint(self):
        self.dll.add_element(5)
        self.dll.add_element(6)
        self.dll.add_element(7)
        self.assertEqual(self.dll.pprint(), "5 -> 6 -> 7")

    def test_to_list(self):
        self.dll.add_element(5)
        self.dll.add_element(6)
        self.dll.add_element(7)
        self.assertEqual(self.dll.to_list(), [5, 6, 7])

    def test_add_at_index(self):
        self.dll.add_element(5)
        self.dll.add_element(6)
        self.dll.add_at_index(1, 7)
        self.assertEqual(self.dll.index(1), 7)
        self.assertEqual(self.dll.index(2), 6)

    def test_add_first(self):
        self.dll.add_element(5)
        self.dll.add_element(6)
        self.dll.add_first(7)
        self.assertEqual(self.dll.index(0), 7)
        self.assertEqual(self.dll.index(1), 5)

    def test_add_linked_list(self):
        self.dll.add_element(5)
        self.dll.add_element(6)
        dll_2 = DoubleLinkedList()
        dll_2.add_element(7)
        dll_2.add_element(8)
        self.dll.add_linked_list(dll_2)
        self.assertEqual(self.dll.to_list(), [5, 6, 7, 8])

    def test_dll_from_to(self):
        self.dll.add_element(5)
        self.dll.add_element(6)
        self.dll.add_element(7)
        self.dll.add_element(8)
        from_to = self.dll.ll_from_to(1, 3)
        self.assertEqual(from_to.to_list(), [6, 7, 8])

    def test_pop(self):
        self.dll.add_element(5)
        self.dll.add_element(6)
        self.dll.add_element(7)
        self.dll.pop()
        size = self.dll.size()
        self.assertEqual(self.dll.index(size - 1), 6)

    def test_reduce_to_unique(self):
        self.dll.add_element(5)
        self.dll.add_element(6)
        self.dll.add_element(7)
        self.dll.add_element(5)
        self.dll.add_element(6)
        self.dll.add_element(7)
        self.dll.reduce_to_unique()
        self.assertEqual(self.dll.to_list(), [5, 6, 7])

if __name__ == '__main__':
    unittest.main()
