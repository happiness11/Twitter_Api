def show_menu():
    print("menu")
    print()
    print("1. Add a person")
    print("2. View People")
    print("3. Stats")
    print("4. Exit")
    option = input("Enter Option\n")
    return option
    
show_menu()

def program_loop():
   while  True:
       option = show_menu()
       if option == 4:
           break
       else:
           print("invalid option")
program_loop()