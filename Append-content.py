firstfile = input("enter the name of the first file")
secondfile = input("enter the name of the second")

f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print('Content of first file before appending - \n', f1.read())
print('Content of second file before appending - \n', f2.read())

f1.close()
f2.close()

f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

f1.write(f2.read())


f1.seek(0)
f2.seek(0)

print('content of first file after appending - \n', f1.read())
print('content of second file after appending - \n', f2.read())

f1.close()
f2.close()