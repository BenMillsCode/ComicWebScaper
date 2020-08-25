import requests, re
from bs4 import BeautifulSoup

result = requests.get("https://www.questionablecontent.net/archive.php")

soup = BeautifulSoup(result.content, "html.parser")

for sibling in soup.b.next_siblings:
    print(sibling.string)