import os

from dotenv import load_dotenv
import requests

load_dotenv()

BASE_URL = os.getenv("BACKEND_BASE_URL")


def add_expense_api(payload):
    response_obj = requests.post(f"{BASE_URL}/expenses", json=payload)
    response = response_obj.json()

    if response_obj.status_code != 200:
        raise Exception(response.get("Message"))

    return response


def get_expenses_api(filters: dict):
    response_obj = requests.get(f"{BASE_URL}/expenses", params=filters)
    response = response_obj.json()

    if response_obj.status_code != 200:
        raise Exception(response.get("Message"))

    return response
