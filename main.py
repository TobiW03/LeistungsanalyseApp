import json 
from my_functions import estimate_max_hr, build_person, build_experiment
#main
if __name__ == "__main__":
    #Userinputs
    firstname = str(input('Please enter your firstname: '))
    lastname = str(input('Please enter your lastname: '))
    sex = str(input('Please enter your gender as male or female: '))
    age = int(input('Please enter your age: '))
    #create person
    person1 = build_person(firstname,lastname,sex,age)
    print(person1)
    #maxHR
    person1_maxHR = estimate_max_hr(age,sex)
    print(person1_maxHR)
    #build experiment
    experimentname = str(input('Please enter the name of the experiment: '))
    date = str(input('Please enter the current date: '))
    supervisor = str(input('Please enter the name of the supervisor: '))
    subject = str(input('Please enter the name of the subject of the experiment: '))
    #creation of experiment
    experiment1 = build_experiment(experimentname,date,supervisor,subject)

# Convert and write JSON object to file
with open("sample.json", "a") as outfile: 
    json.dump(experiment1, outfile)
    json.dump(person1, outfile)
