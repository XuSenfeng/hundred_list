import numpy.random
import pandas
import numpy
dic = {'sex': "男", 'age':12, 'score':99}
series = pandas.Series(dic)
print(series)

vlist = ['好', 'name', 1, 2, 3]
serie = pandas.Series(vlist)
print(serie)

varray = numpy.random.randint(1, 10, size=5)
seriess = pandas.Series(varray, index=['a', 'b', 'c', 'd', 'e'])
print(seriess)



