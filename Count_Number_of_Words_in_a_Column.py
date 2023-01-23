# Data science professionals use the pandas library for data handling and preparation. 
# The pandas library doesn’t have any method to count the number of words in a piece of text. 
# One way to solve this problem is by finding the length of the text by splitting the complete text.

# Import a textual dataset that can count the number of words in a column:
import pandas as pd 
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding = 'latin1')
print(data.head())

# Dataset has two columns Article and Title.
# Creating a new column as the number of words in the article column:
data["number of Words"] = data["Article"].apply(lambda n: len(n.split()))
print(data.head())