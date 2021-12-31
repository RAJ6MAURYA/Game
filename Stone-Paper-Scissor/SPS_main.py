"""A Stone paper Scissor program"""
import random

print("Hi my name is dot. Welcome to the game")
player = input("Enter your name: ")

Dict = ["stone", "paper", "scissor"]
while True:
    input1 = Dict[int(input("Choose a option: 1.Stone 2.Paper 3.Scissor : ")) - 1]
    input2 = Dict[random.randrange(0, 3)]
    print(player + " :" + input1)
    print("computer :" + input2)
    if (
        input1 == "stone"
        and input2 == "scissor"
        or input1 == "paper"
        and input2 == "stone"
    ):
        print(player.capitalize() + " is the winner of the round.")
    elif input1 == input2:
        print("Draw Play again")
    else:
        print("DOT is the winner of the round. You can't win from a coputer XD.")
    ch = input("press y to continue")
    if ch == "y" or ch == "Y":
        continue
    else:
        break
