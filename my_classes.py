#Imports
import json
from datetime import datetime
#Klassen
class Person():
    """A simple attempt to model a person."""
    def __init__(self, first_name,last_name):
        """Initialize name and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
    def save(self):
        with open("sample.json", "w") as outfile: 
            json.dump(self.__dict__, outfile, indent = len(self.__dict__))

class Experiment():
    """A simple attempt to model an experiment."""
    def __init__(self, name, date, supervisor, subject):
        """Initialize name and age attributes."""
        self.name = name
        self.date = date
        self.supervisor = supervisor.__dict__
        self.subject = subject.__dict__
    def save(self):
        with open("sample.json", "w") as outfile: 
            json.dump(self.__dict__, outfile, indent = len(self.__dict__))

class Subject(Person):
    def __init__(self, first_name,last_name,sex, birthdate):
        #Fkt super() -> Init aus Elternklasse
        super().__init__(first_name, last_name)
        self.__birthdate = birthdate
        self.sex = sex
        self.max_hr = self.estimate_max_hr(self.sex, self.calculate_age(birthdate))
    def calculate_age(self, birthdate):
        birthdate = datetime.strptime(birthdate, "%d.%m.%Y")
        current_date = datetime.now()
        age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
        return age
    def estimate_max_hr(self, sex,age_years):
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
           max_hr_bpm = 226 - 1.0 *  age_years
        else:
           max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

class Supervisor(Person):
    def __init__(self, first_name,last_name, ID):
        #Fkt super() -> Init aus Elternklasse
        super().__init__(first_name, last_name)
        self.ID = ID