import numpy as np
import pandas as pd

 # Method Chain 1
    
def load_and_process(url_or_path_to_csv_file):
    df1 = (pd.read_csv(url_or_path_to_csv_file).dropna()
          .reset_index(drop=True)  
          .rename(columns={"Period Start": "Risk Period Start", "Period End": "Risk Period End", "Object Name": "Asteroid Name"})
          .rename(columns={"Asteroid Velocity": "Asteroid Velocity (km/s)", "Asteroid Magnitude": "Asteroid Magnitude (au)"})
    )

    # Method Chain 2 

    df2 = (
          df1
          .drop(['Maximum Torino Scale'], axis=1)
          .sort_values(by='Risk Period Start', ascending=True)
    )

    # Return the latest dataframe

    return df2