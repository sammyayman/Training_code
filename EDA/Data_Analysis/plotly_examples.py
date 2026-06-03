# Two Simple Plotly Examples
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

print("Creating two simple Plotly examples...")

# Example 1: Simple Line Plot
print("\n1. Creating a simple line plot...")

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Create line plot using plotly.graph_objects
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name='Linear Function'))
fig1.update_layout(
    title='Simple Line Plot: y = 2x',
    xaxis_title='X Values',
    yaxis_title='Y Values',
    template='plotly_white'
)

# Save the plot as HTML file
fig1.write_html('Practice/line_plot.html')
print("Line plot saved as 'line_plot.html'")

# Example 2: Interactive Scatter Plot
print("\n2. Creating an interactive scatter plot...")

# Generate random data for scatter plot
np.random.seed(42)  # For reproducible results
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)
colors = np.random.randn(50)  # For color mapping

# Create scatter plot using plotly.express (easier syntax)
fig2 = px.scatter(
    x=x_scatter, 
    y=y_scatter, 
    color=colors,
    title='Interactive Scatter Plot with Random Data',
    labels={'x': 'X Values', 'y': 'Y Values', 'color': 'Color Scale'},
    color_continuous_scale='viridis'
)

# Add hover information
fig2.update_traces(
    hovertemplate='<b>Point</b><br>' +
                  'X: %{x:.2f}<br>' +
                  'Y: %{y:.2f}<br>' +
                  'Color: %{marker.color:.2f}<extra></extra>'
)

# Save the plot as HTML file
fig2.write_html('Practice/scatter_plot.html')
print("Scatter plot saved as 'scatter_plot.html'")

# Display both plots in the browser
print("\nOpening plots in browser...")
fig1.show()
fig2.show()

print("\nBoth plots have been created and saved as HTML files!")
print("You can also view them interactively in your browser.") 