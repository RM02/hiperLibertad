import scrapy
import json
class HiperSpider(scrapy.Spider):
    name = "hiper"
    start_urls = ["tecnologia"]
    api_url = "https://www.hiperlibertad.com.ar/api/catalog_system/pub/products/search/{category}?O=OrderByTopSaleDESC&_from={startPage}&_to={endPage}&ft&sc={sucursal}"
    
    def start_requests(self):
        for category in self.start_urls:
            url = self.api_url.format(category=category, startPage=0, endPage=20, sucursal=1)
            meta = {
                "listingPage": url,
                "category": category,
                "startPage": 0,
                "endPage": 20,
                "sucursal": 1
            }
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)
    
    def parse(self, response):

        data_json = json.loads(response.body)

        if len(data_json) == 0:
            return

        listingPage = response.meta.get("listingPage")
        category = response.meta.get("category")
        endPage = response.meta.get("endPage")
        sucursal = response.meta.get("sucursal")
                
        for product in data_json:
            print(product['link'])

        nextPage = endPage + 20
        url = self.api_url.format(category=category, startPage=endPage, endPage=nextPage, sucursal=sucursal)
        meta = {
            "listingPage": listingPage,
            "category": category,
            "startPage": endPage,
            "endPage": nextPage,
            "sucursal": sucursal
        }
        
        yield scrapy.Request(url=url, callback=self.parse, meta=meta)
            