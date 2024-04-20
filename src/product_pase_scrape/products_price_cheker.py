from product_pase_scrape.product_repositoy import Product_repository
from selenium import webdriver
from product_pase_scrape.amazon_product_page_scraper import AmazonProductsPageScraper
from product_pase_scrape.meli_products_page_scraper import MelProdcutsPageScraper
import os 
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv() 

class productsPriceCheker : 
    def __init__(self) -> None:
        self.repository = Product_repository()

    def check(self) : 
        options = webdriver.ChromeOptions()
        options.binary_location = "/Program/Files/Google/Chrome/Application"
        products = self.repository.list_products()

        for product in products: 
            amazon_product_page_scraper = AmazonProductsPageScraper(webdriver.Chrome(options=options))
            amazon_product_html = amazon_product_page_scraper.get_html("https://www.amazon.com/"+product[product["amazon_url"]])
            new_amazon_price = amazon_product_page_scraper.get_current_price(html_content=amazon_product_html)


            meli_product_page_scraper = MelProdcutsPageScraper(webdriver.Chrome(options=options))
            meli_product_html = meli_product_page_scraper.get_html([product["meli_url"]])
            new_meli_price = meli_product_page_scraper.get_current_price(html_content=meli_product_html)

            if(new_amazon_price != product["amazon_price"]):
                self.notify(f"El precio del producto {product['name']} en Amazon ha cambiado")
                self.repository.update_product(product["_id"], {"amazon_price": new_amazon_price})

            if(new_meli_price != product["meli_price"]):
                self.notify(f"El precio del producto {product['name']} en Mercado Libre ha cambiado")
                self.repository.update_product(product["_id"], {"meli_price": new_meli_price})


    
    def notify (self, msg: str): 
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")

        email_message = EmailMessage() 

        email_message.set_content(msg)
        email_message["subject"] = "Actualizacion de precios de productos"
        email_message["to"] = user
        email_message["from"] = user 

        server = smtplib.SMTP("simonmartinez1605@gmail.com", 537)

        server.starttls()
        server.login(user, password)
        server.send_message(email_message)
        server.quit()
