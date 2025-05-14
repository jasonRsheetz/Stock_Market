import numpy as np
import requests
import time
from datetime import datetime

class GraphModel:
    """Manages the data and state of our graph"""
    def __init__(self):
        self.data = []
        self.x_values = np.arange(len(self.data))
    
    def update_data(self, new_value):
        """Add new data point and update x-axis"""
        self.data.append(new_value)
        self.x_values = np.arange(len(self.data))
        return self.data, self.x_values
    
    def get_current_state(self):
        """Return current data state"""
        return self.data, self.x_values

    def get_bitcoin_price(self):
        """Fetch Bitcoin price from CoinGecko API"""
        try:
            response = requests.get('https://api.coingecko.com/api/v3/simple/price',
                              params={'ids': 'bitcoin', 'vs_currencies': 'usd'})
            
            if response.status_code == 200:
                response = response.json()
                self.data.append(response['bitcoin']['usd']), self.x_values
                self.x_values = np.arange(len(self.data))
                return self.data, self.x_values
            elif response.status_code == 429:
                return self.data, self.x_values
            else:
                print(f"API error: {response.status_code}")
                return None
            
        except Exception as e:
            print(f"Error fetching price: {str(e)}")
            return None

    def write_data(self):
        try:
            file = open("data.txt", "a")
            file.write(str(self.data[len(self.data)-1]) + '\n')
            file.close()
        except Exception as e:
                print(f"Error opening file: {str(e)}")
        