import logging
from extract_data import fetch_data_from_api
from transform_data import transform_data
from load_data import load_data

# Konfigurera loggning
logging.basicConfig(
    filename='logs/etl_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# API-variabler
API_URL = "https://www.alphavantage.co/query"
API_KEY = "F5M85Y8YVMTZSVW4"  
SYMBOL = "IBM"  # Exempelaktie

def run_pipeline():
    """Kör hela ETL-pipelinen genom att hämta data från ett API."""
    try:
        # Hämta data från API
        data_csv = fetch_data_from_api(API_URL, API_KEY, SYMBOL)

        if data_csv:
            # Bearbeta data
            transformed_data = transform_data(data_csv)

            # Spara bearbetad data
            load_data(transformed_data)

            logging.info("ETL-processen slutförd.")
        else:
            logging.error("Ingen data returnerades från API.")
    except Exception as e:
        logging.error(f"ETL-processen misslyckades: {e}")

if __name__ == "__main__":
    run_pipeline()
