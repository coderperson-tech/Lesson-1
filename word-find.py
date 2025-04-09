word_to_find = "Hello"
found = False

with open('Codingal.txt', 'r') as file:
    for line in file:
        if word_to_find in line:
            found = True
            break

if found:
    print(f"{word_to_find} found in the file")
else:
    print(f"{word_to_find} not found in the file")