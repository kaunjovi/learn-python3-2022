import requests
from bs4 import BeautifulSoup
 
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# check status code for response received
# success code - 200

print(r) # <Response [200]>
print(r.url) # https://www.geeksforgeeks.org/python-programming-language/

# Get the raw text 
# print(r.content) # print content of request

# Print the pretty html 
soup = BeautifulSoup(r.content, "html.parser")
print( soup.prettify())