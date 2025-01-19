x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x) #Python is awesome


def myfunc():
  
    global x
    x = "fantastic"
print(x)


x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)#Python is fantastic