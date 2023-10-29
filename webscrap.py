#Commiting file after inviting another user to repository and assign her to change the code to save the output to the file.
print("Webscrapping is done!")

#Get HTML of Google
import requests
from bs4 import BeautifulSoup

response = requests.get("https://google.com")

html= BeautifulSoup(response.text, "html.parser")

#adding this as a contributor to the repository
output_file = "scrapped_text.txt" #specifying the file name-Tooba

with open(output_file, "w") as f1: #save the scrapped text to the specified file
    f1.write(html)

print(html.prettify())

