from ikea.models import BaseModel, User, Student, Movie


BaseModel.create_all_tables()

User.create_obj(name="George")
Movie.create_obj(title="Transporter")
Student.create_obj(shirt_size=15)
