def validate_inputs(order_type, quantity, price):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("LIMIT order requires --price")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
