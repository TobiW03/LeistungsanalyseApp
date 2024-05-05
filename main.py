import my_classes

if __name__ == "__main__":
    # Hardcoded inputs Person / Subject
    subject_firstname = str(input("Enter the firstname of the subject: ")) # "Carina" # SubjectFN
    subject_lastname = str(input("Enter the lastname of the subject: ")) # "Tilg" # SubjectLN
    sex = str(input("Enter the gender of the subject: ")) # "female" # Subject sex
    age = int(input("Enter the age of the subject: ")) #20 # Subject age

    # Hardcoded inputs Experiment
    experimentname = str(input("Enter the name of the experiment: ")) # "Experiment2024"
    date = str(input("Enter the current date [dd-mm-yyyy]: ")) # "28-04-2024"
    supervisor_first_name = str(input("Enter the firstname of the supervisor: ")) # "SupervisorFN"
    supervisor_last_name = str(input("Enter the lastname of the supervisor: ")) # "SupervisorLN"
    email = str(input("Enter the email: ")) # "email"
    # calling the class Person
    person1 = my_classes.Person(subject_firstname, subject_lastname)

    # calling the class Supervisor
    supervisor1 = my_classes.Supervisor(supervisor_first_name, supervisor_last_name)

    # calling the class Subject
    subject1 = my_classes.Subject(subject_firstname, subject_lastname, sex, age, email)
    
    # calling the class Experiment
    experiment1 = my_classes.Experiment(experimentname, date, supervisor1.__dict__, subject1.__dict__)

    # print dictionary in shell
    print(person1.__dict__)
    print(experiment1.__dict__)
    
    # save dictionaries as JSON
    my_classes.Person.save(person1)
    my_classes.Experiment.save(experiment1)

