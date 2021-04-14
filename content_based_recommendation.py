import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#Import
anime_df = pd.read_csv('anime_df.csv')

#Vectorization
genres_str = anime_df['genre'].str.split(',').astype(str)

tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 4), min_df=0)
tfidf_matrix = tfidf.fit_transform(genres_str)