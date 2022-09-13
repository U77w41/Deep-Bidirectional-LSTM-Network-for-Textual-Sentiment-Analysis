#import what we need
from requests_html import HTMLSession
session = HTMLSession()

#use session to get the page
r = session.get('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')
