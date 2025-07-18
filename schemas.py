from pydantic import BaseModel
from typing import List, Optional

class BrandInsights(BaseModel):
    store_url: str
    hero_products: List[str] = []
    privacy_policy_link: Optional[str] = None
    brand_description: Optional[str] = None
