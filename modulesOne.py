# import calc
# from math import sqrt,factorial


# calc.add(56,24)
# calc.subtract(100,24)

# print(sqrt(16))


import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200
print(response.json())       # Output: API response in JSON format
