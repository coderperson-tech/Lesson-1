with open('Codingal.txt','r') as file:
    content = file.read()
updated_content = content.replace("Codingal","Hi")
with open("updated_sample.txt", 'w') as file:
    file.write(updated_content)