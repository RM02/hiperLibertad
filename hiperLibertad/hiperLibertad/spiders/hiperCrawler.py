import scrapy
import json
from hiperLibertad.items import HiperlibertadItem
from hiperLibertad.settings import SUCURSALES
class HiperSpider(scrapy.Spider):
    name = "hiper"
    start_urls = [
        "tecnologia",
        "electrodomesticos",
        "hogar",
        "bebidas",
        "almacen",
        "lacteos",
        "quesos-y-fiambres",
        "carnes",
        "frutas-y-verduras",
        "taeq",
        "congelados",
        "pastas-frescas-y-tapas",
        "limpieza",
        "perfumeria",
        "bebes-y-ninos",
        "vehiculos",
        "mascotas",
        "aire-libre-y-jardin",
        "libreria",
        "deportes"
    ]
    api_url = "https://www.hiperlibertad.com.ar/api/catalog_system/pub/products/search/{category}?O=OrderByTopSaleDESC&_from={startPage}&_to={endPage}&ft&sc={sucursal}"
    
    def __init__(self, sucursal=""):
        self.sucursal = sucursal

    def start_requests(self):

        for category in self.start_urls:
            url = self.api_url.format(category=category, startPage=0, endPage=20, sucursal=self.sucursal)
            meta = {
                "listingPage": url,
                "category": category,
                "startPage": 0,
                "endPage": 20,
                "sucursal": self.sucursal
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
            item = HiperlibertadItem()
            
            item['url'] = product['link']
            item['name'] = product['productName']
            item['price'] = product['items'][0]['sellers'][0]['commertialOffer']['Price']
            item['oldprice'] = product['items'][0]['sellers'][0]['commertialOffer']['ListPrice']

            item['stock'] = product['items'][0]['sellers'][0]['commertialOffer']['IsAvailable']
            item['category'] = product['categories']
            item['sku'] = product['productId']
            item['description'] = product['description']
            
            yield item

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
            