from random import randint


t = ["Rock/1", "Paper/2", "Scissors/3"]


computer = t[randint(0,2)]


player = False

while player == False:

    player = input("Rock/1, Paper/2 , Scissors/3 ?\n")
    if player == computer:
        print("Tie!")
    elif player == "Rock/1" or player == "1":
        if computer == "Paper/2":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper/2" or player == "2":
        if computer == "Scissors/3" or player == 3:
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors/3" or player == "3":
        if computer == "Rock/1":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0,2)]
