import random
from game_data import data
import art

print("Welcome to Higher Lower game! ")
print(art.logo)
print("""
=== HIGHER LOWER GAME RULES ===
1. Objective: Guess who has more social media followers.
2. Setup: You will be shown two choices (A and B).
3. How to Play: Type 'A' or 'B' to make your guess.
4. Scoring: 
   - Correct guess = You get 1 point, and the game continues. 
   - Choice B becomes the new Choice A, and a new opponent is generated.
5. Game Over: The moment you guess incorrectly, the game ends immediately!
===============================
""")

random.shuffle(data)
A = random.choice(data)
B = random.choice(data)
while A == B:
    B = random.choice(data)
print(f"Option A: {A['name']} is a {A['description']}, from {A['country']}")
print(art.vs)
print(f"Option B: {B['name']} is a {B['description']}, from {B['country']}")

def compare(A, B):
    if A['follower_count'] > B['follower_count']:
        winner = 'A'
    else:
        winner = 'B'
    return winner

winner = compare(A, B)
choice = input("Who has more followers on instagram: 'A' or 'B' \n ").upper()

score = 0

while choice == winner:
    score += 1
    A = B
    B = random.choice(data)
    while A == B:
        B = random.choice(data)
    print(" \n" * 100)
    print(f"You are right! Your score is: {score}")

    print(f"Option A: {A['name']} is a {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"Option B: {B['name']} is a {B['description']}, from {B['country']}")

    choice = input("Who has more followers on instagram: 'A' or 'B' \n ").upper()
    winner = compare(A, B)

print(f"You are wrong! You lose. Your final score is {score}")


