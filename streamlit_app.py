import streamlit as st
import requests

st.set_page_config(page_title="🛍️ Shopify Store Insights", layout="wide")

st.title("🛍️ Shopify Store Insights Fetcher")

st.markdown("Enter Shopify store URL (e.g. `memy.co.in` or `https://memy.co.in`):")

store_url = st.text_input("Shopify Store URL", value="https://memy.co.in")

if st.button("Fetch Insights"):
    if not store_url:
        st.error("Please enter a Shopify store URL.")
    else:
        with st.spinner("Scraping store..."):
            try:
                backend_url = f"http://127.0.0.1:8000/scrape?website_url={store_url}"
                response = requests.get(backend_url)
                data = response.json()

                if response.status_code != 200:
                    st.error(f"Error: {data.get('detail', 'Unknown error')}")
                else:
                    st.success("✅ Store Insights")

                    st.json(data)

                    st.markdown("### 🛒 Product Catalog")
                    for product in data.get("products", []):
                        title = product.get("title", "Untitled")
                        handle = product.get("handle", "unknown-handle")
                        st.markdown(f"- **{title}** — `{handle}`")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

