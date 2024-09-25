import pandas as pd
import logging

def load_data(data, output_file='data/processed_data.csv'):
    """Sparar bearbetad data till en CSV-fil."""
    try:
        data.to_csv(output_file, index=False)
        logging.info(f"Bearbetad data sparad till {output_file}")
    except Exception as e:
        logging.error(f"Fel vid sparning av data: {e}")
        raise
