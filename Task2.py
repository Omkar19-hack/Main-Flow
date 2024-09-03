import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Dataset Task 2 2.csv')

summary_stats = df.describe()
print("Summary Statistics:\n", summary_stats)

missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values)

df.hist(figsize=(12, 10), bins=30, color='teal')
plt.suptitle('Histograms of Features')
plt.show()

sns.pairplot(df)
plt.suptitle('Pairplot of All Features', y=1.02)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, palette='Set2')
plt.title('Box Plots of All Features')
plt.show()

correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
