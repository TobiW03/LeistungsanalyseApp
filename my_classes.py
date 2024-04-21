import json

# create a class Person
class Person():
    # constructor: with attributes of the parameters from my_function.py
    def __init__(self, fist_name, last_name, sex, age):
        self.first_name = fist_name
        self.last_name = last_name  
        self.sex = sex
        self.age = age
        self.estimate_max_hr = self.estimate_max_hr(sex, age)
    
    # method: estimate the maximum heart rate
    def estimate_max_hr(self, sex, age_years):
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
    
    # method: save class attributes as a dictionary as JSON
    def save(self):
        # create a dictionary of the class attributes
        with open("person.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)
        
# create a class Experiment
class Experiment():
    # constructor: with attributes of the parameters from my_function.py
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
    
    # method: save class attributes as a dictionary as JSON
    def save(self):
        # create a dictionary of the class attributes
        with open("experiment.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)       
