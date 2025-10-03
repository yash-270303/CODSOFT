import random

def get_computer_choice():
    return random.choice(['rock','paper','scissors'])
def determine_winner(user_choice , computer_choice):
    if user_choice == computer_choice:
        return "Its a tie!"
    elif(user_choice=='rock' and computer_choice=='scissors') or \
        (user_choice=='scissors' and computer_choice=='paper') or \
        (user_choice=='paper' and computer_choice=='rock'):
        return "You win!" 
    else:
        return "You lose!"
    
def play_game():
     user_score=0
     computer_score=0

     while True:
         user_choice=input("choose rock, paper or scissors: ").lower()
         if user_choice not in ['rock','paper','scissors']:
             print("invalid choice. Please try again")
             continue
         computer_choice= get_computer_choice()
         print(f"you chose:{user_choice}")
         print(f"computer chose:{computer_choice}")

         result= determine_winner(user_choice,computer_choice)
         print(result)

         if result == "You win!":
             user_score += 1
         elif result == "You lose!" :
             computer_score += 1
         print(f"Score - You:{user_score} , Computer:{computer_score}")

         play_again = input("Do you want to play again?(yes/no):").lower()
         if play_again != 'yes' :
          break
         
if __name__ == "__main__":
    play_game()