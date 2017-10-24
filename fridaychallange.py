
// #friday challange solution
// https://richardadalton.github.io/HTML_Notes/practical_python/file_io/07_walkthrough_quiz_game.html
def show_menu():
    print("Menu")
    print()
    print("1. Add a person")
    print("2. View People")
    print("3. Stats")
    print("4. Exit")
    option = input("Enter Option\n>")
    return option
  
def add_a_person():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    team = input("Enter team: ")
    
    line = first_name + "," + last_name + "," + age + "," + team + "\n"
    
    with open("people.txt", "a") as people_file:
        people_file.write(line)

def load_people():
    people = []
    with open("people.txt", "r") as people_file:
        lines = people_file.read().splitlines()
        for line in lines:
            fields = line.split(",")
            people.append(fields)
    return people    
  
  
def view_people():
    people = load_people()
    print("List Of People")  
    for person in people: 
        print ("{1}, {0} ({2}), Team: {3}".format(person[0], person[1], person[2], person[3]))
    
def view_stats():
    people = load_people()
    
    team_lists = {}
    
    total_age = 0
    for person in people:
        total_age += int(person[2])
        list = team_lists.get(person[3], [])
        list.append(person)
        team_lists[person[3]] = list
    
    average_age = total_age / len(people)
    
    print("The number of people is {0}".format(len(people)))
    print("The average age is {0}".format(average_age))
    
    for team, players in team_lists.items():
        print(team)
        print(players)

def program_loop():
    while True:
        option = show_menu()
        
        if option == "1":
            add_a_person()
        elif option == "2":
            view_people()
        elif option == "3":
            view_stats()
        elif option == "4":
            break
        else:
            print("Invalid Option")
        
program_loop()
        
        