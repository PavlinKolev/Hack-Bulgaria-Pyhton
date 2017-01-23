class BaseColumn:
    def set_data(self, data):
        print("I am {} with data {}".format(self.__class__.__name__, data))


class PKColumn(BaseColumn):
    pass


class IntegerColumn(BaseColumn):
    pass


class TextColumn(BaseColumn):
    pass
