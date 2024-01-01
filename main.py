import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



df1 = pd.read_csv("tmdb_5000_credits.csv")
df2 = pd.read_csv("tmdb_5000_movies.csv")

df1.columns = ["id", "title", "cast", "crew",]
df2 = df2.merge(df1, on="id")

C = df2["vote_average"].mean()
m = df2["vote_count"].quantile(0.9)
q_movies = df2.copy().loc[df2["vote_count"] >= m]

def weighted_rating(X, m=m, C=C):
  v = X["vote_count"]
  R = X["vote_average"]

  return (v/(v+m)*R)+(m/(v+m)*C)

q_movies["score"] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values("score", ascending=False)

features = ["cast", "crew", "keywords", "genres"]
for feature in features:
  df2[feature] = df2[feature].apply(literal_eval)

def get_director(x):
  for i in x:
    if i["job"] == "Director":
      return i["name"]
  return np.nan

df2["director"] = df2["crew"].apply(get_director)

def get_list(x):
  if isinstance(x, list):
    names = [i["name"] for i in x]
    return names
  return []

features = ["cast", "keywords", "genres"]
for feature in features:
  df2[feature] = df2[feature].apply(get_list)

def clean_data(x):
  if isinstance(x, list):
    return [str.lower(i.replace(" ", "")) for i in x]
  else:
    if isinstance(x, str):
      return str.lower(x.replace(" ", ""))
    else:
      return ""

features = ["cast", "keywords", "genres"]
for feature in features:
  df2[feature] = df2[feature].apply(clean_data)

def create_soup(x):
  return ' '.join((x['keywords'])) + ' ' + ' '.join((x['cast'])) + ' ' + str(x['director']) + ' ' + ' '.join(x['genres'])

df2["soup"] = df2.apply(create_soup, axis = 1)

count = CountVectorizer(stop_words = "english")
count_matrix = count.fit_transform(df2["soup"])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
df2 = df2.reset_index()
indices = pd.Series(df2.index, index = df2["original_title"])

def get_recommendation(title, cosine_sim):
  idx = indices[title]
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse = True)
  sim_scores = sim_scores[1:11]
  movie_indices = [i[0] for i in sim_scores]
  return df2["original_title"].iloc[movie_indices]

print(get_recommendation(input("Enter a movie youve watched"), cosine_sim2))

def find_titles_in_csv(target_title):
    target_title_lower = target_title.lower()
    df1['title_lower'] = df1['title'].str.lower()

    matching_titles = df1[df1['title_lower'].str.contains(target_title_lower)]['title'].tolist()

    return matching_titles

#use below function to search movies in dataset
#find_titles_in_csv("Rush")