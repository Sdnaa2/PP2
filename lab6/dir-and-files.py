import os
import shutil

#1.List only directories, files, and all items in a specified path
def list_contents(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)
    return directories, files, all_items

print(list_contents('.'))

#2.Check for access to a specified path (existence, readability, writability, executability)
def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

print(check_access('example.txt'))

#3.Check if a path exists and extract filename & directory
def path_info(path):
    if os.path.exists(path):
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        return True, directory, filename
    else:
        return False, None, None

print(path_info('example.txt'))

#4.Count the number of lines in a text file
def count_lines(filepath):
    if not os.path.exists(filepath):
        return f"Error: {filepath} does not exist."
    with open(filepath, 'r') as file:
        return sum(1 for line in file)

print(count_lines('example.txt'))

#5.Write a list to a file
def write_list_to_file(filepath, data):
    with open(filepath, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

write_list_to_file('output.txt', ['Line 1', 'Line 2', 'Line 3'])

#6.Generate 26 text files named A.txt, B.txt, ..., Z.txt
def generate_text_files():
    for i in range(26):
        filename = f"{chr(65 + i)}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}")

generate_text_files()

#7.Copy the contents of a file to another file
def copy_file(source, destination):
    shutil.copyfile(source, destination)

copy_file('output.txt', 'output_copy.txt')

#8.Delete a file after checking access & existence
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    else:
        return False

print(delete_file('output.txt'))

#To ensure example.txt exists
def create_example_file():
    with open('example.txt', 'w') as file:
        file.write("This is an example file.\nSecond line.\nThird line.")

create_example_file()