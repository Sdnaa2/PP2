
import re

#Match a string that has an 'a' followed by zero or more 'b's
pattern1 = r"ab*"
test_strings = ["a", "ab", "abb", "ac"]
for s in test_strings:
    match = re.fullmatch(pattern1, s)
    print(f"  '{s}':", "Match" if match else "No match")
print()

#Match a string that has an 'a' followed by two to three 'b's
pattern2 = r"ab{2,3}"
test_strings = ["ab", "abb", "abbb", "abbbb"]
for s in test_strings:
    match = re.fullmatch(pattern2, s)
    print(f"  '{s}':", "Match" if match else "No match")
print()

#Find sequences of lowercase letters joined with an underscore
text = "hello_world not_matching Hello_World another_test sample_text"
pattern3 = r"[a-z]+_[a-z]+"
matches = re.findall(pattern3, text)
print("  Lowercase sequences with underscore:", matches)
print()

#Find the sequences of one uppercase letter followed by lowercase letters
text = "Hello World This is a Test Example"
pattern4 = r"[A-Z][a-z]+"
matches = re.findall(pattern4, text)
print("  Uppercase followed by lowercase sequences:", matches)
print()

#Match a string that has an 'a' followed by anything, ending in 'b'
pattern5 = r"^a.*b$"
test_strings = ["ab", "a123b", "aXYZb", "acb", "a"]
for s in test_strings:
    match = re.fullmatch(pattern5, s)
    print(f"  '{s}':", "Match" if match else "No match")
print()

#Replace all occurrences of space, comma, or dot with a colon
text = "Hello, world. This is a test"
pattern6 = r"[ ,\.]"
result = re.sub(pattern6, ":", text)
print("  After replacement:", result)
print()

#Convert a snake case string to a camel case string
snake_str = "this_is_a_snake_case_string"
camel_str = ''.join(x.capitalize() for x in snake_str.split('_'))
print("  CamelCase:", camel_str)
print()

#Split a string at uppercase letters
text = "SplitThisStringAtUppercaseLetters"
parts = re.split(r"(?=[A-Z])", text)
parts = [part for part in parts if part]  # Remove any empty strings
print("  Splitted parts:", parts)
print()

#Insert spaces between words starting with capital letters
text = "InsertSpacesBetweenCapitalWords"
result = re.sub(r"(?<!^)(?=[A-Z])", " ", text)
print("  With spaces inserted:", result)
print()

#Convert a camel case string to snake case
camel_str = "ThisIsCamelCaseString"
snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
print("  Snake case:", snake_str)
print()
