import pandas as pd

df = pd.read_csv("D:/Twitter DataSet/DataSet/training.1600000.processed.noemoticon.csv",
                 encoding="latin-1",
                 names=["sentiment", "id", "date", "query", "user", "text"])

print(df.head())
print(df.shape)
print(df['sentiment'].value_counts())
import matplotlib.pyplot as plt

df['sentiment'].value_counts().plot(kind='bar', color=['red', 'green'])
plt.title('Positive vs Negative Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.show()
labels = ['Negative', 'Positive']
sizes = [800000, 800000]
colors = ['red', 'green']

plt.figure()
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Tweet Sentiment Distribution')
plt.show()