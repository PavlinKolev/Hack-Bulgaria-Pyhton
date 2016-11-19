class Bill:
    def __init__(self, amount):
        if type(amount) is not int:
            raise TypeError("Amount of bill must be int.")
        if amount < 0:
            raise ValueError("Amount of bill cannot be neagtive")
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

    def __lt__(self, other):
        return self.amount < other.amount


class BatchBill:
    def __init__(self, bills):
        if type(bills) is not list:
            raise TypeError("Bills in BatchBill must be list of Bill.")
        self.bills = bills

    def __len__(self):
        return len(bills)

    def __getitem__(self, index):
        if index < 0 or index >= len(self.bills):
            raise IndexError("Index out of range.")
        return self.bills[index]

    def total(self):
        return sum([int(bill) for bill in self.bills])


class CashDesk:
    def __init__(self):
        self.total_money = 0
        self.bills = {}

    def take_money(self, money):
        if type(money) is not Bill and type(money) is not BatchBill:
            raise TypeError("Type of money for CashDesk must be Bill or BatchBill.")
        if type(money) is Bill:
            self.total_money += int(money)
            self.add_bill(money)
        else:
            self.total_money += money.total()
            for bill in money:
                self.add_bill(bill)

    def add_bill(self, bill):
        if bill not in self.bills.keys():
            self.bills[bill] = 1
        else:
            self.bills[bill] += 1

    def total(self):
        return self.total_money

    def inspect(self):
        bills = list(self.bills.keys())
        bills.sort()
        result = "We have a total of {}$ in the desk\n".format(self.total_money)
        result += "We have the following count of bills, sorted in ascending order:"
        for bill in bills:
            result += "\n{}$ bills - {}".format(int(bill), self.bills[bill])
        return result
