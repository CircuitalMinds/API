import requests
from bs4 import BeautifulSoup
search = lambda query: f"https://www.google.com/search?q={query}"
query = "Sons of Belial lyrics"
data = BeautifulSoup(requests.get(search(query=query)).text, "html.parser").findAll("div")

lyric = []
for div in data:
    classNames = []
    if "class" in list(div.attrs.keys()):
        classNames.extend(div['class'])
    if "BNeawe" in classNames:
        lyric.append(div.text.split("\n"))
        if "Compositor: " in div.text or "Compositores: " in div.text:
            break
for t in lyric:
    x = ""
    for s in t[:-1]:
        x += s + "\n"
    x += t[-1]
    print(x)