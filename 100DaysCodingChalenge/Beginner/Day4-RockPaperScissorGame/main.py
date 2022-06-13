import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_list=[rock,paper,scissors]

#print(rps_list[2])

user_choice=int(input("choose 0-rock,1-scissor,2-paper\n"))
computer_choice=random.randint(0,2)


print(f'Your choice :\n{rps_list[user_choice]}')
print(f'Computer choice :\n {rps_list[computer_choice]}')

#logic to check rock paper scissor rule

if user_choice >=3 or user_choice <0:
  print(" your choice is invalid, you loss!")
elif computer_choice>user_choice:
  print("you loss")
elif computer_choice ==0 and user_choice ==2:
  print("you loss")
elif user_choice> computer_choice:
  print("you win")
elif user_choice ==0 and computer_choice==2:
  print("you win")
elif computer_choice == user_choice:
  print("It's a draw!!")



