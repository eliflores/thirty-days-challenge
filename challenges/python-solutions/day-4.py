class Person:
    def __init__(self, initial_age):
        if initial_age < 0:
            print("This person is not valid, setting age to 0.")
        self.age = initial_age

    def am_i_old(self):
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def year_passes(self):
        self.age += 1
