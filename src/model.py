import numpy as np

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