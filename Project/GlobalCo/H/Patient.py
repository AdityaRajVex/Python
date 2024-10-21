#
#
#
from Address import Address
from Phone import Phone
from Contact import Contact
from Procedures import Procedures


class Patient(Address, Phone, Contact, Procedures):
    def __init__(self, fn, ln, address, phone_no, phone_type, e_name, e_number):
        Address.__init__(self, address)
        Phone.__init__(self, phone_no, phone_type)
        Contact.__init__(self, e_name, e_number)
        Procedures.__init__(self, )
        self.fn = fn
        self.ln = ln


