from api.categories_api import get_categories
from api.users_api import get_users

users_api_response = get_users()
users = users_api_response.get("users")

categories_api_response = get_categories()
categories = categories_api_response.get("categories")
