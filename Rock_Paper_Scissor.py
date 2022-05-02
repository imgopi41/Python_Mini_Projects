import random   #importing random module to make random choice.

def menu(): #defining a function
    while True: #applying while loop for try-again block

        user = input(str("\nEnter your choice(Rock,Paper,Scissor): "))  #asking user choice
        available_action = ["Rock","Paper","Scissors"]  #providing avaiable choices
        computer = random.choice(available_action)  #applying random module and choice function for the user input

        print("\nYour Choice is {}\nComputer Choice is {}".format(user,computer))   #displaying user's choice and computer's choice 

        if user == computer:    #applying if-condition if user and computer's choice is same then "Tie game" message display's on output screen
            print("Tie game...!")   #user message

        elif user =="Rock": 
            if computer =="Paper":
                print("You lost")
            else:
                print("You win")
        elif user=="Paper":
            if computer=="Scissor":
                print("you lost")
            else:
                print("You win")
        elif user=="Scissor":
            if computer=="Paper":
                print("You win")
            else:
                print("You lost")


        again = input("\nDo you want play again?(Y/N): ")   #try-again\play-again block
        if again.upper() == 'Y':    #converts lowercase to uppercase.
            menu()  #if user types "y" function is going to repeat again
            print('Thank you')  #if not "Thank you message is displayed"
        break   #breaks when user types "n".
menu()  #out of main function.



