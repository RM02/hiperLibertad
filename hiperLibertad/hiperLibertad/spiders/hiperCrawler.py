import scrapy

class HiperSpider(scrapy.Spider):

    start_urls = []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url)
            