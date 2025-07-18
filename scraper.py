import requests
from app.models import BrandData, Product

def scrape_shopify_store(url: str) -> BrandData:
    if not url.startswith("http"):
        url = "https://" + url

    try:
        res = requests.get(f"{url}/products.json", timeout=10)
        res.raise_for_status()
    except:
        return None

    products_json = res.json().get("products", [])

    products = [Product(title=p["title"], handle=p["handle"]) for p in products_json]

    return BrandData(
        store_url=url,
        products=products,
        hero_products=[],
        policies={},
        faqs=[],
        social_links={},
        contact_info={},
        about_text="",
        important_links=[]
    )
