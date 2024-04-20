from abc import ABC , abstractclassmethod
from bs4 import BeautifulSoup
from .product import product

class ProductsPageScraper(ABC):

    @abstractclassmethod
    def get_html(self, url: str) -> BeautifulSoup: 
        ...

    @abstractclassmethod
    def get_products(self, html_content : BeautifulSoup) -> list[product]: 
        ...  

    @abstractclassmethod
    def get_current_price(self, html_content: BeautifulSoup) -> float: 
        ...