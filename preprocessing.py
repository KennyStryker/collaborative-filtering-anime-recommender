import pandas as pd
from text_cleaning import text_cleaning
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os

rating = pd.read_csv('dataset/raw/rating.csv')
anime_df = pd.read_csv('dataset/raw/anime.csv')

#Data Cleaning

null_features = anime_df.columns[anime_df.isna().any()]
anime_df[null_features].isna().sum()
anime_df.dropna(inplace=True)

tqdm.pandas()
anime_df['name'] = anime_df['name'].progress_apply(text_cleaning)