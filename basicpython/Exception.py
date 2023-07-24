ItemInCart = 0
# 2 items added in cart

# if ItemInCart != 2:
#     #     raise Exception("Products count not matched.")
#     pass


# assert (ItemInCart == 2)

# Try catch/except mechanism
# If test case fails then code would not stop

# try:
#     with open('test.txt', 'r') as reader:
#         reader.read()

# except:
#     print("Somehow I reached this block because there is failure in try block.")

try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    # print("Somehow I reached this block because there is failure in try block.")
    print(e)

finally:
    print("Cleaning up resources")
