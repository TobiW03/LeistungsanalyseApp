import json

# create a class Person
class Person():
    # constructor
    def __init__(self, fist_name, last_name):
        self.first_name = fist_name
        self.last_name = last_name

    # method: save class attributes as a dictionary as JSON
    def save(self):
        # create a dictionary of the class attributes
        with open("person.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)

# create sub-class Supervisor of the class Person
class Supervisor(Person):
    # constructor
    def __init__(self, fist_name, last_name):
        super().__init__(fist_name, last_name)
    
# create sub-class Subject of the class Person
class Subject(Person):
    # constructor
    def __init__(self, fist_name, last_name, sex, age):
        super().__init__(fist_name, last_name)
        self.sex = sex
        # hidden attribute: __age
        self.__age = age
        self.estimate_max_hr = self.estimate_max_hr(sex, age)

    # method: estimate the maximum heart rate
    def estimate_max_hr(self, sex, age_years):
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

# create a class Experiment
class Experiment(): 
    # constructor
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