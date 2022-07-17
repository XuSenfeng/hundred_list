import pandas

dic = {'sex': '男', 'age': 12, 'score': 99}
series = pandas.Series(dic)

print(series[0:1])
print("--------------------")
print(series[:'age'])

