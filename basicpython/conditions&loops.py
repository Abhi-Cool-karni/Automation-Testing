# IfElse condition

greeting = "GOOD MORNING"

if greeting == "GOOD MORNING":
    print("Condition matches.")
else:
    print("Condition do not match.")

print("If else code is completed.")

# FOR loop

# objects = [0,1,2,3,4,5,6]
# for object in objects:ṇ
#     print(object+1)

# Sum of first natural numbers 1+2+3+4+5 = 15
print("**********************FOR LOOP******************************")
sum = 0
for num in range(1, 6):
    sum = sum + num
    print("*"*sum, sum)
print("Sum completed")


print("**********************FOR LOOP******************************")
for numb in range(1, 10, 2):
    print(numb*"*", numb)

#########################################################################

# While loops
print("*******************WHILE LOOP**********************")

it = 1
while it <= 10:
    print("*"*it, it)
    it = it + 1
print("**************While loop completed*****************")

print("**************DESCENDING WHILE LOOP******************")
itt = 10
while itt > 0:
    print("*"*itt, itt)
    itt = itt-1
print("**************While loop completed*****************")


print("*******************WHILE LOOP USING IF CONDITION**********************")

it = 1
while it <= 10:

    if it != 5:
        print("*"*it, it)
    it = it + 1

print("**************While loop completed HERE 5 IS SKIPPED*****************")


print("*******************WHILE LOOP USING BREAK IN IF CONDITION**********************")

it = 1
while it <= 10:

    if it == 5:
        break

    print("*"*it, it)
    it = it + 1

print("**************While loop completed HERE LOOPS BREAK AT 4*****************")


print("*******************WHILE LOOP USING CONTINUE IN IF CONDITION**********************")

it = 10
while it > 1:
    if it == 9:
        it = it-1
        continue

    if it == 3:
        break

    print("*"*it, it)
    it = it - 1

print("**************While loop completed HERE LOOPS SKIPS AT 9 & BREAKS AT 3*****************")
