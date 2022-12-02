rock = 'rock'
paper = 'paper'
scissors = 'scissors'

equal = 'equal'
win = 'win'
loose = 'loose'

def convert_rival_move(move):
    if move == 'A':
        return rock
    if move == 'B':
        return paper
    if move == 'C':
        return scissors

def convert_determiner(move):
    if move == 'X':
        return loose
    if move == 'Y':
        return equal
    if move == 'Z':
        return win

def compare(rival_move, determiner):
    if determiner == equal:
        if rival_move == rock:
            return 3 + 1
        if rival_move == paper:
            return 3 + 2
        if rival_move == scissors:
            return 3 + 3
    
    if determiner == win:
        if rival_move == rock:
            return 6 + 2
        if rival_move == paper:
            return 6 + 3
        if rival_move == scissors:
            return 6 + 1

    if determiner == loose:
        if rival_move == rock:
            return 0 + 3
        if rival_move == paper:
            return 0 + 1
        if rival_move == scissors:
            return 0 + 2

playerScore = 0

with open('input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        moves = line.split(" ")
        playerScore += compare(convert_rival_move(moves[0]), convert_determiner(moves[1]))

print(playerScore)