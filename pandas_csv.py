import pandas as pd
# f=open("data.csv")
df = pd.read_csv("data.csv",index_col=["Name"])  #index_col used to set the labels as "Name", helps in selection by row
# print(df)
# print(df.to_string()) 
# SELECTION BY COLUMN
# print(df["Name"].to_string())
# print(df[["Name","Height","Weight"]])

# SELECTION BY ROW:- 
# print(df.loc["Pikachu"])  # gives all the properties of row named "Pikachu"
# print(df.loc["Pikachu", ["Height", "Weight"]])
#print(df.iloc[:5:2, :5:2])  #slicing based on rows and columns

#FILTERING:-
# taking the row that match a condition
# tall = df[df["Height"]>=2]
# heavy = df[df["Weight"]>150]
# legendary_pk=df[df["Legendary"]==True]
# ff_pok=df[(df["Type1"]=="Fire") & (df["Type2"]=="Flying")]
# print(ff_pok)

#Aggregate funtions: used to reduce a set of values into a single summary value. Used to summarise and analyse data.
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.count())

#Single Column:-
# print(df["Height"].mean())
# print(df["Height"].max())

#group by

# group = df.groupby("Type2")
# print(group["Height"].mean())
# group2= df.groupby("Type1")
# print(group2["Weight"].max())

#Data Cleaning:-
# df= df.drop(columns=["Legendary","No"])
# print(df.to_string())
# df = df.dropna(subset=["Type2"]) #dropna-> dropnotavailable, drops the rows where Type2 value is NaN
# print(df.to_string())
#replace the NaN with something instead of dropping the row
# df = df.fillna({"Type2": "None"})
# print(df)

#Fix Inconsistent Values:-
# df["Type1"]=df["Type1"].replace({"Grass": "GRASS",
                                #  "Fire":"FIRE",
                                #  "Water":"WATER"})
# print(df.to_string())
#remove duplicates:-

# df = df.drop_duplicates()
# print(df.to_string())
#fix data types:
# df["Legendary"]=df["Legendary"].astype(bool)
# print(df.to_string())
# 