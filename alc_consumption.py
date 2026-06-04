Original file is located at
    https://colab.research.google.com/drive/1pRYJ1YnjCy9vu1yH3pGeo0y8quZrPndK
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data= pd.read_csv('/content/beer-servings.csv')
data.head()

data.head(15)

data.tail(10)

data.columns

data.shape

data.dtypes

data.info()

data.describe()

data.isna()

data.isna().sum()

plt.hist(data['beer_servings'])
plt.title("Distr of Beer Servings Column")
plt.show()

data['beer_servings']=data['beer_servings'].fillna(data['beer_servings'].median())

plt.hist(data['beer_servings'])
plt.title("Distr of Beer Servings Column")
plt.show()

data.isna().sum()

plt.hist(data['spirit_servings'])
plt.title("Distr of Spirit Servings Column")
plt.show()

data['spirit_servings']=data['spirit_servings'].fillna(data['spirit_servings'].median())

data.isna().sum()

plt.hist(data['wine_servings'])
plt.title("Distr of Wine Servings Column")
plt.show()

data['wine_servings']=data['wine_servings'].fillna(data['wine_servings'].median())

data.isna().sum()

plt.hist(data['total_litres_of_pure_alcohol'])
plt.title("Distr of total_litres_of_pure_alcohol")
plt.show()

data['total_litres_of_pure_alcohol']=data['total_litres_of_pure_alcohol'].fillna(data['total_litres_of_pure_alcohol'].median())

data.isna().sum()

"""Detecting Outliers

"""

plt.boxplot(data['beer_servings'])
plt.title("Distr of Beer Servings Column")
plt.show()

plt.boxplot(data['spirit_servings'])
plt.title("Distr of Spirit Servings Column")
plt.show()

plt.boxplot(data['wine_servings'])
plt.show()

plt.boxplot(data['spirit_servings'])
plt.title("Distr of Spirit Servings Column")
plt.show()

q1=np.percentile(data['spirit_servings'],25)
q2=np.percentile(data['spirit_servings'],50)
q3=np.percentile(data['spirit_servings'],75)
print(q1)
print(q2)
print(q3)

data['spirit_servings'].median()

iqr=q3-q1
print(iqr)

up_lim=q3+1.5*iqr
low_lim=q1-1.5*iqr
print(up_lim)
print(low_lim)

outlier=[]
for x in data['spirit_servings']:
  if((x>up_lim) or (x<low_lim)):
    outlier.append(x)
print(outlier)

q1=np.percentile(data['wine_servings'],25)
q2=np.percentile(data['wine_servings'],50)
q3=np.percentile(data['wine_servings'],75)
wine_outlier=[]
wine_outlier.clear()
up_lim=q3+1.5*iqr
low_lim=q1-1.5*iqr
iqr=q3-q1
for x in data['wine_servings']:
  if((x>up_lim) or (x<low_lim)):
    wine_outlier.append(x)
print(wine_outlier)

plt.boxplot(data['wine_servings'])
plt.title("Distr of Wine Servings Column")
plt.show()

plt.boxplot(data['total_litres_of_pure_alcohol'])
plt.title("Distr of total_litres_of_pure_alcohol Column")
plt.show()

"""Encoding"""

#label encoding country
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data['country']=le.fit_transform(data['country'])
data.head()

#One hot encode continent column
data=pd.get_dummies(data,dtype=int)
data.head()

data.shape
