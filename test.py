import my_classes
import json

#main
if __name__ == "__main__":
    # Hardcoded inputs Person
    firstname = "Carina"
    lastname = "Tilg"
    sex = "female"
    age = 20

    # Hardcoded inputs Experiment
    experimentname = "Experiment1"
    date = "2021-10-10"
    supervisor = "Supervisor1"
    subject = "Subject1"

    # calling the class Person
    person1 = my_classes.Person(firstname, lastname, sex, age)
    
    # calling the class Experiment
    experiment1 = my_classes.Experiment(experimentname, date, supervisor, subject)

    # print dictionary in shell
    print(person1.__dict__)
    print(experiment1.__dict__)
    
    # save dictionaries as JSON
    my_classes.Person.save(person1)
    my_classes.Experiment.save(experiment1)



