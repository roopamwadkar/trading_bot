import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    order_data = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        order_data["price"] = price
        order_data["timeInForce"] = "GTC"

    logging.info(f"Order Request: {order_data}")

    response = client.futures_create_order(**order_data)

    logging.info(f"Order Response: {response}")

    return response
