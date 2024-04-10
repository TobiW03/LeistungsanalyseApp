#Imports
import json
#Klassen
class Person():
    """A simple attempt to model a person."""
    def __init__(self, first_name,last_name,sex, age):
        """Initialize name and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.estimated_max_hr = self.estimate_max_hr(sex, age)
    def estimate_max_hr(self, sex,age_years):
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
    def save(self):
        with open("sample.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)

class Experiment():
    """A simple attempt to model an experiment."""
    def __init__(self, name, date, supervisor, subject):
        """Initialize name and age attributes."""
        self.name = name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
    def save(self):
        with open("sample.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)