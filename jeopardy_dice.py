# Josiah Roa
# 102
# jeopardy_dice.py
# This homework was assigned to help me understand the usefulness of while loops,
# why and where we should use them, and how to make a game with a scoring system.
import random


# This function has no parameters, it only returns a boolean based on the
# answer given, this answer can only be a 'Y' or 'N', otherwise, it will continue
# to ask the user until the correct input is given
def get_user_answer():
    while True:
        user_answer = input('Do you want to roll again (Y/N)? ')
        if user_answer is 'Y':
            return True
        elif user_answer is 'N':
            return False
        else:
            continue


# This function takes a parameter for the turn that the game is on
# It will return a boolean based on if it is the computer's or the user's turn next
def get_next_player(turns):
    if turns % 2 == 0:
        print("It is now the user's turn")
        return False
    else:
        print("It is now the computer's turn")
        return True


# This is the main function of the game taking in two arguments, if it is the computer playing, and the value
# at which the computer will stop its turn at
# It will return the points accumulated for the turn and add them to the overall score in the main function
def take_turn(is_computer, hold_value):
    user_turn_score = 0
    computer_turn_score = 0
    # False = user's turn
    while is_computer is False:
        roll = random.randint(1, 6)
        print('You rolled a ' + str(roll))
        if roll == 1:
            user_turn_score = 1
            break
        else:
            user_turn_score += roll
            print('Your turn total is ' + str(user_turn_score))
            print(' ')
            answer = get_user_answer()
            if answer:
                continue
            else:
                break
    # True = computer's turn
    while is_computer is True:
        roll = random.randint(1, 6)
        print('You rolled a ' + str(roll))
        if roll == 1:
            computer_turn_score = 1
            break
        else:
            computer_turn_score += roll
            print('Your turn total is ' + str(computer_turn_score))
            print(' ')
            if computer_turn_score < hold_value:
                continue
            else:
                break
    if is_computer is False:
        return user_turn_score
    else:
        return computer_turn_score


# This function will take the scores and report them after the end of each round
# It takes two parameters, user_score and computer_score
# Nothing returned
def report_points(user_score, computer_score):
    print('Computer: ' + str(computer_score))
    print('User: ' + str(user_score))
    print(' ')


# This function takes 3 parameters user_score, computer_score, and the score required to end the game
# takes the scores and checks to see if the game is over, if the score is higher than the game_end, the
# function returns false, if not, it returns True, and the game keeps on going
def check_win(user_score, computer_score, game_end):
    if user_score > game_end:
        game = False
        print('Congratulations! User won this round of jeopardy dice!')
        return game
    elif computer_score > game_end:
        game = False
        print('Congratulations! Computer won this round of jeopardy dice!')
        return game
    else:
        game = True
        return game


# Main function
def main():
    # Global variables
    game = True
    turns = 0
    user_score = 0
    computer_score = 0
    hold_value = 10
    game_end = 25
    # Greeting
    print('Welcome to Jeopardy Dice!')
    print(' ')
    # While loop that controls game
    # Game ends when game is set to False
    while game:
        is_computer = get_next_player(turns)
        if turns % 2 == 0:
            user_round_score = take_turn(is_computer, hold_value)
            user_score += user_round_score
        else:
            computer_round_score = take_turn(is_computer, hold_value)
            computer_score += computer_round_score
        turns += 1
        report_points(user_score, computer_score)
        # If check_win returns False, game ends
        game = check_win(user_score, computer_score, game_end)


if __name__ == '__main__':
    main()
