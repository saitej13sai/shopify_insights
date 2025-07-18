from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    title: str
    handle: str
    price: Optional[str] = None

class BrandData(BaseModel):
    store_url: str
    products: List[Product]
    hero_products: Optional[List[Product]] = []
    policies: Optional[dict] = {}
    faqs: Optional[List[dict]] = []
    social_links: Optional[dict] = {}
    contact_info: Optional[dict] = {}
    about_text: Optional[str] = ""
    important_links: Optional[List[str]] = []
