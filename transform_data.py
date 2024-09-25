import pandas as pd
import logging
import io  

def transform_data(data):
    """Bearbetar finansiella data genom att lägga till en kolumn för prisförändringar."""
    try:
        # Använd io.StringIO för att läsa CSV-data
        data = pd.read_csv(io.StringIO(data))
        
        # Beräkna procentuell förändring mellan öppnings- och stängningspriser
        data['price_change'] = (data['close'] - data['open']) / data['open'] * 100
        
        logging.info("Data har bearbetats.")
        return data
    except Exception as e:
        logging.error(f"Fel vid datatransformation: {e}")
        raise
