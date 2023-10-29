#Commiting file after inviting another user to repository and assign her to change the code to save the output to the file.
print("Webscrapping is done!")

#Get HTML of Google
import requests
from bs4 import BeautifulSoup

response = requests.get("https://google.com")

html= BeautifulSoup(response.text, "html.parser")

print(html.prettify())

