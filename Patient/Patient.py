class Patient:
    def __init__(self, name, address, phone, contact):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__contact = contact
        self.__procedures = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_contact(self):
        return self.__contact

    def set_contact(self, contact):
        self.__contact = contact

    def add_procedure(self, procedure):
        self.__procedures.append(procedure)

    def get_procedures(self):
        return self.__procedures

    def get_bill(self):
        total_bill = sum(procedure.get_charges() for procedure in self.__procedures)
        return total_bill
