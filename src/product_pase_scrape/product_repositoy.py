from pymongo import MongoClient
from bson import objectid

class Product_repository : 
    def __init__(self):
        self.cliente = MongoClient(
            host="mongodb+srv://simonmartinez1605:simonmartinez1605@cluster0.bf1uebt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", 
            port=27017
        )

        self.db = self.cliente["web-scraping"]
        self.collection = self.db.products

    def save_product(self, name: str, amazon_url : str, meli_url: str, amazon_price : float , meli_price: float): 

        product = {
            "name" : name, 
            "amazon_url" : amazon_url, 
            "meli_url": meli_url, 
            "amazon_price" : amazon_price, 
            "meli_price": meli_price
        }

        self.collection.insert_one(product)

    def list_products(self): 
        results = self.collection.find({})

        return results

    def update_product (self, id:str, data : dict): 
        self.collection.find_one_and_update(
            {"_id": objectid(id)}, 
            {"$set": data}, 
            upsert=False
        )