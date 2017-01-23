import sqlite3
from ikea.base import DateBaseMeta
from ikea.fields import PKColumn, TextColumn, IntegerColumn


class BaseModel(metaclass=DateBaseMeta):
    __tablename__ = None

    # db = sqlite3.connect("test.db")
    # db.row_factory = sqlite3.Row
    # c = db.cursor()

    @classmethod
    def create_all_tables(cls):
        print([cl.__name__ for cl in cls._registry])

    @classmethod
    def create_obj(cls, **kwargs):
        for k, v in kwargs.items():
            if k not in cls._fields:
                raise AttributeError("{} is not attribute for {}".format(k, cls.__name__))
            cls._fields[k].set_data(v)


class User(BaseModel):
    __tablename__ = "Users"

    id = PKColumn()
    name = TextColumn()
    age = IntegerColumn()


class Student(User):
    __tablename__ = "Students"

    email = TextColumn()
    shirt_size = IntegerColumn()


class Movie(BaseModel):
    __tablename__ = "Movies"

    title = TextColumn()
    year = IntegerColumn()
    budget = IntegerColumn()
