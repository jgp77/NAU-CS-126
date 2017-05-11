import random
class One_Digit_Lock():
    def __init__(self):
        self.open=False
        self.digit=random.randint(0,9)

    def change_digit(self):
        self.digit=int(input('Input a number 0 to 9. '))

    def open_lock(self):
        password=int(input('Input the current digit. '))
        if password == self.digit:
            self.open=True
            return True
        else:
            return False

class Three_Digit_Lock():
    def __init__(self):
        self.open=False
        self.digits=random.randint(0,999)

    def change_digits(self):
        self.digits=int(input('Input a three digit code. '))

    def open_lock(self):
        password=int(input('Input the current three digit code. '))
        if password == self.digits:
            self.open=True
            return True
        else:
            return False
