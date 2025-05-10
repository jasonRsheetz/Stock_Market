import numpy as np
import matplotlib.pyplot as plt



# # Set random seed for reproducibility
# np.random.seed(42)
#
# # Generate sample data
# prices = generate_stock_prices()
#
# # Create figure with larger size for better readability
# plt.figure(figsize=(12, 6))
#
# # Plot price movement
# plt.plot(prices, linewidth=1.5, label='Stock Price')
#
# # Customize appearance
# plt.title('Simulated Stock Price Movement', fontsize=14, pad=20)
# plt.xlabel('Trading Days', fontsize=12)
# plt.ylabel('Price ($)', fontsize=12)
# plt.grid(True, alpha=0.3)
# plt.legend(fontsize=10)
#
# # Add horizontal line at starting price
# plt.axhline(y=prices[0], color='r', linestyle='--', alpha=0.5, 
#            label=f'Starting Price (${prices[0]:.2f})')
#
# # Calculate and annotate key statistics
# stats_text = f'''
# Initial Price: ${prices[0]:.2f}
# Final Price:   ${prices[-1]:.2f}
# Max Price:     ${max(prices):.2f}
# Min Price:     ${min(prices):.2f}
# '''.strip()
#
# plt.text(0.02, 0.98, stats_text,
#          transform=plt.gca().transAxes,
#          verticalalignment='top',
#          bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
#          fontsize=10)
#
# plt.tight_layout()
# plt.show()