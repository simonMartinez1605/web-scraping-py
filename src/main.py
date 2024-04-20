from selenium import webdriver
from product_pase_scrape.amazon_product_page_scraper import AmazonProductsPageScraper
from product_pase_scrape.meli_products_page_scraper import MelProdcutsPageScraper
from product_pase_scrape.product_repositoy import Product_repository

def init() : 
    item_name = input("Ingrese el nombre del producto que desea buscar: ")
    options = webdriver.ChromeOptions()
    options.binary_location = "/Program/Files/Google/Chrome/Application"

    amazon_search_result_url = "https://www.amazon.com/s?k={}".format(item_name)
    mercado_search_result_url = "https://listado.mercadolibre.com.co/{}".format(item_name) 

    # Amazon
    amazon_product_page_scraper = AmazonProductsPageScraper(driver= webdriver.Chrome(options=options))
    amazon_result_html = amazon_product_page_scraper.get_html(amazon_search_result_url)

    amazon_products = amazon_product_page_scraper.get_products(html_content=amazon_result_html)

    for item in amazon_products : 
        print("{}. Product : {} Precio ${}".format(item.id, item.name, item.price, item.url), end="\n\n")

    amazon_product_id = input("Ingrese el id de uno de los productos de amazon: ")

    AmazonProduct = next(filter(lambda product: product.id == int(amazon_product_id), amazon_products))

    # Mercado libre
    meli_product_page_scraper = MelProdcutsPageScraper(driver=webdriver.Chrome(options=options))
    meli_results_html = meli_product_page_scraper.get_html(mercado_search_result_url)

    meli_products = meli_product_page_scraper.get_products(html_content=meli_results_html)

    for result in meli_products: 
        print("{}. Product : {} Precio ${}".format(result.id, result.name, result.price, result.url), end= "\n\n")  

    meli_product_id = input("Ingrese el id de el producto de amazon: ")

    MeliProduct = next(filter(lambda product: product.id == int(meli_product_id), meli_products))

    Product_repository().save_product(
        name=item_name, 
        amazon_url= AmazonProduct.url,
        meli_url= MeliProduct.url ,
        amazon_price=AmazonProduct.price,
        meli_price=MeliProduct.price 
    )



if __name__ == "__main__": 
    init()