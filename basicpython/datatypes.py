# List is a data type that allows multiple values and can be different data types
values = [1, 2, 3, "abhishek", 0.6]

print(values[0])  # 1
print(values[3])  # value1
print(values[-1])  # 0.6 last index
print(values[1:4])  # [2, 3, 'value1'] sublist index
values.insert(4, "kulkarni")
# [1, 2, 3, 'abhishek', 'kulkarni', 0.6] INSERT NEW ITEM BETWEEN LIST
print(values)
values.append("End")
# [1, 2, 3, 'abhishek', 'kulkarni', 0.6, 'End'] ADD/INSERT ITEM AT THE END
print(values)
values[3] = "abhijeet"
# [1, 2, 3, 'abhijeet', 'kulkarni', 0.6, 'End'] REPLACE/MODIFY/MUTABLE SPECIFIC VALUES
print(values)
del values[0]
# [2, 3, 'abhijeet', 'kulkarni', 0.6, 'End'] DELETE ITEM FORM LIST
print(values)

# TUPLE: Same as list data type but IMMUTABLE (cannot be modified)
val = (1, 2, "ABHISHEK", 4, 5)
# val[1] = "KULKARNI"
print(val[2], "TUPLE")

# DICTIONARY: It is key value pair
# Method to  extract a values from dictionary
dic = {"a": 2, 3: "bcd", "c": "Hello user", "d": ["abhi", "jeet", "arvind"]}
# print(dic.get("d"),"DICTIONARY")
print(dic, "DICTIONARY")

# How to create dictionary dynamically in runtime
dict = {}

dict["firstname"] = "Abhishek"

dict["lastname"] = "Kulkarni"

dict["age"] = 22

print(dict)
print(dict["firstname"])


# STRINGS
print("****************STRING********************")
string = "AbhishekKulkarni.com "
string1 = "personal blog"
string2 = "       Abhishek       "

print(string[1])  # b
print(string[0:8])  # Abhishek - substring
print(string+string1)  # AbhishekKulkarni.com personal blog - Concatenation
print(string2 in string)  # True - substring check
print(string.split("."))  # ['AbhishekKulkarni', 'com '] - split string
# AbhishekKulkarni - extract 0th index i.e. first item from the splitted string
print(string.split(".")[0])
# Abhishek - removed white spaces form beginning and end of the string
print(string2.strip())
print(string2.lstrip())  # Abhishek       # removed left spaces only
print(string2.rstrip())  # Abhishek       # removed right spaces only
