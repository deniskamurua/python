from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title)
#print(soup.a)

# printing all elements
all_anchor_tags = soup.find_all(name="a")

# selecting text from the anchor tags
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

#printing
