import random
print("Welcome to the game of rolling dice.")
while True:
    choice=input("Press enter the dice or 'q' to quit.")
    if choice=='q':
        print("Thank you for playing")
        break
    elif choice=='':
        number=random.randint(1,6)
        print(f"your number is {number}")
    else:
         print("wrong choice")
print("Game OVER")

