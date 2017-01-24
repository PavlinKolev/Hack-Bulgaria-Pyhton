import sqlite3
from ikea.base import DateBaseMeta
from ikea.fields import PKColumn, TextColumn, IntegerColumn
from ikea.generate_queries import create_table_query


class BaseModel(metaclass=DateBaseMeta):
    __tablename__ = None

    db = sqlite3.connect("ikea.db")
    db.row_factory = sqlite3.Row
    c = db.cursor()

    @classmethod
    def create_all_tables(cls):
        for cl in cls._registry:
            cls.c.execute(create_table_query(cl))

        cls.db.commit()

    @classmethod
    def create_obj(cls, **kwargs):
        query = "INSERT INTO " + cls.__tablename__ + ' !!!' + '\nVALUES ('
        columns_names = "("
        args_len = len(kwargs)
        index = 0
        for k, v in kwargs.items():
            if k not in cls._fields:
                raise AttributeError("{} is not attribute for {}".format(k, cls.__name__))
            cls._fields[k].validate_data(v)
            index += 1
            columns_names += k
            if type(v) is str:
                query += '\"' + v + '\"'
            else:
                query += str(v)
            if index < args_len:
                query += ','
                columns_names += ','
        query += ')'
        columns_names += ')'
        query = query.split('!!!')
        query = query[0] + columns_names + query[1]
        cls.c.execute(query)
        cls.db.commit()

    @classmethod
    def filter(cls, **kwargs):
        res = "SELECT *\nFROM " + cls.__tablename__ + "\nWHERE "
        args_len = len(kwargs)
        index = 0
        for k, v in kwargs.items():
            if k not in cls._fields:
                raise AttributeError("{} is not attribute for {}".format(k, cls.__name__))
            res += k + "=="
            index += 1
            if type(v) is str:
                res += '\"' + v + '\"'
            else:
                res += str(v)
            if index < args_len:
                res += ' and '
        cls.c.execute(res)
        cls.c.fetchall()
        # ...


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
