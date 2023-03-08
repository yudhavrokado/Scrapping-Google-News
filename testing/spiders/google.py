import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urlencode
from urllib.parse import urlparse
from ..items import TestingItem
from datetime import datetime
import pandas as pd
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector

#print("Masukan Keyword :", end = "")
#keywords = str(input())

#def create_google_url(query, site=''):
 #   google_dict = {"q": query, "num": 100, }
  #  if site:
   #     web = urlparse(site).netloc
    #    google_dict["as_sitesearch"] = web
     #   return "http://www.google.com/search?" + urlencode(google_dict)
   # return "http://www.google.com/search?" + urlencode(google_dict)

class GoogleSpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["www.google.com"]
    custom_settings = {
        'ROBOTSTXT_OBEY' : False,
        'DOWNLOAD_DELAY' : 10
    }

    def start_requests(self):
        url = "http://www.google.com/search?q=tumpahan+minyak+pertamina"
        yield scrapy.Request(url=url, callback=self.parse_google)
        #queries = ['tumpahan+minyak+pertamina', 'clickup+reviews', 'best+project+management+software', 'best+project+management+software+for+small+teams']
        #for query in queries:
         #   url = create_google_url(query)

    def parse_google(self, response):
        driver = webdriver.Chrome()
        #driver.implicitly_wait(10)
        #wait = WebDriverWait(driver, 5)
        driver.get("https://news.google.com/search?q=tumpahan%20minyak%20pertamina")

        item = TestingItem()

        testing = driver.find_elements(By.XPATH, '//div[@class="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc"]')

        for element in testing:
            item['titel'] = element.text.split("\n",1)[0]
            item['date_post'] = element.text.split("\n",1)[1]
            item['link'] = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            item['scrape_date'] = datetime.now()

            yield item
 
   

        driver.quit()

  