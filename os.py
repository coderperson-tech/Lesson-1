new_file = open('New_File.txt','x')
new_file.close()

import os
print("Chickeing if my_file exists or not.....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file does not exist")


my_file = open("my_file.txt", "w")
my_file.write("Hi i am peguin and i am 1 yr old")
my_file.close()

os.remove('Codingal.txt')