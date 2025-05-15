import numpy as np
# from lxml.classlookup import self

class GraphController:
    """Coordinates between Model and View"""
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.counter = 0
        
        # Connect view elements to controller actions
        self.view.set_button_command(self.handle_button_press)
        self.model.init_timer()
        
    def handle_button_press(self):
        """Handle button press event"""
        # Generate sample data (replace with actual data source)
        data, x_values = self.model.get_current_data()
        
        work on these commented out lines
        # min_x = self.view.get_min_x()
        # max_x = self.view.get_max_x()
        
        # Update the view
        self.view.update_graph(data, x_values)
        # self.view.update_graph((max_x - min_x), x_values[min_x:max_x])
