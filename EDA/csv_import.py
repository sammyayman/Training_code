print('\033[2J')  # Clear terminal screen
import pandas as pd , polars as pl
from IPython.display import display
from io import StringIO
import requests

 
 

# url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
# df = pl.read_csv(url)
# print(df.head())


# url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
# df = pd.read_csv(url)
# display(df.head())

 

# url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# # r = requests.get(url)
# # csv_text = r.text  # raw CSV content

# # df = pd.read_csv(StringIO(csv_text))
# # print(df.head())

#  Contries gdp data

# url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
# df = pl.read_csv(url)
# print(df.head())


#  # Global CO2 emissions data
# url = "https://raw.githubusercontent.com/datasets/co2-fossil-global/master/global.csv"
# df = pd.read_csv(url)
# display(df.head())



# # COVID-19 aggregated data
# url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
# df = pl.read_csv(url)
# print(df.tail())

# World population data
# url =  "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
# df = pd.read_csv(url)
# display(df)

# # Tips dataset from Seaborn
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
 


print(requests.get(url))

df = pl.read_csv(url)
print(df.head())


# Penguins dataset from Seaborn
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
print(requests.get(url))

df = pl.read_csv(url)
print(df.head())


# Flights dataset from Seaborn
url  = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
df = pd.read_csv(url)
display(df.head())

url ="https://mavenanalytics.io/guided-projects/global-video-game-sales"
df = pd.read_csv(url)
print(df.head())