import random
choice = 'Y'
while choice.upper()=='Y':
    guess= -1
    count =-1
    num = random.randint(1,100)
    while guess!=num:
        try:
            guess=int(input("Enter a number to guess (1,100):"))
            count+=1
            if(guess<num):
                print("Guess a larger number.")
            elif(guess>num):
                print("Guess a smaller number.")
            else:
                print(f"You guessed it right in {count} attempts.")
        except:
            print("You entered an invalid number!\nPlease enter a valid one.")    
    choice = input("Do you want to play it again(Y/N):\n")
print("Thanks for playing!")