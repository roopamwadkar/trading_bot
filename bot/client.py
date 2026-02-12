import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_futures_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not api_secret:
        raise ValueError("API keys not found in .env file.")

    client = Client(api_key, api_secret, testnet=True)
    client.FUTURES_URL = "https://demo-fapi.binance.com"
    return client
