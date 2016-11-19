import unittest
from cash_desk import Bill, BatchBill, CashDesk


class TestBill(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(50)

    def test_str(self):
        self.assertEqual(str(self.bill), "A 50$ bill")

    def test_int(self):
        self.assertEqual(int(self.bill), 50)

    def test_eq(self):
        self.assertTrue(self.bill == Bill(50))
        self.assertFalse(self.bill == Bill(60))

    def test_lt(self):
        self.assertTrue(self.bill < Bill(60))


class TestBatchBill(unittest.TestCase):
    def setUp(self):
        self.batch = BatchBill([Bill(50), Bill(10), Bill(30), Bill(20)])

    def test_getitem(self):
        self.assertEqual(self.batch[0], Bill(50))
        self.assertRaises(IndexError, self.batch.__getitem__, 5)

    def test_total(self):
        self.assertEqual(self.batch.total(), 110)


class TestCashDesck(unittest.TestCase):
    def setUp(self):
        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        self.desk = CashDesk()
        self.desk.take_money(batch)
        self.desk.take_money(Bill(10))

    def test_total(self):
        self.assertEqual(self.desk.total(), 390)

    def test_inspect(self):
        expect = "We have a total of 390$ in the desk\n"
        expect += "We have the following count of bills, sorted in ascending order:\n"
        expect += "10$ bills - 2\n20$ bills - 1\n50$ bills - 1\n100$ bills - 3"
        self.assertEqual(self.desk.inspect(), expect)


if __name__ == '__main__':
    unittest.main()
