# Acquisition methods

import pandas as pd 

def acquisition(file_path):
    df_acquisition = pd.read_csv(file_path)
    return df_acquisition