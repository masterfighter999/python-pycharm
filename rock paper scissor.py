p1=input("enter rock or paper or scissor: ")
p2=input("enter rock or paper or scissor: ")

if p1=="rock" and p2=="paper":
    print("Player 2  wins")
elif p1=="paper" and p2=="scissor":
    print("Player 2  wins")
elif p1=="scissor" and p2=="rock":
    print("Player 2  wins")
elif p1=="scissor" and p2=="scissor":
    print("Draw")
elif p1=="paper" and p2=="paper":
    print("Draw")
elif p1=="rock" and p2=="rock":
    print("Draw")
else :
    print("Player 1 wins")
