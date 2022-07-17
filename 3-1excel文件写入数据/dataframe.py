import pandas

list_dic = [{'sex': '男', 'age': 12, 'score': 99}, {'sex': '女', 'age': 22, 'score': 69}]

df = pandas.DataFrame(list_dic, index=[1, 2])
print(df)
print("-----------------------------------------------")
dic_list = {'naem': ['Tom', 'Jone', 'LiMing', 'Wang'], 'age': [12, 23, 34, 45]}
df1 = pandas.DataFrame(dic_list, index=['a', 'b', 'c', 'd'])
print(df1)
print("-----------------------------------------------")

series1 = pandas.Series([67, 78, 23], index=['数学', '化学', '物理'])
series2 = pandas.Series([78, 99, 45], index=['数学', '化学', '物理'])
dic = {"小明": series1, "康康": series2}
df2 = pandas.DataFrame(dic)
print(df2)

