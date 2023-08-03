'''Guessing game by Scotty'''
import random
print("Welcome to Scottys numnber guessing game")
def play_game():
    score = 0
    num_new = random.randint(1,8)
    how_many_try = 0
    while how_many_try < 5:
        users_guess = int(input('I have a number in mind! What do you think it is? Guess a number from 1 to 8: You get five tries'))
        if users_guess > 9 or users_guess < 1:
            print('Sorry you have to choose a number between 1 and 8. Please try again: ')
            play_game()
        else:
            if users_guess == num_new:
                print('Congratulations you got it right')
                play_again = input('Would you like to play again? Y = Yes N = No :')
                if play_again == 'y' or play_again == 'Y':
                    play_game()
                elif play_again == 'n' or play_again == 'N':
                    print('Ok Thanks for playing!')
                    break
            else:
                print('Sorry thats wrong please try again')
                how_many_try += 1
play_game()