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
    
def ask_questions():
    with open("question.txt") as f:
        questions = f.read().split("\n")[:-1]
        
    score =0
    
    for q in questions:
        question, answer = q.split("|")
        # qlist = q.split("|")[0]
        # answer = q.split("|")[1]
        # print(qlist)
        # print(answer)
        guess=input(question) 
        
        if guess == answer:
            score+=1
    print("You scored {0}".format(score))        
        
    
    
    

def add_a_question():
    question = input("Enter a question: ")
    answer = input("Ok then tell me, "+ question +": ")
    
    with open("question.txt","a") as f:
        line = question + "|" + answer +"\n"
        f.write(line)
    
    
    
while True:
    option = show_menu()
    
    
    if option =="1":
        ask_questions()
    if option =="2":
        add_a_question()
        
    if option == "3":
        break

   