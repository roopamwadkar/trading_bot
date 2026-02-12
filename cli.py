import argparse
import logging
from bot.client import get_futures_client
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Binance Futures Demo Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_inputs(args.type, args.quantity, args.price)

        client = get_futures_client()

        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ Order Successful")
        print("---------------------")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Average Price: {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        logging.error(str(e))
        print("\n❌ Order Failed")
        print("Error:", str(e))


if __name__ == "__main__":
    main()
