from product_pase_scraper import ProductsPageScraper 
from bs4 import BeautifulSoup
from .product_pase_scraper import product
from time import sleep

class AmazonProductsPageScraper(ProductsPageScraper):

    def __init__(self, driver) -> None:
        self.driver = driver
        
    def get_html(self, url: str) -> BeautifulSoup: 
        self.driver.get(url)
        sleep(5)
        content = self.driver.page_source
        html = BeautifulSoup(content, "html.parser") 
        self.driver.close()
        return html 
    
    def get_product(self, html_content: BeautifulSoup) -> list[product]: 
        return super().get_products(html_content)