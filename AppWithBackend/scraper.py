from newspaper import Article
from newspaper import Config

class scrape_article:
  def __init__(self, url):
    
    self.url = url

  def scrape_data(self):
    article = Article(self.url)
    article.download()
    article.parse()
    self.data = article

  def get_full_text(self):
    return self.data.text
  
  def get_paragraphs(self):
    return self.data.text.split("\n\n")

  def get_metadata(self):
    self.authors = self.data.authors
    self.title = self.data.title
    self.description = self.data.meta_description
    self.date = self.data.publish_date

  def print_everything(self):
    print(f'''Title: {self.title}
Authors: {[a.item for a in self.authors]}
Description: {self.description}
Publish Date: {self.date}''')

#article = scrape_article('https://www.forbes.com/sites/alanohnsman/2022/02/10/biden-opens-access-to-5-billion-to-build-national-ev-charging-network/')
#article.scrape_data()
#article.get_full_text()