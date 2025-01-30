x = ("apple", "banana", "cherry")
y = list(x)

y.insert(0, "lemon") 
y.append("melon")
y.remove("banana")
y.pop(1)

x = tuple(y)
print(x)

a = ("eee", "aaa")
x += a
print(x)