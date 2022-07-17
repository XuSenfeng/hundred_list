import pandas


series1 = pandas.Series([67, 78, 23], index=['数学', '化学', '物理'])
series2 = pandas.Series([78, 99, 45], index=['数学', '化学', '物理'])
dic = {"小明": series1, "康康": series2}
df2 = pandas.DataFrame(dic)
print(df2)

print(df2.index)
print(df2.values)
print("-----------------")
print(df2[["小明", "康康"]])
print("--------------")
print(df2.loc["物理"])
print(df2.iloc[1])
