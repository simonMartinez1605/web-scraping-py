from product_pase_scraper import ProductsPageScraper
from product_pase_scraper import product
from product_pase_scraper import ProductsPageScraper
from time import sleep
from bs4 import BeautifulSoup


class MelProdcutsPageScraper (ProductsPageScraper): 
    def __init__(self, driver) -> None:
        self.driver = driver

    def get_html(self, url: str) -> BeautifulSoup: 
        self.driver.get(url)
        sleep(10)
        content = self.driver.page_source
        html = BeautifulSoup(content, "html.parser") 
        self.driver.close()
        return html 
    
    def get_product(self, html_content: BeautifulSoup) -> list[product]: 
        products: list[product] = []
        products_div_list = html_content.find_all("div", {"class": "andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16"})
        for index, item in enumerate(products_div_list): 
            try : 
                item_name = item.find("h2", {"class" : "ui-search-item__title"}).text
                item_price = item.find("apn", {"class" : "andes-money-amount__fraction"}).text
                item_url = item.find("a", {"class" : "ui-search-item__group__element ui-search-link__title-card ui-search-link"}).attrs["href"]
                products.append[product(id=index +1, name=item_name, price=float(item_price), url=item_url)]

            except Exception as e : 
                pass 
        
        return products 
    
    def get_current_price(self, html_content: BeautifulSoup) -> float: 
        price = html_content.find("span", {"class" : "a-size-base s-underline-text"}).text

        try: 
            item_price = html_content.find("apn", {"class" : "andes-money-amount__fraction"}).text
        except Exception as e : 
            pass 

        return float(price)