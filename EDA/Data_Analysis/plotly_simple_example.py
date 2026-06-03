# Simple Plotly Examples - Basic Charts
import plotly.express as px

# ============================================
# Example 1: Simple Bar Chart
# ============================================
print("Creating Bar Chart...")

categories = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Mangoes']
values = [45, 32, 28, 50, 38]

fig_bar = px.bar(
    x=categories,
    y=values,
    title='Fruit Sales',
    labels={'x': 'Fruits', 'y': 'Sales'},
    color=values,
    color_continuous_scale='Blues'
)
fig_bar.show()

# ============================================
# Example 2: Simple Line Chart
# ============================================
print("Creating Line Chart...")

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temperature = [10, 12, 18, 22, 28, 32]

fig_line = px.line(
    x=months,
    y=temperature,
    title='Monthly Temperature',
    labels={'x': 'Month', 'y': 'Temperature (°C)'},
    markers=True
)
fig_line.show()

# ============================================
# Example 3: Simple Pie Chart
# ============================================
print("Creating Pie Chart...")

languages = ['Python', 'JavaScript', 'Java', 'C++', 'Other']
users = [40, 25, 20, 10, 5]

fig_pie = px.pie(
    values=users,
    names=languages,
    title='Programming Language Usage'
)
fig_pie.show()

# ============================================
# Example 4: Simple Scatter Plot
# ============================================
print("Creating Scatter Plot...")

# Sample data
study_hours = [2, 3, 4, 5, 6, 7, 8, 5, 6, 7, 3, 4, 8, 9, 6]
exam_scores = [60, 65, 70, 75, 80, 85, 90, 72, 78, 88, 68, 73, 92, 95, 82]

fig_scatter = px.scatter(
    x=study_hours,
    y=exam_scores,
    title='Study Hours vs Exam Scores',
    labels={'x': 'Study Hours', 'y': 'Exam Score'},
    trendline='ols'  # Add trendline
)
fig_scatter.show()

print("\nAll plots created successfully!")
print("Hover over the charts to see interactive features.")
