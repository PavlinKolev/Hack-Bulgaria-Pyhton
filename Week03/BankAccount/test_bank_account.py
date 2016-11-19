import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Pesho", 0, "BGN")

    def test_str(self):
        self.assertEqual(str(self.account), "Bank account for Pesho with balance of 0BGN")

    def test_int(self):
        self.assertEqual(int(self.account), 0)

    def test_depsit(self):
        self.account.deposit(50)
        self.assertEqual(int(self.account), 50)

    def test_deposit_with_negative(self):
        self.assertRaises(ValueError, self.account.deposit, -50)

    def test_balance(self):
        self.account.deposit(150)
        self.assertEqual(self.account.balance(), 150)

    def test_withdraw(self):
        self.account.deposit(1000)
        self.account.withdraw(600)
        self.assertEqual(self.account.balance(), 400)

    def test_withdraw_with_too_much(self):
        self.account.deposit(200)
        self.account.withdraw(500)
        self.assertEqual(self.account.balance(), 200)

    def test_transfer_to(self):
        account_2 = BankAccount("Gosho", 1000, "BGN")
        account_2.transfer_to(self.account, 600)
        self.assertEqual(account_2.balance(), 400)
        self.assertEqual(self.account.balance(), 600)

    def test_history(self):
        self.account.deposit(1000)
        self.account.balance()
        str(self.account)
        int(self.account)
        self.account.history()
        self.account.withdraw(500)
        self.account.balance()
        self.account.withdraw(1000)
        self.account.balance()
        history = self.account.history()
        expected = ['Account was created', 'Deposited 1000BGN',
        'Balance check -> 1000BGN', '__int__ check -> 1000BGN',
        '500BGN was withdrawed', 'Balance check -> 500BGN',
        'Withdraw for 1000BGN failed.', 'Balance check -> 500BGN']
        self.assertEqual(history, expected)


if __name__ == '__main__':
    unittest.main()
