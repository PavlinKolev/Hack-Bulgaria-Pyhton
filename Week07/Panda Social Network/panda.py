class Panda:
    def __init__(self, name, mail, gender):
        self.__set_name(name)
        self.__set_email(mail)
        self.__set_gender(gender)

    def __eq__(self, other):
        return self._name == other._name\
            and self._email == other._email\
            and self._gender == other._gender

    def __hash__(self):
        return hash(self._name)*hash(self._mail)*hash(self._gender)

    def __str__(self):
        return "{} {} {}".format(self._name, self._mail, self._gender)

    def __repr__(self):
        return self.__str__()

    def name(self):
        return self._name

    def email(self):
        return self._mail

    def gender(self):
        return self._gender

    def isMale(self):
        return self.gender == "male"

    def isFemaile(self):
        return not(self.isMale())

    def __set_name(self, name):
        if type(name) is not str:
            raise TypeError("Name of panda must be string")
        self._name = name

    def __set_email(self, mail):
        if type(mail) is not str:
            raise TypeError("E-mail of panda must be string.")
        # TODO: with regular expression
        if "@" not in mail:
            raise ValueError("Not a valid e-mail.")
        self._email = mail

    def __set_gender(self, gender):
        if type(gender) is not str:
            raise TypeError("Gender of panda must be string")
        if gender != "male" and gender != "female":
            raise ValueError("Not a valid type of gender.")
