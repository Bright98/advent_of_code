rock = 'rock'
paper = 'paper'
scissors = 'scissors'

def converter(move):
    if move in {'A', 'X'}:
        return rock
    if move in {'B', 'Y'}:
        return paper
    if move in {'C', 'Z'}:
        return scissors

def compare(rival_move, player_move):
    if player_move == rival_move:
        if player_move == rock:
            return 3 + 1
        elif player_move == paper:
            return 3 + 2
        else:
            return 3 + 3
    
    if player_move == rock:
        if rival_move == paper:
            return 1 + 0
        else:
            return 1 + 6

    if player_move == paper:
        if rival_move == rock:
            return 2 + 6
        else:
            return  2 + 0

    if player_move == scissors:
        if rival_move == rock:
            return 3 + 0
        else:
            return 3 + 6

playerScore = 0

with open('input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        moves = line.split(" ")
        playerScore += compare(converter(moves[0]), converter(moves[1]))

print(playerScore)