🚀 Features
🔍 Scrape products, FAQs, policies, contact info, and more from any Shopify store.

⚡ FastAPI backend for scalable performance.

🖥️ Streamlit frontend for user-friendly UI.

📄 Structured JSON output.

🌐 No Shopify API key needed.

💾 PostgreSQL support via Supabase (optional).

🧱 Project Structure

shopify_insights/
│
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI entrypoint
│   ├── schemas.py            # Pydantic models
│   ├── scraper.py            # Web scraping logic
│   └── utils.py              # Helpers (optional)
│
├── frontend/
│   └── streamlit_app.py      # Streamlit UI
│
├── requirements.txt          # Backend dependencies
├── requirements_frontend.txt # Streamlit dependencies
├── .env                      # Environment variables
├── README.md                 # This file
└── run.bat / run.sh          # Quick launch scripts
⚙️ Installation & Setup
🔧 Backend (FastAPI)
1.Clone the repo 
git clone https://github.com/your-username/shopify-insights.git
cd shopify-insights
2.Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
3. Install backend dependencies
pip install -r requirements.txt

4.Run FastAPI server
uvicorn app.main:app --reload
💻 Frontend (Streamlit UI)
Activate the same virtual environment (if not already)

streamlit run frontend/streamlit_app.py
