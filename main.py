import json 
import my_classes
#main
if __name__ == "__main__":
    #Userinputs
    print("Inputs for subject: ")
    firstname = str(input('Please enter your firstname: '))
    lastname = str(input('Please enter your lastname: '))
    sex = str(input('Please enter your gender as male or female: '))
    birthdate = str(input('Please enter your birthdate in the following style - dd.mm.yyyy: '))
    #Supervisor
    print("Inputs for supervisor: ")
    firstnamesup = str(input('Please enter the firstname of the supervisor: '))
    lastnamesup = str(input('Please enter the lastname of the supervisor: '))
    ID = int(input('Please enter the ID of the supervisor: '))
    #Experiment
    print("Inputs for experiment: ")
    experimentname = str(input('Please enter the name of the experiment: '))
    date = str(input('Please enter the current date: '))
    #Objekterstellung
    Subject1 = my_classes.Subject(firstname,lastname,sex,birthdate)
    Supervisor1 = my_classes.Supervisor(firstnamesup,lastnamesup,ID)
    Experiment1 = my_classes.Experiment(experimentname,date,Supervisor1,Subject1)
    print(Subject1.__dict__)
    print(Supervisor1.__dict__)
    print(Experiment1.__dict__)
    my_classes.Supervisor.save(Supervisor1)
    my_classes.Subject.save(Subject1)
    my_classes.Experiment.save(Experiment1)