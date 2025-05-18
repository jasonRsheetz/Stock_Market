import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphView:
    """Handles visualization using Matplotlib in Tkinter"""
    def __init__(self, root):
        self.root = root
        self.root.title("MVC Graph Example")
        
        # Create main container
        self.container = tk.Frame(root)
        self.container.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Setup matplotlib figure
        self.fig = Figure(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.container)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Setup button
        self.button = tk.Button(self.container, text="Update Graph")
        self.button.pack(pady=5)
        
        #setup input boxes
        min_value_string = tk.StringVar(value="0")
        self.min_x = tk.Entry(self.container, textvariable=min_value_string)
        self.min_x.pack(pady=5)
        
        
        self.last_slider_length = 0
        
        # Create horizontal slider
        self.horizontal_slider = tk.Scale(
            root,
            from_=0,
            to=1100,
            orient='horizontal',
            length=300,  # Set desired length in pixels
            command=self._on_slider_change
            )
        self.horizontal_slider.pack(pady=5, expand=True)

        # Initialize plot
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot([], [])
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.ax.grid(True)
    
    def update_graph(self, data, x_values):
        """Update the displayed graph"""
        self.line.set_xdata(x_values)
        self.line.set_ydata(data)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()
        print(len(data))
        
        if len(data)> self.last_slider_length:
            self.last_slider_length = len(data)
            self.horizontal_slider.configure(to=len(data))
        
    def get_min_x(self):
        
        min_value = int(self.min_x.get())
        return min_value

    def show_values(self):
        # Update labels with current values
        self.h_value.set(f"Horizontal: {self.horizontal_var.get():.1f}")
        

    def _on_slider_change(self, value):
        # Notify controller of slider change
        self.controller.on_slider_change(int(value))
        
        
        