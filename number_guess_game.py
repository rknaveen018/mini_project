import random
guess = 0
while guess < 4:
    guess += 1
    rand_num = random.randrange(10)
    guessed_num = int(input("Enter the chosen number : "))
    if guessed_num != rand_num:
        print("You have " + str(4-guess) + " left in your hand")
    else:
        print("\nššš you got me ššš")
        break
print("\n\t ššš We had a great play ššš")
