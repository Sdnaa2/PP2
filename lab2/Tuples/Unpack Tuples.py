fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)

fruits = ('apple', 'banana', 'cherry', 'lemon')
(x, *y) = fruits
print(y)

(x, *y, z) = fruits
print(y)