import sqlite3
from prettytable import PrettyTable
from queries import *
from settings import *


class HospitalDB:
    def __init__(self, name=DEFAULT_HOSPITAL_NAME):
        self.db = sqlite3.connect(name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.__create_doctors_table()
        self.__create_patients_table()
        self.__create_hospital_stay_table()
        self.set_patients_ids()
        self.set_doctors_ids()
        self.set_hospital_ids()

    def set_patients_ids(self):
        self.cursor.execute(LIST_PATIENT_IDS)
        patients = self.cursor.fetchall()
        self.patients_ids = [p["ID"] for p in patients]

    def set_doctors_ids(self):
        self.cursor.execute(LIST_DOCTOR_IDS)
        doctors = self.cursor.fetchall()
        self.doctors_ids = [d["ID"] for d in doctors]

    def set_hospital_ids(self):
        self.cursor.execute(LIST_HOSPITAL_STAY_IDS)
        hospital_stays = self.cursor.fetchall()
        self.hospital_stay_ids = [hs["ID"] for hs in hospital_stays]

    def __create_patients_table(self):
        # self.cursor.execute(DROP_PATIENT_TABLE)
        # self.db.commit()
        self.cursor.execute(CREATE_PATIENT_TABLE)
        self.db.commit()

    def __create_doctors_table(self):
        # self.cursor.execute(DROP_DOCTOR_TABLE)
        # self.db.commit()
        self.cursor.execute(CREATE_DOCTOR_TABLE)
        self.db.commit()

    def __create_hospital_stay_table(self):
        # self.cursor.execute(DROP_HOSPITAL_STAY_TABLE)
        # self.db.commit()
        self.cursor.execute(CREATE_HOSPITAL_STAY_TABLE)
        self.db.commit()

    def add_patient(self, first_name, last_name, age, gender, doctor_id):
        self.__validate_patient_data(age, gender, doctor_id)
        self.cursor.execute(ADD_PATIENT,
                            (first_name, last_name, age, gender, doctor_id))
        self.db.commit()
        self.patients_ids.append(self.cursor.lastrowid)

    def add_doctor(self, first_name, last_name, academic_title):
        HospitalDB.check_academic_title(academic_title)
        self.cursor.execute(ADD_DOCTOR, (first_name, last_name, academic_title))
        self.db.commit()
        self.doctors_ids.append(self.cursor.lastrowid)

    def add_hospital_stay(self, startdate, room, patient_id, injury, enddate=None):
        HospitalDB.check_injury(injury)
        self.__check_patient_id(patient_id)
        self.cursor.execute(ADD_HOSPITAL_STAY,
                            (startdate, enddate, room, injury, patient_id))
        self.db.commit()
        self.hospital_stay_ids.append(self.cursor.lastrowid)

    def delete_patient(self, patient_id):
        self.__check_patient_id(patient_id)
        self.cursor.execute(DELETE_PATIENT, (patient_id,))
        self.db.commit()

    def delete_doctor(self, doctor_id):
        self.__check_doctor_id(doctor_id)
        self.cursor.execute(DELETE_DOCTOR, (doctor_id,))
        self.db.commit()

    def delete_hospital_stay(self, hospital_stay_id):
        self.__check_hs_id(hs_id)
        self.cursor.execute(DELETE_HOSPITAL_STAY, (hospital_stay_id,))
        self.db.commit()

    def list_all_patients(self):
        self.cursor.execute(LIST_ALL_PATIENTS)
        self.__print_patients_after_query()

    def list_all_doctors(self):
        self.cursor.execute(LIST_ALL_DOCTORS)
        doctors = self.cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Id", "Firstname", "Lastname", "Academic title"]
        for d in doctors:
            table.add_row([d[0], d[1], d[2], d[3]])
        print(table)

    def __print_patients_after_query(self):
        patients = self.cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["ID", "Fistname", "Lastname", "Age"]
        for p in patients:
            table.add_row([p[0], p[1], p[2], p[3]])
        print(table)

    def update_patient_first_name(self, patient_id, first_name):
        self.__check_patient_id(patient_id)
        self.cursor.execute(UPDATE_DOCTOR_FIRSTNAME, (first_name, patient_id))
        self.db.commit()

    def update_patient_last_name(self, patient_id, last_name):
        self.__check_patient_id(patient_id)
        self.cursor.execute(UPDATE_DOCTOR_LASTNAME, (last_name, patient_id))
        self.db.commit()

    def update_patient_age(self, patient_id, age):
        HospitalDB.check_patient_age()
        self.__check_patient_id(patient_id)
        self.cursor.execute(UPDATE_PATIENT_AGE, (age, patient_id))
        self.db.commit()

    def update_patient_doctors_id(self, patient_id, doctor_id):
        self.__check_patient_id(patient_id)
        self.__check_doctor_id(doctor_id)
        self.cursor.execute(UPDATE_PATIENT_DOCTOR_ID, (doctor_id, patient_id))
        self.db.commit()

    def update_doctor_first_name(self, doctor_id, first_name):
        self.__check_doctor_id(doctor_id)
        self.cursor.execute(UPDATE_DOCTOR_FIRSTNAME, (first_name, doctor_id))
        self.db.commit()

    def update_doctor_last_name(self, doctor_id, last_name):
        self.__check_doctor_id(doctor_id)
        self.cursor.execute(UPDATE_DOCTOR_LASTNAME, (last_name, doctor_id))
        self.db.commit()

    def update_doctor_academic_title(self, doctor_id, academic_title):
        HospitalDB.check_academic_title(academic_title)
        self.__check_doctor_id(doctor_id)
        self.cursor.execute(UPDATE_DOCTOR_ACADEMIC_TITLE, (academic_title, doctor_id))
        self.db.commit()

    def updatate_hs_startdate(self, hs_id, startdate):
        self.__check_hs_id(hs_id)
        self.cursor.execute(UPDATE_HS_STARTDATE, (startdate, hs_id))
        self.db.commit()

    def updatate_hs_enddate(self, hs_id, enddate):
        self.__check_hs_id(hs_id)
        self.cursor.execute(UPDATE_HS_ENDDATE, (enddate, hs_id))
        self.db.commit()

    def update_hs_room(self, hs_id, room):
        self.__check_hs_id(hs_id)
        self.cursor.execute(UPDATE_HS_ROOM, (room, hs_id))
        self.db.commit()

    def update_hs_injury(self, hs_id, injury):
        HospitalDB.check_injury(injury)
        self.__check_hs_id(hs_id)
        self.cursor.execute(UPDATE_HS_INJURY, (injury, hs_id))
        self.db.commit()

    def update_hs_patient_id(self, hs_id, patient_id):
        self.__check_hs_id(hs_id)
        self.__check_patient_id(patient_id)
        self.cursor.execute(UPDATE_HS_PATIENT_ID, (patient_id, hs_id))
        self.db.commit()

    def all_patients_by_doctor(self, doctor_id):
        self.__check_doctor_id(doctor_id)
        self.cursor.execute(LIST_PATIENTS_OF_DOCTOR, (doctor_id,))
        self.__print_patients_after_query()

    def all_patients_with_injury(self, injury):
        HospitalDB.check_injury(injury)
        self.cursor.execute(PATIENTS_GROUP_BY_INJURY, (injury,))
        self.__print_patients_after_query()

    def all_patients_between_dates(self, startdate, enddate):
        # TODO: validation for dates
        self.cursor.execute(PATIENTS_BETWEEN_DATES, (startdate, enddate))
        self.__print_patients_after_query()

    def __validate_patient_data(self, age, gender, doctor_id):
        HospitalDB.check_patient_age(age)
        HospitalDB.check_patient_gender(gender)
        self.__check_doctor_id(doctor_id)

    def __check_patient_id(self, patient_id):
        if patient_id not in self.patients_ids:
            raise ValueError("There is no patient with this ID.")

    def __check_doctor_id(self, doctor_id):
        if doctor_id not in self.doctors_ids:
            raise ValueError("There is no doctor with this id.")

    def __check_hs_id(self, hs_id):
        if hs_id not in self.hospital_stay_ids:
            raise ValueError("There is no hospidatl stay with this id.")

    @staticmethod
    def check_patient_age(age):
        if type(age) is not int:
            raise TypeError("Type of patients age must be int.")
        if age < 0 or age > 120:
            raise ValueError("Not a valid patient age.")

    @staticmethod
    def check_patient_gender(gender):
        if type(gender) is not str:
            raise TypeError("Type of gender must be string.")
        if gender != 'M' and gender != 'F':
            raise ValueError("Gender must be \'M\' or \'F\'.")

    @staticmethod
    def check_injury(injury):
        if injury not in INJURIES:
            raise ValueError("Unrecognised injury.")

    @staticmethod
    def check_academic_title(academic_title):
        if academic_title not in ACADEMIC_TITLES:
            raise ValueError("Unrecognised academic title.")
