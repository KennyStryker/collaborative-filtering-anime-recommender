import pandas as pd
from collections import defaultdict
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

#Anime Genre Count Graph

'''type_count = anime_df['type'].value_counts()

sns.barplot(x=type_count.values,
            y=type_count.index,
            palette='muted').set_title('Anime Types')

plt.tight_layout()
plt.show()'''

all_genres = defaultdict(int)

for genres in anime_df['genre']:
    for genre in genres.split(','):
        all_genres[genre.strip()] += 1


#Save DataFrame
anime_df.to_csv("anime_df.csv")