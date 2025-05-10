import tkinter as tk
from model import GraphModel
from controller import GraphController
from view import GraphView


# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    
    # Initialize components
    model = GraphModel()
    view = GraphView(root)
    controller = GraphController(model, view)
    
    # Start the application
    root.mainloop()