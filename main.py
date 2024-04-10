from my_functions import estimate_max_hr, build_person, build_experiment
#main
if __name__ == "__main__":
    #MaxHR
    print("1. Proband")
    print(estimate_max_hr(25,"male"))
    print("2. Probandin")
    print(estimate_max_hr(47,"female"))
    #BuildPerson
    print(build_person('Tobias','Wannenmacher','male',21))
    #BuildExperiment
    print(build_experiment('MGST23','2024-04-03','TW','MGST'))
