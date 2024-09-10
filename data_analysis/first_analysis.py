import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../data/anime.csv")

#Data cleaning

#Check for missing values
print(data.isnull().sum())

print(data[data['rating']==-1])
