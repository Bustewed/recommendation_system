import networkx as nx
import pandas as pd


df = pd.read_csv("data/anime.csv")
# print(df.head())

df2 = pd.read_csv("data/rating.csv")
print(df2.head())


G = nx.Graph()
G.add_nodes_from(df2['user_id'])
G.add_nodes_from(df2['anime_id'])
G.add_edges_from(zip(df2['user_id'], df2['anime_id'],df2['rating']))

G.add_nodes_from(df['genre'].unique(), bipartite=2)
for _,row in df.iterrows() :
    G.add_edge(row['anime_id'], row['genre'])