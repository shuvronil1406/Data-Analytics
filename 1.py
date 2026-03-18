import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
# print(df.head())
plt.plot(df[df.columns[0]])
plt.title("Line Plot")
# plt.show()
# 
# bar graph
sns.barplot(x=df.columns[0],y=df.columns[1],data=df)
# plt.show()

sns.histplot(df[df.columns[0]],bins = 10)
# plt.show()

#scatterplot
sns.scatterplot(x='sepal length (cm)',y="sepal width (cm)",data=df)
# plt.show()

#boxplot
sns.boxplot(y="petal length (cm)",data=df)
# plt.show()

#correlation
sns.heatmap(df.corr(),annot=True)
# plt.show()

sns.kdeplot(df['sepal width (cm)'],fill=True)
plt.title("Density Plot")
plt.show()

