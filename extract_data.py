import requests
import logging

def fetch_data_from_api(api_url, api_key, symbol):
    """Hämtar finansiella data från Alpha Vantage API."""
    try:
        url = f"{api_url}?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}&datatype=csv"
        response = requests.get(url)

        if response.status_code == 200:
            logging.info(f"Data hämtad från API för symbolen {symbol}")
            return response.text  # Returnerar CSV-data som text
        else:
            logging.error(f"API-anrop misslyckades med statuskod {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Fel vid API-anrop: {e}")
        raise
