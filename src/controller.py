import numpy as np

class GraphController:
    """Coordinates between Model and View"""
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.counter = 0
        
        # Connect view elements to controller actions
        self.view.set_button_command(self.handle_button_press)
    
    def handle_button_press(self):
        """Handle button press event"""
        # Generate sample data (replace with actual data source)
        self.counter += 1
        data, x_values = self.model.update_data(np.sin(self.counter))
        
        # Update the view
        self.view.update_graph(data, x_values)