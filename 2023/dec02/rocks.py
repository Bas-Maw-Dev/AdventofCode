# Scores for RPS
# Rock (A)(X) =  1 : Paper (B)(Y) = 2  : Scissors (C)(Z) =  3
# Win =  6  : Lose = 0   : Draw =  3

# Function to change the letter into a score
def base_score(letter):
    if letter == 'A' or letter == 'X':
        return 1
    elif letter == 'B' or letter == 'Y':
        return 2
    elif letter == 'C' or letter == 'Z':
        return 3

#Using the numbers compare who won return their score
def win_lose_draw(player_a, player_b):
    if player_a == player_b:
        return 3
    elif player_a == 1:
        if player_b == 2:
            return 0
        return 6
    elif player_a == 2:
        if player_b == 3:
            return 0
        return 6
    elif player_a == 3:
        if player_b == 1:
            return 0
        return 6

def rigged_score(play_style, player_a):
    style_score = 0
    # Lose the game
    if play_style == 'X':
        if player_a == 'A':
            style_score = 3
        elif player_a == 'B':
            style_score = 1
        else:
            style_score = 2

        return (0 + style_score)
    
    # Draw the game
    elif play_style == 'Y':
        if player_a == 'A':
            style_score = 1
        elif player_a == 'B':
            style_score = 2
        else:
            style_score = 3
        return (3 + style_score)
    
    # Win the game
    if player_a == 'A':
        return 8
    elif player_a == 'B':
        return 9
    else: 
        return 7


file = open('rockpapersc.txt', 'r')

pa_score = 0
pb_score = 0

rigged_result = 0

for line in file:
    line = line.split()
    player_a = base_score(line[0])
    player_b = base_score(line[1])
    pa_score = pa_score + player_a + win_lose_draw(player_a, player_b)
    pb_score = pb_score + player_b + win_lose_draw(player_b, player_a)
    rigged_result += rigged_score(line[1], line[0]) 
    print(f"player A score: {pa_score} Player B: {pb_score}")
    print(f"Rigged score: {rigged_result}")
