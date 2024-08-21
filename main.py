import random
from art import logo,vs
from game_data import data
from os import system
      
you_score = 0  

def compare_A_B(choice,a,b):
    if a > b:
        return choice == 'A'
    else:
        return choice == 'B'

print(logo)

game_over = False


option_b = random.choice(data)

while game_over != True:
    option_a = option_b
    option_b = random.choice(data)
    if option_a == option_b:
        number_random_b = random.choice(data)

    a = option_a.get('follower_count') 
    b = option_b.get('follower_count') 

    print(f"Compare A: {option_a.get('name')}, a {option_a.get('description')}, from {option_a.get('country')}")

    print(vs)

    print(f"Compare B: {option_b.get('name')}, a {option_b.get('description')}, from {option_b.get('country')}")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    is_correct = compare_A_B(choice,a,b)

    if is_correct:
        you_score = you_score + 1
        system('cls')
        print(f"You're right! Current score: {you_score}")
         
    else:
        system('cls') 
        print(f"Sorry, that`s wrong. Final score: {you_score}")
        game_over = True



