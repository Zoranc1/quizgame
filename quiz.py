def show_menu():
    print("Quiz game")
    print("_____")
    print()
    print("1. Run Quiz")
    print("2. Enter a Question")
    print("3. Exit")
    print()

    option = input("Enter option: ")
    return option

def add_a_quastion():
    quastion = input("Enter a quastion: ")
    answer = input("Ok then tell me, "+ quastion +": ")
    
    with open("question.txt","a") as f:
        line = quastion + "|" + answer +"\n"
        f.write(line)
    
    
    
while True:
    option = show_menu()
    
    
    if option =="1":
        print("You picked run quiz")
    if option =="2":
        add_a_quastion()
        
    if option == "3":
        break

   