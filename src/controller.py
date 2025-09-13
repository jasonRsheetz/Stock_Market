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
        data, x_values = self.model.get_current_data(self.view.getSliderValue())
        self.view.update_graph(data, x_values)
        
        # Create and start the timer
        self.timer = threading.Thread(target=self.timer_function, args=(20.0, self.get_timer_driven_data))
        self.timer.daemon = True  # So the thread dies when main program exits
        self.timer.start()
        
        self.graph_trendline()

    def timer_function(self,interval, callback):
        while True:
            time.sleep(interval)
            callback()

    def get_timer_driven_data(self):
        self.model.get_bitcoin_price()
        
        #save data 
        self.model.write_data()
        
        # Generate sample data (replace with actual data source)
        data, x_values = self.model.get_current_data(self.view.getSliderValue())
        
        # work on these commented out lines
        min_x = self.view.get_min_x()

        #graph trendline
        self.graph_trendline()
        
        # Update the view
        self.view.update_graph(data[min_x:len(x_values)], x_values[min_x:len(x_values)])
        
    def on_slider_change(self, value):
        # Update model when slider changes
        data, x_values = self.model.get_graph_min(value)
        
        self.graph_trendline()

        # Update the view
        self.view.update_graph(data, x_values)
        
    def graph_trendline(self):
        slider_value = self.view.getSliderValue()
        # coefficients = self.model.getCoefficientMatrix()
        y_trendline, x_trendline = self.model.makeTrendline(slider_value)
        y_data, x_data = self.model.get_current_data(slider_value)
        y_data = y_data[-len(x_data):]
        self.view.update_graph(y_data, x_data, y_trendline)
        print("")
       
    def calc_r_value(self, min_value=None):
       
        if min_value == None:
            min_value = self.view.getSliderValue()
             
        r_squared = 0
        i = 0;
        residual = 0
        total_variance = 0
                
        y_trendline, x_trendline = self.model.makeTrendline(min_value)
        y_data, x_data = self.model.get_current_data(min_value)
        y_data = y_data[-len(x_data):]       

        mean = np.mean(y_data)
        
        for point in y_trendline:
           
           #find the residual sum of squares, which is y_data - y_trendline squared
           residual += pow(y_data[i] - y_trendline[i] ,2)

           #find total sum of squares, which is y_data - mean of all y_data squared
           total_variance += pow(y_data[i] - mean, 2)
            
           i += 1
        #divide residual ober total and subtract from 1 
        r_squared += 1 - (residual/total_variance) 
        
        return r_squared * 100 
    
    def button_press(self):

        i = 0
        r_value = 0
        temp_r_value = 0
        best_r_value_location = 0
        
        y_data, x_data = self.model.get_current_data(self.view.getSliderValue())
        
        while i < len(x_data) - 50:
            temp_r_value = self.calc_r_value(i)
            
            if temp_r_value > r_value:
                r_value = temp_r_value
                best_r_value_location = i

            i += 1
            
        print()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       