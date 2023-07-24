# READ
# open method is use to open any files

file = open("test.txt")
# print(file.read())  # read all contains of the file
# print(file.read(500))  # read n numbers of characters by passing parameters

# Read one single line at a time using readline()
# print(file.readline())
# print(file.readline())
# print(file.readline())

# Print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# using readlines it while provide in list
for line in file.readlines():
    print(line)

file.close()
