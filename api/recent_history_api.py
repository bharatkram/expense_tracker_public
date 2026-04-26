import os

from dotenv import load_dotenv
import requests

load_dotenv()

BASE_URL = os.getenv("BACKEND_BASE_URL")


def get_recent_history():
    response_obj = requests.get(f"{BASE_URL}/")
    response = response_obj.json()

    if response_obj.status_code != 200:
        raise Exception(response.get("Message"))

    return response
