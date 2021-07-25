import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt
import sys 

def load_and_process(impacts):
                     
    # Method Chain 1 (Load Data, Rename Columns, Drop Unused Column)

    impacts = (pd.read_csv("impacts.csv")
           .rename(columns= {"Object Name": "Asteroid Name",
           "Period Start": "Risk Period Start", 
           "Period End": "Risk Period End",
           "Asteroid Velocity": "Asteroid Velocity (Km/s)",
           "Asteroid Magnitude": "Asteroid Apparent Magnitude"})
           .drop(['Maximum Torino Scale'], axis=1)
     )
    
    # Method Chain 2 (Sort Values, Index Asteroid Name, Retrieve rows from index)
                     
    impacts = (
           impacts
          .sort_values(by='Risk Period Start', ascending=True)
          .loc[0:648]
    )
