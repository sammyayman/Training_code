import plotly.express as px

palette = {'Male': 'darkblue', 'Female': 'darkred'}

fig = px.histogram(Raw_DF, x="Age", color="Gender",
                   color_discrete_map=palette, nbins=5)
fig.show()