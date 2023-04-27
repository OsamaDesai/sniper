import pandas as pd

data = pd.read_csv("C:/Users/nnair/Downloads/exp3 (data  preprocessing and storing) - facebook-liverpool.csv")

#1) finding missing data
print(data.isnull().sum())

#2) drop missing data
remove = ['image','video','video_thumbnail','video_id','link']
data.drop(remove,inplace=True,axis=1)

#After dropping data : 
print(data.isnull().sum())

#3) Inputting missing values
data['text'] = data['text'].fillna('No text')
print(data.isnull().sum())

#4) Drop duplicates
data.drop_duplicates()
print(data)

#5) normalize casing
print(data['text'])
data['text'] = data['text'].str.lower()
print('\n\nAfter Normalizing Casing')
print(data['text'])

#6) Renaming Columns
new_name={'likes':'no. of likes',
'comments':'no. of comments',
'shares':'no. of shares'}
data.rename(columns=new_name, inplace=True)

#7) Truncate Rows
data = data.truncate(before=1,axis=0,copy=True)
print('\n\nAfter Truncating Rows')
print(data['text'])

#8) Saving Cleaned Data
data.to_csv('cleaned_facebook_liverpool.csv', index=False)
print("\n\nCleaned Data Stored Successfully")