known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Greg", "Harry"]

print(len(known_users))

while True:
    print("Hi.. My name is Travis")
    name = input("What is your name?").strip().capitalize()
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n) ?: ").strip().lower()
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No Problem! I did not want you to leave anyway")
            
    else:
        print("Hmmm I dont think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?:").strip().lower()
        if add_me == "y":
            known_users.append(name);
        elif add_me == "n":
            print("Ok See you later")
            
