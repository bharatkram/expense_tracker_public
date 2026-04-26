from api.expenses_api import add_expense_api, get_expenses_api


def save_expense(expense_data):

    try:
        response = add_expense_api(expense_data)
        return True, response

    except Exception as e:
        return False, str(e)


def get_expenses(filters):

    try:
        response = get_expenses_api(filters)
        return True, response

    except Exception as e:
        return False, str(e)
