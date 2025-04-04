file = open('Codingal.txt','r')
print(file.read())
file.close()


file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()


file = open('Codingal.txt','a')
file.write("Hi! i am peguin and i am 1yr old")
file.close()