import requests

def fetch_crypto_prices(crypto_id="bitcoin"):
    """
    Fetches the current price and 24h change for a specified cryptocurrency.
    """
    # API Endpoint for CoinGecko
    url = f"https://api.coingecko.com/api/v3/simple/price"
    
    # Parameters for the GET request
    params = {
        'ids': crypto_id,
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }

    try:
        # 1. Use the requests library to make a GET request
        response = requests.get(url, params=params)

        # Check if the request was successful (Status Code 200)
        response.raise_for_status()

        # 2. Parse the fetched data (JSON format)
        data = response.json()

        # 3. Handle cases where the API returns an empty dictionary (invalid crypto ID)
        if not data:
            print(f"Error: Could not find data for '{crypto_id}'.")
            return

        # Extract specific fields
        price = data[crypto_id]['usd']
        change = data[crypto_id]['usd_24h_change']

        # Display the data in a user-friendly format
        print("-" * 30)
        print(f"CRYPTO REPORT: {crypto_id.upper()}")
        print("-" * 30)
        print(f"Current Price: ${price:,.2f}")
        print(f"24h Change:    {change:.2f}%")
        print("-" * 30)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the internet.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

if __name__ == "__main__":
    # Example usage: fetch Bitcoin data
    fetch_crypto_prices("bitcoin")
