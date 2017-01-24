class BaseColumn:
    def set_data(self, data):
        print("I am {} with data {}".format(self.__class__.__name__, data))


class PKColumn(BaseColumn):
    def __init__(self, type_="INTEGER", autoincrement=True):
        self.type = type_
        if self.type == "INTEGER":
            self.autoincrement = autoincrement
        else:
            self.autoincrement = None

    def __str__(self):
        res = self.type + " PRIMARY KEY"
        res += " AUTOINCREMENT" if self.autoincrement else ""
        return res

    def __repr__(self):
        return self.__str__()


class IntegerColumn(BaseColumn):
    def __str__(self):
        return "INTEGER"

    def __repr__(self):
        return self.__str__()


class TextColumn(BaseColumn):
    def __str__(self):
        return "TEXT NOT NULL"

    def __repr__(self):
        return self.__str__()
