import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/mnt/data/export_cars.csv')

print("First 5 rows of dataset:\n", df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:\n", df.describe(include='all'))

print("\nShape of DataFrame:", df.shape)
print("Data Types:\n", df.dtypes)

print("\nMissing Values:\n", df.isnull().sum())

df.fillna(df.median(numeric_only=True), inplace=True)

plt.figure(figsize=(10,5))
top_makes = df['Make'].value_counts().head(10)
sns.barplot(x=top_makes.index, y=top_makes.values)
plt.title('Top 10 Car Makes')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
