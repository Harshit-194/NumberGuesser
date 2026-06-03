import random
print("Welcome to the Number Guesser")
lose_point=5
#default:
while True:
    print("--------------------Menu---------------------\n1>Default Game(number start from 1)\n2>User defined Game\n3>quit")
    choice1 = int(input("enter your choice number from menu:"))
    if choice1==3:
        print("THANK YOU for playing!!!")
        break
    elif choice1==1:
        print("You have entered default game zone:\n---------------------Menu for levels---------------------")
        print("1. very easy(20 numbers)\n2. easy(50 numbers)\n3. medium(100 numbers)\n4. hard(500 numbers)\n5. Expert(1000 numbers)")
        choice2=int(input("enter your choice number from menu:"))
        count=1


        # level 1: 20 numbers
        if choice2==1:
            System_number = random.randint(1,20)
            while True:
                user_number = int(input("Choose a number 1 to 20: "))
                if 20<user_number<1:
                    print("please choose a number between 1 and 20")
                else:
                    if count==lose_point:
                        print("Your tries exceeded 10, you lost!!!!!!!!!!")
                        break
                    else:
                        if user_number == System_number:
                            print(f"You correctly guessed the number {user_number} with {10-count} tries left!!")
                            break
                        elif user_number<System_number:
                            print(f"Incorrect!!! {10-count} tries left !!!!!! Try a higher number!!!!")
                        elif user_number>System_number:
                            print(f"Incorrect!!! {10-count} tries left !!!!!!S Try a lower number!!!!")
                    count = count + 1



        # level 2: 50 numbers
        elif choice2==2:
            System_number = random.randint(1, 50)
            while True:
                user_number = int(input("Choose a number 1 to 50: "))
                if 1>user_number> 50:
                    print("please choose a number between 1 and 50")
                else:
                    if count == lose_point:
                        print("Your tries exceeded 10, you lost!!!!!!!!!!")
                        break
                    else:
                        if user_number == System_number:
                            print(f"You correctly guessed the number {user_number} with {10-count} tries left!!")
                            break
                        elif user_number < System_number:
                            print(f"Incorrect!!! {10 - count} tries left !!!!!! Try a higher number!!!!")
                        elif user_number > System_number:
                            print(f"Incorrect!!! {10 - count} tries left !!!!!!S Try a lower number!!!!")
                    count = count + 1


        # level 3: 100 numbers
        elif choice2==3:
            System_number = random.randint(1, 100)
            while True:
                user_number = int(input("Choose a number 1 to 100: "))
                if 1>user_number > 100:
                    print("please choose a number between 1 and 100")
                else:
                    if count == lose_point:
                        print("Your tries exceeded 10, you lost!!!!!!!!!!")
                        break
                    else:
                        if user_number == System_number:
                            print(f"You correctly guessed the number {user_number} with {10-count} tries left!!")
                            break
                        elif user_number < System_number:
                            print(f"Incorrect!!! {10 - count} tries left !!!!!! Try a higher number!!!!")
                        elif user_number > System_number:
                            print(f"Incorrect!!! {10 - count} tries left !!!!!!S Try a lower number!!!!")
                    count = count + 1


        # level 4: 500 numbers
        elif choice2==4:
            System_number = random.randint(1, 500)
            while True:
                user_number = int(input("Choose a number 1 to 500: "))
                if 1> user_number > 500:
                    print("please choose a number between 1 and 500")
                else:
                    if count == lose_point:
                        print("Your tries exceeded 10, you lost!!!!!!!!!!")
                        break
                    else:
                        if user_number == System_number:
                            print(f"You correctly guessed the number {user_number} with {10-count} tries left!!")
                            break
                        elif user_number < System_number:
                            print(f"Incorrect!!! {10 - count} tries left !!!!!! Try a higher number!!!!")
                        elif user_number > System_number:
                            print(f"Incorrect!!! {10 - count} tries left !!!!!!S Try a lower number!!!!")
                    count = count + 1


        #level 5: 1000 numbers
        elif choice2==5:
            System_number = random.randint(1, 1000)
            while True:
                user_number = int(input("Choose a number 1 to 1000: "))
                if 1 > user_number > 1000:
                    print("please choose a number between 1 and 1000")
                else:
                    if count == lose_point:
                        print("Your tries exceeded 10, you lost!!!!!!!!!!")
                        break
                    else:
                        if user_number == System_number:
                            print(f"You correctly guessed the number {user_number} with {10-count} tries left!!")
                            break
                        elif user_number < System_number:
                            print(f"Incorrect!!! {10 - count} tries left !!!!!! Try a higher number!!!!")
                        elif user_number > System_number:
                            print(f"Incorrect!!! {10 - count} tries left !!!!!!S Try a lower number!!!!")
                    count = count + 1


    #custom level:
    elif choice1==2:
        count=1
        lower=int(input("enter lower number: "))
        upper=int(input("enter upper number: "))
        System_number=random.randint(lower, upper)
        while True:
            user_number = int(input("Choose a number 1 to 50: "))
            if upper<user_number<lower:
                print(f"please choose a number between {lower} and {upper}")
            else:
                if count == lose_point:
                    print(f"Your tries exceeded {lose_point}, you lost!!!!!!!!!!")
                    break
                else:
                    if user_number == System_number:
                        print(f"You correctly guessed the number {user_number} with {lose_point-count} tries left!!")
                        break
                    elif user_number < System_number:
                        print(f"Incorrect!!! {lose_point - count} tries left !!!!!! Try a higher number!!!!")
                    elif user_number > System_number:
                        print(f"Incorrect!!! {lose_point - count} tries left !!!!!!S Try a lower number!!!!")
                count = count + 1
    else:
        print("please enter a valid input!!!")
