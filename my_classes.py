import json

import requests

# create a class Person
class Person():
    # constructor
    def __init__(self, fist_name, last_name):
        self.first_name = fist_name
        self.last_name = last_name

    # methode to create a new person on the webserver
    def put(self):
        data = {'first_name': self.first_name}  # create a dictionary with the first name
        response = requests.post('http://localhost:5000/person/', json=data) # send a POST request to the webserver
        return response.json()

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
    def __init__(self, fist_name, last_name, sex, age, email):
        super().__init__(fist_name, last_name)
        self.sex = sex
        # hidden attribute: __age
        self.__age = age
        self.estimate_max_hr = self.estimate_max_hr(sex, age)
        self.email = email

    def update_email(self):
        data = {"name": self.first_name, "email": self.email}
        
        data_json = json.dumps(data)
        response = requests.post("http://127.0.0.1:5000/person/Testname2", data=data_json)
        return response.json()
        

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