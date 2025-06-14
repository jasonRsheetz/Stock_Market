import numpy as np
import time
from datetime import datetime
import threading
import time

class GraphController:
    """Coordinates between Model and View"""
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self  # Reference back to controller
        self.counter = 0
        
        # Connect view elements to controller actions
        # self.view.set_button_command(self.handle_button_press)
        
        # Set initial graph
        data, x_values = self.model.get_current_data()
        self.view.update_graph(data, x_values)
        
        # Create and start the timer
        self.timer = threading.Thread(target=self.timer_function, args=(20.0, self.get_timer_driven_data))
        self.timer.daemon = True  # So the thread dies when main program exits
        self.timer.start()
        
    def timer_function(self,interval, callback):
        while True:
            time.sleep(interval)
            callback()

    def get_timer_driven_data(self):
        self.model.get_bitcoin_price()
        
        #save data 
        self.model.write_data()
        
        # Generate sample data (replace with actual data source)
        data, x_values = self.model.get_current_data()
        
        # work on these commented out lines
        min_x = self.view.get_min_x()
        
        # Update the view
        self.view.update_graph(data[min_x:len(x_values)], x_values[min_x:len(x_values)])
        
    def on_slider_change(self, value):
        # Update model when slider changes
        data, x_values = self.model.get_graph_min(value)
        
        # Update the view
        self.view.update_graph(data, x_values)
        
        
    def button_press(self):
        slider_value = self.view.getSliderValue()
        # coefficients = self.model.getCoefficientMatrix()
        y_trendline, x_trendline = self.model.makeTrendline(slider_value)
        y_data, x_data = self.model.get_current_data()
        self.view.update_graph(y_data, x_data, y_trendline)
        print("")
        
        
        
        