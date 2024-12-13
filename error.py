# syntar error 
anount = 1000
# forgetting a colon 
# if amount>2999
#     print("enough money")

# exceptions errors 
# marks = 400
# a = marks/0
# print(a)

# using try except 

marks = 400
try:
    a = marks/0
    print(a)
except Exception as e:
    print("exception caught", e)