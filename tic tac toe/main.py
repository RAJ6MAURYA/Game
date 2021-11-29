# a tic tak toe game

""" #RULES
1.Any diagonal is matched with O or X
2.Any vertical or horizontal line with O or X
"""

import sys

#rules for the winner 
def check(c):
    global ar
    for i in range(len(ar)):
        row_sum = 0
        col_sum = 0
        rdia_sum = 0
        ldia_sum = 0
        for j in range(len(ar[0])):
            if(ar[i][j] == c):
                row_sum += 1
            if(ar[j][i] == c):
                col_sum += 1
            if(i == j and ar[i][j] == c):
                ldia_sum += 1
            if(i+j == len(ar) and ar[i][j] == c):
                rdia_sum += 1
        if(row_sum == 3 or col_sum == 3 or rdia_sum == 3 or ldia_sum == 3):
            return True
    return False

# to place the correct input at the correct position
def index(x, c):
    global ar
    j = x % len(ar)
    i = x//len(ar)
    ar[i][j] = c


# display function
def display():
    for i in ar:
        for j in i:
            print(j, end=" ")
        print()


# main program
print("Enter player 1:")
p1 = input()
print("Enter Player 2")
p2 = input()
ar = [['-'for i in range(3)] for j in range(3)]
display()
ind = 0
while (ind <= 9):
    print(p1, ":")
    m = int(input())
    index(m, 'X')
    ind += 1
    if(check('X')):
        print(p1+" is the winner of the game")
        sys.exit(1)
    display()
    print(p2, ":")
    n = int(input())
    index(n, 'O')
    ind += 1

    if(check('O')):
        print(p2+' is the winner of the game')
        sys.exit(1)
    display()

for i in ar:
    for j in i:
        print(j, end=" ")
    print()
