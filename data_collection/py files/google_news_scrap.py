#import what we need
#import nest_asyncio
from requests_html import AsyncHTMLSession

#nest_asyncio.apply()
asession = AsyncHTMLSession()


#use session to get the page
r = await asession.get('https://news.google.com/search?q=cryptocurrency&hl=en-IN&gl=IN&ceid=IN%3Aen/')

#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
await r.html.arender(sleep=1, scrolldown=5)
articles = r.html.find('article')
newslist = []
#loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        title = newsitem.text
        link = newsitem.absolute_links
        newsarticle = {
            'title': title,
            'link': link 
        }
        newslist.append(newsarticle)
    except:
       pass

#print the length of the list
print(len(newslist))

import pandas as pd
df = pd.DataFrame(newslist)
df.to_csv('./Smart-Financial-Assistant/data/raw/crypto_news.csv')