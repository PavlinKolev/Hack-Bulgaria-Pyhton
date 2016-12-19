import os
from hospital_data_base import HospitalDB


def populate_hospital(hospital):
    if type(hospital) is not HospitalDB:
        raise TypeError("Type of hospitalital must be hospitalitalDB")

    hospital.add_doctor("Georgi", "Atanasov", 'Allergist')
    hospital.add_doctor("Doctor", "Radeva", 'Gynecologist')
    hospital.add_doctor("Mariq", "Slavcheva", 'Urologist')
    hospital.add_doctor("Ivan", "Ivanov", 'Pediatrician')
    hospital.add_doctor("Doctor", "House", 'Oncologist')

    hospital.add_patient("Ivan", "Georgiev", 20, "M", 1)
    hospital.add_patient("Ivanka", "Georgieva", 25, "F", 2)
    hospital.add_patient("Pesho", "Georgiev", 19, "M", 3)
    hospital.add_patient("Bojko", "Petrov", 22, "M", 4)
    hospital.add_patient("Petq", "Hristova", 23, "F", 5)
    hospital.add_patient("Martin", "Georgiev", 20, "M", 1)
    hospital.add_patient("Baba", "Zlata", 85, "F", 2)
    hospital.add_patient("Dqdo", "Ioco", 89, "M", 3)
    hospital.add_patient("Lelq", "Goshka", 45, "F", 4)
    hospital.add_patient("Bat", "Georgi", 28, "M", 5)

    hospital.add_hospital_stay("2016-12-16", 105, 1, "Cancer", "2016-12-20")
    hospital.add_hospital_stay("2016-12-14", 222, 2, "Diabetes", "2016-12-22")
    hospital.add_hospital_stay("2016-12-15", 308, 3, "Eczema", "2017-01-10")
    hospital.add_hospital_stay("2016-12-23", 404, 4, "Epilepsy", "2016-12-27")
    hospital.add_hospital_stay("2016-12-16", 105, 5, "Cancer", "2016-12-26")
    hospital.add_hospital_stay("2016-12-22", 105, 6, "Leukemia", "2016-12-25")
    hospital.add_hospital_stay("2016-12-10", 222, 7, "Lupus", "2016-12-15")
    hospital.add_hospital_stay("2016-12-31", 777, 8, "Hepatitis", "2017-12-20")
    hospital.add_hospital_stay("2017-01-05", 155, 9, "Leukemia", "2017-01-20")
    hospital.add_hospital_stay("2016-12-06", 355, 10, "Laryngitis", "2016-12-22")


def is_hospital_existing(hospital_name):
    file_path = os.getcwd() + '/' + hospital_name + '.db'
    if os.path.isfile(file_path):
        return True
    return False
