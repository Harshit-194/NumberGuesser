import random
print("Welcome to the Number Guesser")#the welcome message
lose_point=5 #maximum number of incorrect guesses allowed
#default:
while True: #executes unless exited
    print("--------------------Menu---------------------\n1>Default Game(number start from 1)\n2>User defined Game\n3>quit") #the menu of available games and exit option
    choice1 = int(input("enter your choice number from menu:")) #to take option selected by users
    if choice1==3: #if user choose to quit the game
        print("THANK YOU for playing!!!")
        break
    elif choice1==1: #if user choose default game levels
        print("You have entered default game zone:\n---------------------Menu for levels---------------------") #to show the chosen game type and menu header
        print("1. very easy(20 numbers)\n2. easy(50 numbers)\n3. medium(100 numbers)\n4. hard(500 numbers)\n5. Expert(1000 numbers)")#to show all available game options
        choice2=int(input("enter your choice number from menu:"))# to take user choice to select game option
        count=1


        # level 1: 20 numbers
        if choice2==1: #case if level 1 is chosen
            System_number = random.randint(1,20)#to generate random number for getting system chosen number (the number to be guessed)
            while True:
                user_number = int(input("Choose a number 1 to 20: "))# to take user input (the user's guess)
                if 20<user_number<1:#to make sure user choose a number in the desired range
                    print("please choose a number between 1 and 20")
                else:
                    if count == lose_point : #to set the number of tries at which user loses
                        print(f"Your tries exceeded {lose_point} , you lost!!!!!!!!!!")
                        break
                    else:
                        if user_number == System_number: #if number guessed correctly
                            print(f"You correctly guessed the number {user_number} with {lose_point-count} tries left!!")
                            break
                        elif user_number<System_number: #case if number is lower than the system number
                            print(f"Incorrect!!! {lose_point-count} tries left !!!!!! Try a higher number!!!!")
                        elif user_number>System_number: #case if number is higher than the system number
                            print(f"Incorrect!!! {lose_point-count} tries left !!!!!!S Try a lower number!!!!")
                    count = count + 1 #to update the number of tries



        # level 2: 50 numbers
        elif choice2==2: #case if level2 is chosen
            System_number = random.randint(1, 50) #to generate random number for getting system chosen number (the number to be guessed
            while True:
                user_number = int(input("Choose a number 1 to 50: "))# to take user input(the user's guessed number)
                if 1>user_number> 50: #to make sure user choose a number in the desired range
                    print("please choose a number between 1 and 50")
                else:
                    if count == lose_point: #to set the number of tries at which the user loses
                        print(f"Your tries exceeded {lose_point}, you lost!!!!!!!!!!")
                        break
                    else:
                        if user_number == System_number:#case if number guessed correctly
                            print(f"You correctly guessed the number {user_number} with {lose_point-count} tries left!!")
                            break
                        elif user_number < System_number: #case if number is lower than system number
                            print(f"Incorrect!!! {lose_point - count} tries left !!!!!! Try a higher number!!!!")
                        elif user_number > System_number:#case if number is higher than system number
                            print(f"Incorrect!!! {lose_point - count} tries left !!!!!!S Try a lower number!!!!")
                    count = count + 1 #to update the number of tries


        # level 3: 100 numbers
        elif choice2==3: #case if level 3 is chosen
            System_number = random.randint(1, 100)#to generate random number for getting system chosen number (the number to be guessed)
            while True:
                user_number = int(input("Choose a number 1 to 100: "))# to take user input(the user's guessed number)
                if 1>user_number > 100:#to make sure user choose a number in the desired range
                    print("please choose a number between 1 and 100")
                else:
                    if count == lose_point: #to set the number of tries at which the user loses
                        print(f"Your tries exceeded {lose_point}, you lost!!!!!!!!!!")
                        break
                    else:
                        if user_number == System_number:#case if number guessed correctly
                            print(f"You correctly guessed the number {user_number} with {lose_point-count} tries left!!")
                            break
                        elif user_number < System_number:#case if number is lower than system number
                            print(f"Incorrect!!! {lose_point - count} tries left !!!!!! Try a higher number!!!!")
                        elif user_number > System_number:#case if number is higher than system number
                            print(f"Incorrect!!! {lose_point- count} tries left !!!!!!S Try a lower number!!!!")
                    count = count + 1  #to update the number of tries


        # level 4: 500 numbers
        elif choice2==4: #case if level 4 is chosen
            System_number = random.randint(1, 500) #to generate the system number(number to be guessed)
            while True:
                user_number = int(input("Choose a number 1 to 500: "))#to take user input(user's guessed number)
                if 1> user_number > 500: # to make sure user select the number in desired range
                    print("please choose a number between 1 and 500")
                else:
                    if count == lose_point:#case if user lost
                        print(f"Your tries exceeded {lose_point}, you lost!!!!!!!!!!")
                        break
                    else:
                        if user_number == System_number:# case if number guessed correctly
                            print(f"You correctly guessed the number {user_number} with {lose_point-count} tries left!!")
                            break
                        elif user_number < System_number:#case if number lower number is guessed
                            print(f"Incorrect!!! {lose_point - count} tries left !!!!!! Try a higher number!!!!")
                        elif user_number > System_number:# case if higher number is guessed
                            print(f"Incorrect!!! {lose_point - count} tries left !!!!!!S Try a lower number!!!!")
                    count = count + 1 #to update the number of tries


        #level 5: 1000 numbers
        elif choice2==5:#case if level5 is chosen
            System_number = random.randint(1, 1000)# to generate a system number(number to be guessed)
            while True:
                user_number = int(input("Choose a number 1 to 1000: "))#to take user input(user's guess)
                if 1 > user_number > 1000:#to make sure number is guessed in the desired range
                    print("please choose a number between 1 and 1000")
                else:
                    if count == lose_point:#case if lost
                        print(f"Your tries exceeded {lose_point}, you lost!!!!!!!!!!")
                        break
                    else:
                        if user_number == System_number:#case if number guessed correctly
                            print(f"You correctly guessed the number {user_number} with {lose_point-count} tries left!!")
                            break
                        elif user_number < System_number:#case if a lower number is guessed
                            print(f"Incorrect!!! {lose_point - count} tries left !!!!!! Try a higher number!!!!")
                        elif user_number > System_number:#case if a higher number is guessed
                            print(f"Incorrect!!! {lose_point - count} tries left !!!!!!S Try a lower number!!!!")
                    count = count + 1 #to update the number of tries


    #custom level:
    elif choice1==2:#case if user choose to play a custom range of number
        count=1
        lower=int(input("enter lower number: "))#to take the user input for the lower number of the range for custom range
        upper=int(input("enter upper number: "))#to take the user input for the upper number of the range for custom range
        System_number=random.randint(lower, upper)#to generate the system number (number to be guessed) in the range specified by the user
        while True:
            user_number = int(input(f"Choose a number {lower} to {upper}: "))#asking user to guess the number in a desired range(user's guess)
            if upper < user_number < lower:#to make sure user guesses a number in the desired range
                print(f"please choose a number between {lower} and {upper}")
            else:
                if count == lose_point:# case if user lost
                    print(f"Your tries exceeded {lose_point}, you lost!!!!!!!!!!")
                    break
                else:
                    if user_number == System_number:# case if number guessed correctly
                        print(f"You correctly guessed the number {user_number} with {lose_point-count} tries left!!")
                        break
                    elif user_number < System_number:#case if a lower number is guessed
                        print(f"Incorrect!!! {lose_point - count} tries left !!!!!! Try a higher number!!!!")
                    elif user_number > System_number:#case if a higher number is guessed
                        print(f"Incorrect!!! {lose_point - count} tries left !!!!!!S Try a lower number!!!!")
                count = count + 1#updating the number of tries
    else:# making sure to give output if invalid choice is made by user while selecting the options
        print("please enter a valid input!!!")
