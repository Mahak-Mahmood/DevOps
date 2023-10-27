#Get HTML of Google
import request as re
response = re.get("https://google.com")
html = response.text
print("html")
