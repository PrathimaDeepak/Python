films = {
            "Finding Dory": [3, 5],
            "Bourne": [18, 5],
            "Tarzan": [15, 5],
            "Ghost Busters": [12,5]
        }

while True:
    choice = input("What film do you want to watch?: ").strip().title()
    if choice in films:
        age = int(input("how old are you?").strip())

        if age >= films[choice][0]:
            if films[choice][1] > 0:
                print("Enjoy the film")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry we are sold out")
        else:
            print("You are too young to see the film")
    else:
        print("We do not have the film yet")
    
