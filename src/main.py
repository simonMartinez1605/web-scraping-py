from selenium import webdriver
from product_pase_scrape.amazon_product_page_scraper import AmazonProductsPageScraper

def init() : 
    item = input("Ingrese el nombre del producto que desea buscar: ")
    options = webdriver.ChromeOptions()
    options.binary_location = "/user/bin/google-chrome"

    amazon_search_result_url = "https://www.amazon.com/{}".format(item)
    mercado_search_result_url = "https://listado.mercadolibre.com.co/{}".format(item)

    amazon_product = AmazonProductsPageScraper(driver= webdriver.Chrome(options=options))
    amazon_product.get_html(amazon_search_result_url)

if __name__ == "__main__": 
    init()