# Imports
from steps import acquisition as ac
from steps import wrangling as wr
from steps import analysis as an 
# import pandas as pd


# Input
path = './data/vehicles.csv'
input_year = input('Enter a year: ')



# Pipeline 

# Primera fase
dataframe_acquisition = ac.acquisition(path)

# Segunda fase
dataframe_wrangling = wr.wrangling(input_year, dataframe_acquisition)

# Tercera fase
pipeline_end_message = an.analysis(dataframe_wrangling)
print(pipeline_end_message)