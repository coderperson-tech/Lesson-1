with open('Codingal.txt','w') as file:
    file.write("Hi! i am peguin and i am 1 yr old")
file.close()


with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()