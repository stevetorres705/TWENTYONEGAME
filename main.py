'''
Arguien, Torres, Hunt
CS 201
12/6/2023
Group Project #1

Algorithum:
1. call for a main loop, import random number from 2-11
2. have the computer give user a random number
3. have the computer pull a random number for itself and put it into a list for itself
4. have the two numbers pulled for the user be appended into its own list
5. display what dealer and user have, and total of numbers together
6. ask if user wants to hit (y or n)
7. if y, pick another card and add to users total
8. if over 21, game over
9. if not over 21, ask user if they want to hit again
10. if n, dealer gets another card added; once user says game is over (or n to another hit)
    then evaluate who has the closest score of 21, but not over
11. ask if user wants to play another game

Test Case (1):
Dealer Wins:
    Lets play again!
    [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
    -------------------------
    The dealer has, [6]
    The dealer has a total of 6
    You have, [3, 2]
    Your total is 5
    -------------------------
    Would you like to hit, y or n? n
    -------------------------
    The dealer has, [6, 2]
    The dealer has a total of 8
    -------------------------
    ##############################
    Dealer wins
    ##############################

Results: works as expected

Test Case (2):
You Win:
    Welcome to Black Jack! Would you like to play? (y or n) y
    [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
    -------------------------
    The dealer has, [2]
    The dealer has a total of 2
    You have, [11, 2]
    Your total is 13
    -------------------------
    Would you like to hit, y or n? n
    -------------------------
    The dealer has, [2, 7]
    The dealer has a total of 9
    -------------------------
    ##############################
    You win
    ##############################
Results: works as expected

Test Case (3):
Draw:
    Lets play again!
    [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
    -------------------------
    The dealer has, [3]
    The dealer has a total of 3
    You have, [10, 3]
    Your total is 13
    -------------------------
    Would you like to hit, y or n? n
    -------------------------
    The dealer has, [3, 10]
    The dealer has a total of 13
    -------------------------
    ##############################
    You guys tied
    ##############################
Results: works as expected
'''


import random 
def main():
    #create an empty list for the dealer
    DC = []
    DC.append(random.randint(2,11)) 
    DC.append(random.randint(2,11)) #adds number to list but keeps it hidden
    print("-"*25)
    print("The dealer has,", DC[0],", and a hidden card.")
    print("The dealer has a total of", DC[0])
    #create an empty list for the player
    PC = []
    PC.append(random.randint(2,11))
    PC.append(random.randint(2,11))
    print("You have,", PC)
    print("Your total is", sum(PC))
    print("-"*25)
    # start loop for if you want another card
    # can only reply 'y' if you are under 21, if you are over 21 the game ends
    while sum(PC) <= 21:
        PA = input("Would you like to hit, y or n? ")
        if PA == "y":
            PC.append(random.randint(2,11))
            if sum(PC) > 21:
                print("-"*25)
                print("You have,", PC)
                print("Your total is", sum(PC))
                print("You went over 21")
                print("-"*25)
                break
            else:
                print("-"*25)
                print("You have,", PC)
                print("Your total is", sum(PC))
                print("-"*25)
                exit
        elif PA == "n":
            if sum(DC) >= 17: 
                break
            elif sum(DC) <= 16:
                DC.append(random.randint(2,11))
                
            print("-"*25)
            print("The dealer has,", DC)
            print("The dealer has a total of", sum(DC))
            print("-"*25)
            # break/end the loop, go into the wining or losing statements
            break
    # print statements for whoever wins
    if sum(DC) > sum(PC):
        
        if sum(DC) <= 21:
            print("#"*30)
            print("Dealer wins")
            print("#"*30)

        elif sum(DC) > 21:
            print("#"*30)
            print("You win!")
            print("#"*30)

    elif sum(DC) == sum(PC):
        print("#"*30)
        print("You guys tied")
        print("#"*30)

    elif sum(PC) > sum(DC):
        
        if sum(PC) <= 21:
            print("#"*30)
            print("You win")
            print("#"*30)
            
        elif sum(PC) > 21:
            print("#"*30)
            print("Dealer wins")
            print("#"*30)

playAgain = input("Welcome to Black Jack! Would you like to play? (y or n) ")

while playAgain != "n":
    print("[]"*30)
    main()
    # looping the game
    playAgain = input('''
\\
Do you want to play again, y or n?
\\
''')
    if playAgain == 'n':
        break
    else:
        print("Lets play again!")
        
    
        
