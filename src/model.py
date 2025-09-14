import numpy as np
import requests
# import time
# from datetime import datetime
# import threading
# import time


class GraphModel:
    """Manages the data and state of our graph"""
    def __init__(self):
        with open('data.txt', 'r') as file:
            self.data = [int(x) for x in file.read().splitlines()]
    
        self.x_values = np.arange(len(self.data))
    
        self.graph_min = 0
        
    def update_data(self, new_value):
        """Add new data point and update x-axis"""
        self.data.append(new_value)
        self.x_values = np.arange(len(self.data))
        return self.data, self.x_values
    
    def get_current_data(self, _x_min):
        """Return current data state"""
        return self.data, self.x_values[_x_min:]

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
        

    def get_graph_min(self, value):
        return self.data[int(value):len(self.data)], self.x_values[int(value):len(self.data)]
        
        
    def getCoefficientMatrix(self):
        ones = np.ones_like(self.x_values)
        x = np.column_stack((self.x_values, ones))
        inverse = np.linalg.inv(x.T@x)
        B = inverse@x.T@self.data

        return B
        
    def makeTrendline(self, _x_min):
        x = self.x_values[_x_min:]
        A = np.vstack([x, np.ones(len(x))]).T
        y = np.array(self.data[_x_min:])
        linear_coefficients = np.linalg.lstsq(A, y, rcond=None)[0]
        
        non_linear_coefficients = np.polyfit(x, y, 2)
        
        equation = np.ones_like(x)
        i = 0
        
        for value in x:
            equation[i] = non_linear_coefficients[0]*(x[i]**2) + \
            non_linear_coefficients[1]*(x[i]) + \
            non_linear_coefficients[2]

            i+=1

        slope = x*linear_coefficients[0]
        y_offset = np.ones_like(x)*linear_coefficients[1]
        y_trendline = slope + y_offset
        return equation, x
        # return y_trendline, x <- linear solution
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        