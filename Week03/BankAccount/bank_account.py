class BankAccount:
    def __init__(self, name, balance, currency):
        if type(name) is not str:
            raise TypeError("Name of Bank Account must be a string.")
        BankAccount._check_amount(balance)
        self.name = name
        self.curr_balance = balance
        self.currency = currency
        self.history_list = ["Account was created"]

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.curr_balance, self.currency)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        self.history_list.append("__int__ check -> {}{}".format(self.curr_balance, self.currency))
        return self.curr_balance

    def deposit(self, amount):
        BankAccount._check_amount(amount)
        self.curr_balance += amount
        self.history_list.append("Deposited {}{}".format(amount, self.currency))

    def balance(self):
        self.history_list.append("Balance check -> {}{}".format(self.curr_balance, self.currency))
        return self.curr_balance

    def withdraw(self, amount):
        BankAccount._check_amount(amount)
        if amount <= self.curr_balance:
            self.curr_balance -= amount
            self.history_list.append("{}{} was withdrawed".format(amount, self.currency))
            return True
        else:
            self.history_list.append("Withdraw for {}{} failed.".format(amount, self.currency))
            return False

    def transfer_to(self, account, amount):
        if type(account) is not BankAccount:
            raise TypeError("Account for trasfer must be of type BankAccount.")
        BankAccount._check_amount(amount)
        if amount <= self.curr_balance and self.currency == account.currency:
            self.curr_balance -= amount
            account.transfer_from(self, amount)
            self.history_list.append("Transfer to {} for {}{}".format(account.name, amount, self.currency))
            return True
        else:
            self.history_list.append("Transfer to {} for {}{} failed".format(account.name, amount, self.currency))
            return False

    def transfer_from(self, account, amount):
        self.curr_balance += amount
        self.history_list.append("Transfer from {} for {}{}".format(account.name, amount, self.currency))

    def history(self):
        return self.history_list

    @classmethod
    def _check_amount(cls, amount):
        if type(amount) is not int:
            raise TypeError("Balance of Bank must be int.")
        if amount < 0:
            raise ValueError("Balance canot be negative.")
