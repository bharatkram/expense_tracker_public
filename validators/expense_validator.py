def validate_expense(expense_data):

    errors = []

    if not expense_data["seller"]:
        errors.append("Seller / Merchant is required")

    if expense_data["amount"] <= 0:
        errors.append("Amount must be greater than 0")

    if not expense_data["category"]:
        errors.append("Please select a category")

    return errors
