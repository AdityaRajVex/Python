#
#
#
class Phone:
    def __init__(self, phone_no, phone_type):
        self.__phone_no = phone_no
        self.__phone_type = phone_type

    # sets
    def set_phone_no(self, phone_no):
        self.__phone_no = phone_no

    def set_phone_type(self, phone_type):
        self.__phone_type = phone_type

    # gets
    def get_phone_no(self):
        return self.__phone_no

    def get_phone_type(self):
        return self.__phone_type

    def __str__(self):
        return (f'Phone number: {self.__phone_no}'
                f'Phone type: {self.__phone_type}')