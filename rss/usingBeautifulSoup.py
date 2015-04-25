__author__ = 'paroksh.saxena'
import pymysql
import feedparser
from bs4 import BeautifulSoup

url = "http://www.myntra.com/lookgood/feed/"

feed = feedparser.parse(url)

print(feed.keys())

feedEntries = feed["entries"]

connection = pymysql.connect("localhost","root","paroksh","test")

for eachFeed in feedEntries:
    print(eachFeed.keys())
    content = eachFeed["content"][0]["value"]
    content = content.encode(encoding='UTF-8',errors='ignore')
    soup = BeautifulSoup(content)
    #print(soup.prettify())
    description = soup.p
    if description is not None:
        description = description.encode(encoding='UTF-8',errors='ignore')
    if soup is not None and soup.img is not None and soup.img.attrs is not None and "src" in soup.img.attrs.keys():
        imageUrl = soup.img.attrs['src']
    if imageUrl is not None:
        imageUrl = imageUrl.encode(encoding='UTF-8',errors='ignore')
    sql = "insert into rss (content,description,image_url) values (%s,%s,%s)"
    #print(sql % (content,description,imageUrl))
    #break
    curs = connection.cursor()
    curs.execute(sql,(content,description,imageUrl))
    curs.close()

connection.commit()
connection.close()
print("done")