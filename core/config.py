"""Configuration file for the application."""

import os
from dotenv import load_dotenv

load_dotenv()

# Supabase credentials
SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_KEY: str = os.environ.get("SUPABASE_KEY")
if SUPABASE_URL is None or SUPABASE_KEY is None:
    raise ValueError("Supabase credentials not set in environment variables.")

# Webhooks for specific scrapers
WEBHOOKS = {
    "la_cuarta": os.environ.get("LA_CUARTA_WEBHOOK"),
    "somoskudasai": os.environ.get("SOMOSKUDASAI_WEBHOOK"),
    "animeflv": os.environ.get("ANIMEFLV_WEBHOOK"),
    "recetas_gratis": os.environ.get("RECETAS_GRATIS_WEBHOOK"),
    "google_trends": os.environ.get("GOOGLE_TRENDS_WEBHOOK"),
}

# Validate that all webhooks are configured
for scraper, webhook in WEBHOOKS.items():
    if not webhook:
        raise ValueError(f"The webhook for {scraper} is not configured.")