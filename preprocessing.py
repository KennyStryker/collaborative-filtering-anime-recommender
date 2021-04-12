import pandas as pd
import numpy as np

anime_raw_data = pd.read_csv("dataset\\raw\\anime.csv")
rating_raw_data = pd.read_csv("dataset\\raw\\rating.csv")

print(anime_raw_data.head())