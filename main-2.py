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
def main(money):
    #create an empty list for the dealer
    DC = []
    DC.append(random.randint(2,11)) 
    DC.append(random.randint(2,11))#adds number to list
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
    while sum(PC) <= 21 and sum(DC) <= 21:
        PA = input("Would you like to hit, y or n? ")
        if PA == "y":
            PC.append(random.randint(2,11))
            if sum(PC) > 21:
                print("[]"*25)
                print(f"You got {PC[-1]}")
                print("You have,", PC)
                print("Your total is", sum(PC))
                print("You went over 21")
                print("[]"*25)
            else:
                print("[]"*25)
                print(f"You got {PC[-1]}")
                print("You have,", PC)
                print("Your total is", sum(PC))
                print("[]"*25)
                
                
        elif PA == "n":
            while sum(DC) <= 21: 
                if sum(DC) >= 17: 
                    print("The dealer will not take anymore cards!")
                    break
                elif sum(DC) <= 16:
                    DC.append(random.randint(2,11))
                    print("The dealer pulled a", DC[-1])
                    
            print("[]"*25)
            print("The dealer has,", DC[ 0 : (len(DC)) ] )
            print("The dealer has a total of", sum(DC))
            print("[]"*25)
            # break/end the loop, go into the wining or losing statements
            break
    # print statements for whoever wins
    if sum(DC) > sum(PC):
        
        if sum(DC) <= 21:
            print("#"*30)
            print("You have,", PC)
            print("Your total is", sum(PC))
            print("The dealer had,", DC[ 0 : (len(DC)) ] )
            print("The dealer has a total of", sum(DC))
            print("Dealer wins")
            print("#"*30)
            money *= -1
        elif sum(DC) > 21:
            print("-"*30)
            print("The dealer had,", DC[ 0 : (len(DC)) ] )
            print("The dealer has a total of", sum(DC))
            print("You win!")
            print("-"*30)
            money *= 2 

    #if player and dealer have the same amount 
    elif sum(DC) == sum(PC):
        
        if sum(PC) <= 21:
            print("="*30)
            print("The dealer had,", DC[ 0 : (len(DC)) ] )
            print("The dealer has a total of", sum(DC))
            print("You guys tied")
            print("="*30)

    #if player has higher than the dealer
    elif sum(PC) > sum(DC):
        #player wins due to having the higher number and lower than or equal to 21
        if sum(PC) <= 21:
            print("-"*30)
            print("You have,", PC)
            print("Your total is", sum(PC))
            print("The dealer had,", DC[ 0 : (len(DC)) ] )
            print("The dealer has a total of", sum(DC))
            print("You win")
            print("-"*30)
            money *= 2
            
            
        #if player busts, it doesn't matter if the dealer busts 
        elif sum(PC) > 21:
            print("#"*30)
            print("You have,", PC)
            print("Your total is", sum(PC))
            print("The dealer had,", DC[ 0 : (len(DC)) ] )
            print("The dealer has a total of", sum(DC))
            print("Dealer wins")
            print("#"*30)
            money *= -1
            
    return money

playAgain = input("Welcome to Black Jack! Would you like to play? (y or n) ")
money = 0
moneyMade = 0 
moneyLost = 0
bank = 0 

bank = 15000

while playAgain != "n":
    
    bet = int(input("How much money are you putting down? (1:1 payout): "))
    bank -= bet 
    
    money = main(bet)
    print(money)
    if money > 0:
        moneyMade += money
    else:
        moneyLost += money
    print(f"Bank: {bank}")
    print(f"Profits: {moneyMade}")
    print(f"Losses: {moneyLost}")

    
    
        
    print("[]"*30)
    # looping the game
    playAgain = input('''
\\
Do you want to play again, y or n?
\\
''')

    
    if playAgain == 'n':
        
        break
        
    else:
        print("\n"*100)
        print("Lets play again!")

    
print(f'''

 ____  _____ _____  __   _____  _   _            
/ ___|| ____| ____| \ \ / / _ \| | | |           
\___ \|  _| |  _|    \ V / | | | | | |           
 ___) | |___| |___    | || |_| | |_| |           
|____/|_____|_____|___|_| \___/ \___/_  __ _____ 
| \ | | ____\ \/ /_   _| |_   _|_ _|  \/  | ____|
|  \| |  _|  \  /  | |     | |  | || |\/| |  _|  
| |\  | |___ /  \  | |     | |  | || |  | | |___ 
|_| \_|_____/_/\_\ |_|     |_| |___|_|  |_|_____|

Total Points : {(moneyLost+moneyMade)+bank}

''')