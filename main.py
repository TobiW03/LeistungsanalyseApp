import json 
import my_classes


#main
if __name__ == "__main__":
    # Userinputs Person
    firstname = str(input("Enter your firstname: ")) # "Carina"
    lastname = str(input("Enter your lastname: ")) # "Tilg"
    sex = str(input("Enter your gender [male/female]: ")) # "female"
    age = int(input("Enter your age: ")) # 20

    # Userinputs Experiment
    experimentname = str(input("Enter the name of the experiment: ")) # "Experiment1"
    date = str(input("Enter the current date [dd-mm-yyyy]: ")) # "20-04-2024"
    supervisor = str(input("Enter the name of the supervisor: ")) # "Supervisor1"
    subject = str(input("Enter the name of the subject of the experiment: ")) # "Subject1"

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
