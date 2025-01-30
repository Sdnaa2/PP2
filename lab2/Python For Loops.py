fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) 
    if x == "cherry":
        break


for x in range(6):
    if x == 7: 
        break
    print(x)
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)