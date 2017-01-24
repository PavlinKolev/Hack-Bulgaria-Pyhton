from ikea.models import BaseModel, User, Student, Movie


BaseModel.create_all_tables()

User.create_obj(name="George", age=20)
Movie.create_obj(title="Transporter", year=2004, budget=15000000)


User.filter(age=20)
Movie.filter(title="Transporter")
