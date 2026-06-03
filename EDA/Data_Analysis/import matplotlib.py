import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

# Sample data
df_bar = pd.DataFrame({'Category': ['A', 'B', 'C', 'D'], 'Values': [23, 45, 56, 78]})
df_line = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': [10, 30, 20, 40]})

# Create a figure with 1 row and 2 columns (Matplotlib + Seaborn only)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Matplotlib Line Plot
axes[0].plot(df_line['X'], df_line['Y'], marker='o', color='blue')
axes[0].set_title('Matplotlib Line Plot')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')

# Seaborn Scatter Plot
sns.scatterplot(x='X', y='Y', data=df_line, ax=axes[1], color='red')
axes[1].set_title('Seaborn Scatter Plot')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')

# Show Matplotlib & Seaborn
plt.tight_layout()
plt.show()

# Plotly Bar Chart in separate window
fig_plotly = px.bar(df_bar, x='Category', y='Values', title='Plotly Bar Chart')
fig_plotly.show()
 