import math
import time
import functools

#Multiply all numbers in a list
def multiply_list(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)

print("Product of [2, 3, 5]:", multiply_list([2, 3, 5])) 

#Count uppercase and lowercase letters in a string
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

print(count_case("Hello World!")) 


#Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("ala")) 
print(is_palindrome("Bekzat"))  

#Square root after specific milliseconds
num = 25100
delay = 2123

# Function to compute square root after a delay
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  
    return math.sqrt(number)


result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} milliseconds is {result}")


#Check if all elements in a tuple are True
def all_true(tup):
    return all(tup)

print(all_true((True, True, True)))  
print(all_true((True, False, True))) 
print(all_true((1, 2, 3)))  
print(all_true((0, 1, 2)))  
