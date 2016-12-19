import os
import sys
from prettytable import PrettyTable
from hospital_data_base import HospitalDB
from populate_starting_data import populate_hospital, is_hospital_existing
from settings import COMMANDS, COMMANDS_COUNT, ACADEMIC_TITLES, INJURIES


class HospitalInterface:
    def __init__(self, hospital_name):
        hospital_name = hospital_name.replace(' ', '-')
        db_was_not_existing = not(is_hospital_existing(hospital_name))
        self.hospital = HospitalDB(hospital_name)
        # only if there was no database with this name, we populate it with data
        if db_was_not_existing:
            populate_hospital(self.hospital)

    def run(self):
        while True:
            os.system('clear')
            HospitalInterface.help_menu()
            try:
                command = int(input("command:>"))
                self.__execute_command(command)
            except ValueError:
                input("Wrong input: No such command.\nPress Enter to continue...")

    def __execute_command(self, command):
        try:
            if command == 0:
                HospitalInterface.help_menu()
            elif command == 1:
                self.hospital.list_all_patients()
            elif command == 2:
                self.hospital.list_all_doctors()
            elif command == 3:
                self.__add_patient()
            elif command == 4:
                self.__add_doctor()
            elif command == 5:
                self.__add_hospital_stay()
            elif command == 6:
                self.__update_patient_info()
            elif command == 7:
                self.__update_doctor_info()
            elif command == 8:
                self.__update_hospital_stay_info()
            elif command == 9:
                self.__delete_patient()
            elif command == 10:
                self.__deleate_doctor()
            elif command == 11:
                self.__delete_hospital_stay()
            elif command == 12:
                self.__patients_of_doctor()
            elif command == 13:
                self.__patient_by_injury()
            elif command == 14:
                self.hospital.all_doctors_diseases()
            elif command == 15:
                self.__patient_between_dates()
            elif command == 16:
                HospitalInterface.exit()
            else:
                print("Wrong input: No such command.")
        except ValueError as err:
            print("Wrong input: ", err)
        input("Press Enter to continue...")

    def __add_patient(self):
        first_name = input("First name:> ")
        last_name = input("Last name:> ")
        age = int(input("Age:> "))
        gender = input("Gender(M or F):> ")
        print("Chose which doctor...")
        self.hospital.list_all_doctors()
        doctor_id = int(input("Doctor id:> "))
        self.hospital.add_patient(first_name, last_name, age, gender, doctor_id)

    def __add_doctor(self):
        first_name = input("First name:> ")
        last_name = input("Last name:> ")
        print("Chose one from the following academic titles:")
        for ac_title in ACADEMIC_TITLES:
            print(" - ", ac_title)
        academic_title = input("Academic title:> ")
        self.hospital.add_doctor(first_name, last_name, academic_title)

    def __add_hospital_stay(self):
        startdate = input("Start date:> ")
        enddate = input("End date:> ")
        room = int(input("Room number:> "))
        print("Chose which patient...")
        self.hospital.list_all_patients()
        patient_id = int(input("Patient ID:> "))
        print("Chose one from the following injuries:")
        for injury in INJURIES:
            print(" - ", injury)
        injury = input("Injury:> ")
        self.hospital.add_hospital_stay(startdate, room, patient_id, injury, enddate)

    def __delete_patient(self):
        print("Chose which patient...")
        self.hospital.list_all_patients()
        patient_id = int(input("Patient ID:> "))
        self.hospital.delete_patient(patient_id)

    def __deleate_doctor(self):
        print("Chose which doctor...")
        self.hospital.list_all_doctors()
        doctor_id = int(input("Doctor ID:> "))
        self.hospital.delete_doctor(doctor_id)

    def __delete_hospital_stay(self):
        hosp_stay_id = int(input("Hospital stay ID:> "))
        self.hospital.delete_hospital_stay(hosp_stay_id)

    def __update_patient_info(self):
        print("Chose which patient...")
        self.hospital.list_all_patients()
        patient_id = int(input("Patient ID:> "))
        print("Set the patient data.")
        print("If you don\'t want to set some attribute, just write nothing.")
        first_name = input("First name:> ")
        last_name = input("Last name:> ")
        age = input("Age:> ")
        gender = input("Gender(M or F):> ")
        print("Chose which doctor...")
        self.hospital.list_all_doctors()
        doctor_id = input("Doctor id:> ")
        if first_name != "":
            self.hospital.update_patient_first_name(patient_id, first_name)
        if last_name != "":
            self.hospital.update_patient_last_name(patient_id, last_name)
        if age != "":
            self.hospital.update_patient_age(patient_id, int(age))
        if gender != "":
            self.hospital.update_patient_gender(patient_id, gender)
        if doctor_id != "":
            self.hospital.update_patient_doctors_id(patient_id, int(doctor_id))

    def __update_doctor_info(self):
        print("Chose which doctor...")
        self.hospital.list_all_doctors()
        doctor_id = int(input("Doctor ID:> "))
        print("Set the doctor data.")
        print("If you don\'t want to set some attribute, just write nothing.")
        first_name = input("First name:> ")
        last_name = input("Last name:> ")
        print("Chose one from the following academic titles:")
        for ac_title in ACADEMIC_TITLES:
            print(" - ", ac_title)
        academic_title = input("Academic title:> ")
        if first_name != "":
            self.hospital.update_doctor_first_name(doctor_id, first_name)
        if last_name != "":
            self.hospital.update_doctor_last_name(doctor_id, last_name)
        if ac_title != "":
            self.hospital.update_doctor_academic_title(doctor_id, academic_title)

    def __update_hospital_stay_info(self):
        hs_id = int(input("Hospital stay ID:> "))
        print("Set the hospital stay data.")
        print("If you don\'t want to set some attribute, just write nothing.")
        startdate = input("Start date:> ")
        enddate = input("End date:> ")
        room = input("Room number:> ")
        print("Chose which patient...")
        self.hospital.list_all_patients()
        patient_id = input("Patient ID:> ")
        print("Chose one from the following injuries:")
        for injury in INJURIES:
            print(" - ", injury)
        injury = input("Injury:> ")
        if startdate != "":
            self.hospital.updatate_hs_startdate(hs_id, startdate)
        if enddate != "":
            self.hospital.updatate_hs_enddate(hs_id, enddate)
        if room != "":
            self.hospital.update_hs_room(hs_id, int(room))
        if patient_id != "":
            self.hospital.update_hs_patient_id(hs_id, int(patient_id))
        if injury != "":
            self.hospital.update_hs_injury(hs_id, injury)

    def __patients_of_doctor(self):
        print("Chose which doctor...")
        self.hospital.list_all_doctors()
        doctor_id = int(input("Doctor ID:> "))
        self.hospital.all_patients_by_doctor(doctor_id)

    def __patient_by_injury(self):
        print("Chose one from the following injuries:")
        for injury in INJURIES:
            print(" - ", injury)
        injury = input("Injury:> ")
        self.hospital.all_patients_with_injury(injury)

    def __patient_between_dates(self):
        startdate = input("Start date:> ")
        enddate = input("End date:> ")
        self.hospital.all_patients_between_dates(startdate, enddate)

    @staticmethod
    def help_menu():
        print("You can use the folowing commands,")
        print("by entering the command\' number")
        table = PrettyTable()
        table.field_names = ["Command", "Number"]
        for i in range(COMMANDS_COUNT):
            table.add_row([COMMANDS[i], str(i)])
        print(table)

    @staticmethod
    def exit():
        sys.exit()
