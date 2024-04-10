import json 
import my_classes
#main
if __name__ == "__main__":
    #Userinputs
    firstname = str(input('Please enter your firstname: '))
    lastname = str(input('Please enter your lastname: '))
    sex = str(input('Please enter your gender as male or female: '))
    age = int(input('Please enter your age: '))
    #build experiment
    experimentname = str(input('Please enter the name of the experiment: '))
    date = str(input('Please enter the current date: '))
    supervisor = str(input('Please enter the name of the supervisor: '))
    subject = str(input('Please enter the name of the subject of the experiment: '))


    #Objekterstellung
    Person1 = my_classes.Person(firstname,lastname,sex,age) 
    Experiment1 = my_classes.Experiment(experimentname,date,supervisor,subject)
    print(Person1.__dict__)
    print(Experiment1.__dict__)
    my_classes.Person.save(Person1)
    my_classes.Experiment.save(Experiment1)