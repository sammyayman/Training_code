import pyodbc
import pandas as pd
import numpy as np
import plotly.express as px

# SQL Server connection parameters
server = 'LAPTOP-O2H5FU1M\\SQLEXPRESS'
database = 'Testdb'

try:
    # Connect to SQL Server
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )
    
    print("✅ Connected to SQL Server!")
    
    # Query to get data
    QUERY = "SELECT * FROM Mydatasheet"
    Raw_DF = pd.read_sql(QUERY, conn)
    print("\n📊 Data loaded successfully!")
    
    # Define a custom color palette for gender
    palette = {'Male': 'darkblue', 'Female': 'darkred'}
    
    # Create an enhanced histogram with plotly
    fig = px.histogram(
        Raw_DF, 
        x="Age", 
        color="Gender",
        color_discrete_map=palette, 
        nbins=5,
        title="Age Distribution by Gender",
        labels={"Age": "Age (years)", "count": "Number of Customers", "Gender": "Gender"},
        opacity=0.8,
        barmode="overlay",  # Overlay bars for better comparison
        marginal="box",     # Add box plot on the margin
        hover_data=["Purchase_Amount_USD", "Previous_Purchases"]  # Show additional data on hover
    )
    
    # Customize the layout
    fig.update_layout(
        template="plotly_white",
        legend_title_text="Gender",
        xaxis_title_font=dict(size=14),
        yaxis_title_font=dict(size=14),
        title_font=dict(size=18),
        hoverlabel=dict(bgcolor="white", font_size=12),
        bargap=0.1
    )
    
    # Add annotations
    fig.add_annotation(
        text="Males tend to have a different age distribution than females",
        xref="paper", yref="paper",
        x=0.5, y=1.05,
        showarrow=False,
        font=dict(size=12)
    )
    
    # Show the interactive plot
    fig.show()
    
    # Save the plot as an HTML file for easy sharing
    fig.write_html('Practice/age_gender_histogram.html')
    print("Histogram saved as 'age_gender_histogram.html'")
    
    # Close connection
    conn.close()
    print("\n✅ Connection closed")
    
except Exception as e:
    print(f"❌ Error: {e}")

"""
ENHANCEMENTS MADE TO THE ORIGINAL PLOTLY HISTOGRAM:

1. Added descriptive title and axis labels
2. Used overlay barmode for better comparison between genders
3. Added a box plot in the margin to show distribution statistics
4. Included hover data to display purchase amount and previous purchases
5. Customized the layout with a clean white template
6. Added an annotation to highlight insights
7. Saved the plot as an HTML file for easy sharing

HOW TO USE:
1. Run this script to generate the enhanced histogram
2. The plot will be displayed in your browser
3. An HTML file will be saved in the Practice directory
4. You can open the HTML file in any browser to view the interactive plot
"""