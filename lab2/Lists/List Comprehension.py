#1
#Consider the following code:
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
#What will be the value of newlist?
print(newlist)
##banana
###__syntax__ ::: newlist = [expression for item in iterable if condition == True]
####  wth???

#2
#Fill in the missing parts to complete the list comprehension:
fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]
print(newlist)

#3
#Consider the following code:
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
#What will be the value of newlist?
print(newlist)
#['apple', 'apple', 'apple']

#ex:
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if "apple" in x]
print(newlist)
#alright..