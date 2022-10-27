import urllib.request
from bs4 import BeautifulSoup
url=input("type the url scraping target\n")
with urllib.request.urlopen(url) as html:
    soup = BeautifulSoup(html,"html.parser")
    tags = "p span br h1 h2 h3 h4 h5 h6 strong em li dt dd mark ind del sup sub small i b".split(" ")
    for i in tags:
        for p in soup.find_all(i):
            print(p.text,end="")
