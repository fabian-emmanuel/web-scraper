import requests

from pages.quote_page import QuotePage

page_content = requests.get('https://quotes.toscrape.com').content
page = QuotePage(page_content)

for quote in page.quote:
    print(quote)