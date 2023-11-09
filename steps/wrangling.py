# Wrangling methods

def wrangling(desired_year, df):
    df = df[df['Year'] == desired_year].reset_index(drop=True)
    return df