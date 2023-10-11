file = open('some_data.txt')



lines = file.readlines()
print("lines: ",lines)

# print(file.read())
line= file.readline()
while line != "":
# for i in file.readline():
    print(line)
    line= file.readline()




file.close()



#int i = file.li