# read the file and store all the lines in list
# reverse the list
# write the list back to file

with open('test.txt', 'r') as reader:
    content = reader.readlines()  # ['a','b','c','d']
    reversed(content)  # ['d','c','b','a']

    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
