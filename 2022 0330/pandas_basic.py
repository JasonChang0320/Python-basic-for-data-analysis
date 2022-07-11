import pandas as pd

df = pd.read_csv('Dataframe/drinks.csv', sep='|')

#常用語法1 :
df.head() 
df.tail() 
df.T
df.dtypes
df.shape
df.values
df.columns
#statistic on each columns
print(df.describe())

#刪除
new_df = df.drop(['total_litres_of_pure_alcohol'], axis=1)
# df.drop(['total_litres_of_pure_alcohol'], axis=1,inplace=True)
new_df.head(10)
#改
new_df['wine_servings'] = new_df['wine_servings']\
        .apply(lambda x: 'high' if x>100 else 'low')
new_df.head()
#增
new_df['alcohol']=df["total_litres_of_pure_alcohol"]

#合併merge
buy={"item":["egg","chicken","apple","milk","basketball"],\
     "counts":[3,1,8,2,1]
     }
market={"product":["cheese","egg","milk","pork","beef","chicken","banana","apple","tennis","basketball"],\
    "price":[50,10,45,60,70,60,30,35,40,100],
    "sample":[1,2,3,4,5,6,7,8,9,10]}

df1=pd.DataFrame(buy)
df2=pd.DataFrame(market)

df3=pd.merge(df1,df2,left_on=["item"],right_on=["product"],how="left", suffixes=["price"])

df3["total"]=df3["counts"]*df3["price"]

#儲存 dataframe
new_df.to_csv("Dataframe/new_drinks.csv")
new_df.to_excel("Dataframe/new_drinks.xlsx")


