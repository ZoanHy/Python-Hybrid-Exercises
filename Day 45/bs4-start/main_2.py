from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_papge = response.text

soup = BeautifulSoup(yc_web_papge, 'html.parser')

articles= soup.select(selector=".titleline a")
article_texts = []
article_links = []

for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links .append(article_tag.get('href'))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_ = "score")]

index_highest_vote = [ index for index in range(len(article_upvotes)) if article_upvotes[index] == max(article_upvotes)]

print(article_texts)
print(article_links)
print(article_upvotes)

print(index_highest_vote)