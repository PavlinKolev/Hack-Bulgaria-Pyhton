from hospital_interface import HospitalInterface


def main():
    hospital_name = input("Hospital name: ")
    interface = HospitalInterface(hospital_name)
    interface.run()


if __name__ == '__main__':
    main()
