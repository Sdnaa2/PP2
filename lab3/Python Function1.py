#1
def converter(grams):
    ounces = 28.3495231 * grams
    return(ounces)


#2
def converter(F):
    C = (5 / 9) * (F - 32)
    return C

#3
def solve(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if (chickens * 2 + rabbits * 4 == legs):
            return f"Rabbits: {rabbits}\nChickens: {chickens}"

#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

    
#5
from itertools import permutations

def print_permutations(s):
    perms = permutations(s)
    for p in perms:
        print("".join(p))

#6
def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

sentence = "We are ready"
print(sentence, "->", reverse_sentence(sentence))

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:  
            code.pop(0)  
        if not code:  
            return True  
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#9
import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

#10
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#11
def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())  # Remove spaces and punctuation
    return cleaned_text == cleaned_text[::-1]

#12
def histogram(lst):
    for num in lst:
        print('*' * num)

histogram([4, 9, 7])

#13
import random

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

guess_the_number()


