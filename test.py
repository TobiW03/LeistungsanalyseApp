import my_classes

if __name__ == "__main__":
    # Example of using the Person object and the put() method
    person = my_classes.Person("Carina", "Tilg")
    response = person.put()
    print("New Person:", response)

    # Example of using the Subject object and the update_email() method
    subject = my_classes.Subject("C", "T", "female", 20, "carina@blabla.com")
    new_email = "carina_tilg@blabla.com"
    response = subject.update_email(new_email)
    print("new email:", response)