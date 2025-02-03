import math
import random

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    secret_number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0
    while True:
        guess = int(input("\nTake a guess.\n"))
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
