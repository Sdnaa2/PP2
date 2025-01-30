thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
print(thisdict["model"])
x = thisdict.get("model")
print(x)

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

