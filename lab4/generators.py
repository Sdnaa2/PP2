#Create a generator that generates the squares of numbers up to some number N.
squares = (i ** 2 for i in range(5))
print(list(squares))

#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
evens = (i for i in range(11) if i % 2 == 0)
print(list(evens))

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
div_by_3_and_4 = (i for i in range(31) if i % 3 == 0 and i % 4 == 0)
print(list(div_by_3_and_4))

#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
squares_range = (i ** 2 for i in range(3, 8))
print(list(squares_range))

#Implement a generator that returns all numbers from (n) down to 0.
countdown = (i for i in range(5, -1, -1))
print(list(countdown))
