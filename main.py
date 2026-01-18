import random
print("EASY = 5 LIFE , HARD = 3 LIFE")
print("EASY - (1,9) , HARD - (10,19)")
choice = input("Select Difficulty Hard/Easy")
if choice.upper() == "EASY" :
    A = random.randint(1,9)
    print("Enter your Guess")
    life = 5

    while life > 0 :
        a = int(input())
        if a == A :
            print("CORRECT")
            print("NUMBER IS" , a)
            break
        else :
            print("Try Again")
            life = life - 1
elif choice.upper() == "HARD" :
    B = random.randint(10,19)
    print("Enter your Guess")
    life = 3

    while life > 0 :
        a = int(input())
        if a == B :
            print("CORRECT")
            print("NUMBER IS" , a)
            break
        else :
            print("Try Again")
            life = life - 1
else :
    print("ONLY SELECT EASY/HARD")
