import os
import sys
from hospital_data_base import HospitalDB
from populate_starting_data import populate_hospital, is_hospital_existing
from settings import COMMANDS_COUNT
from helper_prints import(
                        print_help_menu,
                        print_for_updates,
                        print_choose_injuries,
                        print_choose_academic_title)


class HospitalInterface:
    def __init__(self, hospital_name):
        hospital_name = hospital_name.replace(' ', '-')
        db_was_not_existing = not(is_hospital_existing(hospital_name))
        self.hospital = HospitalDB(hospital_name)
        self.commands = self.__make_function_dict()
        # only if there was no database with this name, we populate it with data
        if db_was_not_existing:
            populate_hospital(self.hospital)

    def run(self):
        while True:
            os.system('clear')
            HospitalInterface.help_menu()
            try:
                command = int(input("command:> "))
                self.__execute_command(command)
            except ValueError:
                input('''Wrong input: No such command.
                        Press Enter to continue...''')

    def __execute_command(self, command):
        try:
            if command in range(COMMANDS_COUNT):
                self.commands[command]()
            else:
                print("Wrong input: No such command.")
        except ValueError as err:
            print("Wrong input: ", err)
        input("Press Enter to continue...")

    def __read_patient_id(self):
        print("Choose which patient...")
        self.hospital.list_all_patients()
        patient_id = input("Patient ID:> ")
        return patient_id

    def __read_doctor_id(self):
        print("Choose which doctor...")
        self.hospital.list_all_doctors()
        doctor_id = input("Doctor ID:> ")
        return doctor_id

    def __read_patient_data(self):
        first_name = input("First name:> ")
        last_name = input("Last name:> ")
        age = input("Age:> ")
        gender = input("Gender(M or F):> ")
        doctor_id = self.__read_doctor_id()
        return {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "gender": gender,
                "doctor_id": doctor_id}

    def __read_doctor_data(self):
        first_name = input("First name:> ")
        last_name = input("Last name:> ")
        print_choose_academic_title()
        academic_title = input("Academic title:> ")
        return {
                "first_name": first_name,
                "last_name": last_name,
                "acc_title": academic_title}

    def __read_hospital_stay_data(self):
        startdate = input("Start date:> ")
        enddate = input("End date:> ")
        room = input("Room number:> ")
        patient_id = self.__read_patient_id()
        print_choose_injuries()
        injury = input("Injury:> ")
        return {
                "startdate": startdate,
                "enddate": enddate,
                "room": room,
                "patient_id": patient_id,
                "injury": injury}

    def __add_patient(self):
        data = self.__read_patient_data()
        self.hospital.add_patient(
                                data["first_name"],
                                data["last_name"],
                                int(data["age"]),
                                data["gender"],
                                int(data["doctor_id"]))

    def __add_doctor(self):
        data = self.__read_doctor_data()
        self.hospital.add_doctor(
                                data["first_name"],
                                data["last_name"],
                                data["acc_title"])

    def __add_hospital_stay(self):
        data = self.__read_hospital_stay_data()
        self.hospital.add_hospital_stay(
                                        data["startdate"],
                                        int(data["room"]),
                                        int(data["patient_id"]),
                                        data["injury"],
                                        data["enddate"])

    def __delete_patient(self):
        patient_id = int(self.__read_patient_id())
        self.hospital.delete_patient(patient_id)

    def __delete_doctor(self):
        doctor_id = int(self.__read_doctor_id())
        self.hospital.delete_doctor(doctor_id)

    def __delete_hospital_stay(self):
        hosp_stay_id = int(input("Hospital stay ID:> "))
        self.hospital.delete_hospital_stay(hosp_stay_id)

    def __update_patient_info(self):
        patient_id = str(self.__read_patient_id())
        print_for_updates("patient")
        data = self.__read_patient_data()
        self.__execute_update_patient(
                                    int(patient_id),
                                    data["first_name"],
                                    data["last_name"],
                                    data["age"],
                                    data["gender"],
                                    data["doctor_id"])

    def __update_doctor_info(self):
        doctor_id = self.__read_doctor_id()
        print_for_updates("doctor")
        data = self.__read_doctor_data()
        self.__execute_update_doctor(
                                    int(doctor_id),
                                    data["first_name"],
                                    data["last_name"],
                                    data["acc_title"])

    def __update_hospital_stay_info(self):
        hs_id = int(input("Hospital stay ID:> "))
        print_for_updates("hospital stay")
        data = self.__read_hospital_stay_data()
        self.__execute_update_hs_stay(
                                    hs_id,
                                    data["startdate"],
                                    data["enddate"],
                                    data["room"],
                                    data["patient_id"],
                                    data["injury"])

    def __execute_update_patient(self, patient_id, first_name, last_name, age, gender, dr_id):
        if first_name != "":
            self.hospital.update_patient_first_name(patient_id, first_name)
        if last_name != "":
            self.hospital.update_patient_last_name(patient_id, last_name)
        if age != "":
            self.hospital.update_patient_age(patient_id, int(age))
        if gender != "":
            self.hospital.update_patient_gender(patient_id, gender)
        if dr_id != "":
            self.hospital.update_patient_doctors_id(patient_id, int(dr_id))

    def __execute_update_doctor(self, dr_id, first_name, last_name, acc_title):
        if first_name != "":
            self.hospital.update_doctor_first_name(dr_id, first_name)
        if last_name != "":
            self.hospital.update_doctor_last_name(dr_id, last_name)
        if acc_title != "":
            self.hospital.update_doctor_academic_title(dr_id, acc_title)

    def __execute_update_hs_stay(self, hs_id, startdate, enddate, room, pat_id, injury):
        if startdate != "":
            self.hospital.updatate_hs_startdate(hs_id, startdate)
        if enddate != "":
            self.hospital.updatate_hs_enddate(hs_id, enddate)
        if room != "":
            self.hospital.update_hs_room(hs_id, int(room))
        if pat_id != "":
            self.hospital.update_hs_patient_id(hs_id, int(pat_id))
        if injury != "":
            self.hospital.update_hs_injury(hs_id, injury)

    def __patients_of_doctor(self):
        doctor_id = int(self.__read_doctor_id())
        self.hospital.all_patients_by_doctor(doctor_id)

    def __patients_by_injury(self):
        print_choose_injuries()
        injury = input("Injury:> ")
        self.hospital.all_patients_with_injury(injury)

    def __patients_between_dates(self):
        startdate = input("Start date:> ")
        enddate = input("End date:> ")
        self.hospital.all_patients_between_dates(startdate, enddate)

    def __make_function_dict(self):
        return {
                0: HospitalInterface.help_menu,
                1: self.hospital.list_all_patients,
                2: self.hospital.list_all_doctors,
                3: self.__add_patient,
                4: self.__add_doctor,
                5: self.__add_hospital_stay,
                6: self.__update_patient_info,
                7: self.__update_doctor_info,
                8: self.__update_hospital_stay_info,
                9: self.__delete_patient,
                10: self.__delete_doctor,
                11: self.__delete_hospital_stay,
                12: self.__patients_of_doctor,
                13: self.__patients_by_injury,
                14: self.hospital.all_doctors_diseases,
                15: self.__patients_between_dates,
                16: HospitalInterface.exit}

    @staticmethod
    def help_menu():
        print_help_menu()

    @staticmethod
    def exit():
        sys.exit()
