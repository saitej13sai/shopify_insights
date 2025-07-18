from fastapi import FastAPI, HTTPException, Query
from app.scraper import scrape_shopify_store
from app.models import BrandData

app = FastAPI(title="Shopify Insights API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Shopify Insights API"}

@app.get("/scrape", response_model=BrandData)
def scrape_endpoint(website_url: str = Query(..., description="Full Shopify store URL")):
    try:
        brand_data = scrape_shopify_store(website_url)
        if not brand_data:
            raise HTTPException(status_code=401, detail="Website not found or not a Shopify site")
        return brand_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
