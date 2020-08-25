#import libraries
import requests, re
from bs4 import BeautifulSoup

#connect to archive page
result = requests.get("https://www.questionablecontent.net/archive.php")

#get the contents of the archive page
soup = BeautifulSoup(result.content, "html.parser")

#Find all links to comics
a_tags = soup.find_all('a')


for tag in a_tags:
    #Get comic name
    print(tag.string)
    #get link to comic
    tag[href]