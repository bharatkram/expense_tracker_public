import os

from dotenv import load_dotenv
import requests

load_dotenv()

BASE_URL = os.getenv("BACKEND_BASE_URL")


def get_categories():
    response = requests.get(f"{BASE_URL}/categories")

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.text)
