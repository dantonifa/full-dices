# CSE 210 W02 ASSIGNMENT:full-dice is a game where the player
# seeks to earn as many points as possible.
# Author: David Antonio Fajardo.
"""Rules of the game:
Dice is a game in which the player seeks to earn as many points as possible
by repeatedly rolling five dice and accumulating the score
until they are no longer able to continue.
When asked 'Roll dice? If the player answers "n" or no, the game is over.
If the player answers "y" or yes, the points are added to their score.
The player scores 100 points for each one that is rolled.
The player scores 50 points for each five that is rolled.
The dice values and player score are displayed on the screen.
If the player does not roll any ones or fives the game is over.' """
import random
dice_values = [ [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
               [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
die_1_index = dice_values[0]
die_2_index = dice_values[1]
die_3_index = dice_values[2]
die_4_index = dice_values[3]
die_5_index = dice_values[4]

def main ():
    start_game = input(f'Roll dice? [y/n] ')
    rolled_numbers =[]

    if start_game.lower() == 'y' or start_game == 'yes':
        die_1_value = random.choice(die_1_index)
        rolled_numbers.append(die_1_value)
        die_2_value = random.choice(die_2_index)
        rolled_numbers.append(die_2_value)
        die_3_value = random.choice(die_3_index)
        rolled_numbers.append(die_3_value)
        die_4_value = random.choice(die_4_index)
        rolled_numbers.append(die_4_value)
        die_5_value = random.choice(die_5_index)
        rolled_numbers.append(die_5_value)
        print(f'You rolled: {rolled_numbers}')
        score(rolled_numbers)
    elif start_game.lower() == 'n' or start_game == 'no':
        print(f'Game finished!')
        exit()
def score(dice_numbers):
    score = 0
    for value in (dice_numbers):
        if value == 5:
            score = score + 50
        elif value == 1:
            score = score + 100
    print(f'Your score is:{score}')
    main()
    if score == 0:
        print(f'Game finished! Good')
        exit()

if __name__ =="__main__":
    main()
