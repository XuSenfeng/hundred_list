import pandas as pd
from pandas import Series, DataFrame
import numpy as np

emp_info = DataFrame(data={'姓名': ["张三", '李四', '王五', '赵六'],
                           '物理': np.random.randint(0, 100, size=4),
                           '化学': np.random.randint(0, 100, size=4),
                           '数学': np.random.randint(0, 100, size=4),
                           '生物': np.random.randint(0, 100, size=4)}, index=range(1, 5))
# print(emp_info)

emp_info.to_excel("./test.xlsx")

vfile = pd.read_excel("./test.xlsx", index_col=0)

print("----------------------")
# print(type(vfile))
# print(vfile.index)

df = pd.DataFrame(vfile)
print(df)

sum_score = df.sum()
print(sum_score)
sum_score = df.sum(axis=1, numeric_only=True)
emp_info["总分"] = sum_score
avg_score = df.mean(axis=1, numeric_only=True)
emp_info['平均分'] = avg_score
emp_info.to_excel("./test.xlsx")



