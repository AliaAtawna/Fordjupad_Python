import unittest
import pandas as pd
from transform_data import transform_data

class TestETLPipeline(unittest.TestCase):

    def test_transform_data(self):
        # Sample data for testing the transformation
        sample_data = """timestamp,open,high,low,close,volume
        2024-09-19 16:00:00,145.32,146.50,144.90,146.10,2000000
        2024-09-19 15:55:00,144.10,145.50,143.90,145.32,1500000
        """
        transformed_data = transform_data(sample_data)
        
        # Ensure 'price_change' column is created in the transformation process
        self.assertIn('price_change', transformed_data.columns)

if __name__ == '__main__':
    unittest.main()
