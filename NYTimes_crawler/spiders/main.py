# coding:utf-8

import time
import urllib.request
import urllib.error
import scrapy
from bs4 import BeautifulSoup

class NYTimes_Spider(scrapy.Spider):
    name = 'NYTimes'
    start_urls = ['https://www.nytimes.com/']

    def parse(self, response):
        #analyze web content
        #res = BeautifulSoup(response.body, "lxml")
        #links = set()
        #story_lists = res.find_all("h2", {"class":"story-heading"})
        #res = response.xpath('//h2[contains(@class, "section-heading")]/a/@href | //h2[contains(@class, "story-heading")]/a/@href')
        res = response.xpath('//h2[contains(@class, "section-heading")] | //h2[contains(@class, "story-heading")]')
        print("@@")
        print(res.extract().get_text())
        #for story_list in res.find_all("h2", {"class":"story-heading"}):
        for story_list in res:
            try:
                story_title = story_list.find('a').get_text(strip=True)
                print(story_title)
                for story_link in story_list.find_all('a', href=True):
                    print(story_link['href'])
                    yield scrapy.Request(story_link['href'], self.parse_detail)
            except UnicodeEncodeError:
                pass
            except AttributeError:
                pass