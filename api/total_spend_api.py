import os

from dotenv import load_dotenv
import requests

load_dotenv()

BASE_URL = os.getenv("BACKEND_BASE_URL")


def get_this_months_total_spend():
    response_obj = requests.get(f"{BASE_URL}/expenses/month-spend")
    response = response_obj.json()

    if response_obj.status_code != 200:
        raise Exception(response.get("Message"))

    return response


def get_this_and_prev_months_total_spend():
    response_obj = requests.get(f"{BASE_URL}/expenses/month-comparison")
    response = response_obj.json()

    if response_obj.status_code != 200:
        raise Exception(response.get("Message"))

    return response
