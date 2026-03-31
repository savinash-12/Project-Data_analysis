import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('airbnb_data_set.csv')
print(df.columns)

#check any missing value
print(df.isnull().sum())
#changing the data type of last review
df['last review'] =pd.to_datetime(df['last review'], errors='coerce')
print(df.info())
#add reviews per month with 0 value and last review with minimum value
df.fillna({'reviews per month' : 0, 'last review' : df['last review'].min()},inplace=True)
#remvoing the data NAME and host name
df.dropna(subset=['NAME','host name'], inplace=True)

print(df.isnull().sum())

#deleting the unwanted column
#df = df.drop(columns=['license','house_rules'],errors ='ignore')
cols = ['house_rules','license']
df.drop(cols, axis=1, inplace=True)
print(df.columns)

#remove dollar sign in price
# df['price'] = (
#     df['price']
#     .astype(str)
#     .str.replace(r'[\$,]', '', regex=True)
#     .astype(float)
# )
# df['service fee'] = (
#     df['service fee']
#     .astype(str)
#     .str.replace(r'[\$,]', '', regex=True)
#     .astype(float)
# )
df['price'] = df['price'].replace('[\$,]','', regex=True).astype(float)
df['service fee'] =df['service fee'].replace('[\$,]','',regex=True).astype(float)
print(df['service fee'])

#remove duplicates
df.drop_duplicates(inplace=True)

#descriptive statics
print(df.describe())

#visulaization and result
#What is the distribution of listing prices?

# plt.figure(figsize = (10,6))
sns.histplot(df['price'],bins=50,kde=True, color ='red')
plt.title("Distribution of listing price")
plt.xlabel('Price  $')
plt.ylabel('Frequency')
plt.show()

# #How are different room types distributed?
plt.figure(figsize = (8,5))
sns.countplot(x ='room type',data =df, color ='hotpink')
plt.title("Distribution of room type")
plt.xlabel('Room type')
plt.ylabel('Count')
plt.show()

# #How are listing distributed across different neighborhoods?
plt.figure(figsize = (12,8))
sns.countplot(y ='neighbourhood group',data =df, color ='lightgreen',order=df['neighbourhood group'].value_counts().index)
plt.title("Number of Listing by Neighborhood Group")
plt.xlabel('Count')
plt.ylabel('Neighborhood Group')
plt.show()

# What is the relationship between price and room type?
plt.figure(figsize = (10,6))
sns.boxplot(x='room type',y = 'price',data = df, hue ='room type', palette='Set1')
plt.title("Price vs. Price")
plt.xlabel('Room type')
plt.ylabel('Price ($)')
plt.legend(title ='Room type')
plt.show()

#How has the number of reviews change over with time
df['last review'] = pd.to_datetime(df['last review'])
reviews_over_time = df.groupby(df['last review'].dt.to_period('M')).size()
plt.figure(figsize = (12,6))
reviews_over_time.plot(kind='line', color = 'red')
plt.title('Number of Reviews Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Reviews')
plt.show()