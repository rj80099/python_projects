from art import logo
from art import vs
import game_data
import random


def check_an_account(acc_a_follower,acc_b_follower,gussed_acc):
    '''
    Return the of guessed account from the user..
    '''
    if acc_a_follower>acc_b_follower and gussed_acc=='a' or acc_b_follower>acc_a_follower and gussed_acc=='b':
        return True
    return False

    

# Generate a random account from the game data.
def get_random_account():
  '''
  Return random account from game data module
  '''
  return random.choice(game_data.data)

def HighLowGame(): 
    # Add art.
    print(logo)
    score =0
    # Make two random account from the game data.
    should_game_continue=True
    account_a=get_random_account()
    account_b=get_random_account()
    while should_game_continue:
        # Make B become the next A.
        account_a =account_b
        account_b=get_random_account()
        while account_a==account_b:
            account_b=get_random_account()
        # Format account data into printable format.
        print(f"comapring A {account_a}") 
        print(vs)
        print(f"comparing B {account_b}")

        # Ask user for a guess.
        guess=input("Who has more follower A or B\n").lower()

        # Check if user is correct.
        ## Get follower count.
        ## If Statement

        a_follower_count=account_a["follower_count"]
        b_follower_count=account_b["follower_count"]

        is_correct=check_an_account(a_follower_count,b_follower_count,guess)
        if is_correct:
            # Score Keeping.
            score +=1
            if guess == 'a':
                account_b =account_a
        else:
            # Feedback.
            print("You guessed it wrong Game Over!")
            print(f"Your score is {score}")
            should_game_continue=False

HighLowGame()
game_choice=input("Do you want to play again 'Y' or 'N'\n").lower()
# Make game repeatable.
if(game_choice=='Y'):
    HighLowGame()














