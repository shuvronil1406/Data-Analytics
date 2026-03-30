import pandas as pd
# print(pd.__version__)
# data=[100,200,300,400,500]
# print(pd.Series(data)) #gives labelled data from position 0
# print(pd.Series(data,index=['a','b','c'])) #index makes the label as per our choice
# print(pd.Series(data,index=[1,0,1])) 
# series = pd.Series(data,index=['a','b','c','d','e'])
# print(series.loc['a']) #loc -> get location using label
# series.loc['c']=500 #loc can be used to access and modify an element

# print(series.iloc[0]) #location by integer label , same as array indexing.
# print(series[(series<300) | (series>400)])

# calories = {"Day 1": 2500, "Day 2": 1780, "Day 3": 1500, "Day 4": 2100}
# series_cal = pd.Series(calories)
# print(series_cal[series_cal>=2000])
# print(series_cal.loc["Day 1"])
# series_cal.loc["Day 3"]+=500
# print(series_cal)
# print(series_cal[series_cal>=2000])
# print(series_cal.iloc[3])

#DATAFRAMES:-

data = {
    "Name": ["Spongebob","Patrick","Squidward"],
    "Age" : [30,35,50]
}
df = pd.DataFrame(data,index=["Employee 1","Employee 2","Employee 3"])
# print(df.loc["Employee 2"])
# print(df.iloc[2])

#add a new column
df["Job"]=["Cook","N/A","Cashier"]
# print(df)
# print(df["Job"].iloc[0]) #Accessing job of a specific employee

#add a new row
new_row=pd.DataFrame([{"Name": "Henry", "Age": 25,"Job": "Student"}],index=["Employee 4"])
df=pd.concat([df,new_row] )
# print(df)
# add new rows
new_rows = pd.DataFrame([{"Name": "Robert", "Age": 45,"Job": "Scientist"},
                         {"Name": "Alex", "Age": 25,"Job": "Engineer"}],index=["Employee 5","Employee 6"])
df =pd.concat([df,new_rows])
print(df)



