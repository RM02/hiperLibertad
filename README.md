# Autoscraping Challenge

This application is a web scraping bot developed in python.
Part of an autoscraping challenge.


# Quick start

### Step 1:  Installation

Clone repository

```
git clone https://github.com/RM02/hiperLibertad.git
cd hiperLibertad
```

Create a virtual enviroment
```
python -m venv env
source env/bin/activate
```

Install dependencies,

```
pip install -r requirements.txt
cd hiperLibertad
```

It should have downloaded dependencies. 


### Step 2:  Scrape it

Each branch office has asigned a code,  look for a branch name and then scrape as following:
 
```
scrapy crawl hiper -a sucursal=1
```
It should scrape data from **CORDOBA - Hipermercado Lugones**

Branch name
```
SUCURSALES  =  {

	"1":  'CORDOBA - Hipermercado Lugones',
	"2":  'CORDOBA - Hipermercado Rivera',
	"3":  'CORDOBA - Hipermercado Jacinto Rios',
	"4":  'CORDOBA - Hipermercado Ruta 9',
	"5":  'MENDOZA - Hipermercado Godoy Cruz',
	"6":  'MENDOZA - Tienda Digital Mza Capital',
	"7":  'TUCUMAN - Hipermercado Tucuman 1',
	"8":  'TUCUMAN - Hipermercado Tucuman 2',
	"9":  'MISIONES - Hipermercado Posadas',
	"10":  'CHACO - Hipermercado Chaco',
	"11":  'SANTA FE - Hipermercado Rosario',
	"12":  'SANTA FE - Hipermercado Rafaela'

}

```

##### Item Response
```
{
	'category': ['/Hogar/COCINA Y COMEDOR/REPOSTERIA Y HORNO/',
	              '/Hogar/COCINA Y COMEDOR/',
	              '/Hogar/'],
	 'description': 'Tortera Estan?ada Baja Desmontable Ilko',
	 'name': 'Tortera Estan?ada Baja Desmontable Ilko',
	 'oldprice': 2299.0,
	 'price': 2299.0,
	 'sku': '1356',
	 'stock': True,
	 'url': 'https://www.hiperlibertad.com.ar/tortera-estan-ada-baja-desmontable-ilko/p'
 }
```

# Considerations

### Data storage
By default, data is storaged in hiperdata.csv file,
You can change directory 

1. Create an .env file
2. Add FILENAME
3. add FILEPATH

```
FILENAME=DATA
FILEPATH=/home
```

### Proxy

Add to .env file the following variables:

```
PROXY_USER=user
PROXY_PASSWORD=password
PROXY_ENDPOINT=proxy.proxyprovider.com
PROXY_PORT=8000
```

