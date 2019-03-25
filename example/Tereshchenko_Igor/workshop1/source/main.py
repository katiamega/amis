"""
Create function to sum float number
"""
from example.Tereshchenko_Igor.workshop1.source.inputpkg.inputter import inputFloat
from example.Tereshchenko_Igor.workshop1.source.inputpkg.inputter import inputInt
def sum(a,b):
assert isinstance(a,float)
assert isinstance(b,float)
if (a>100.0) (a<-100.0) (b>100.0) (b<-100.0)
    raise ValueError
return a+b

if '_name_' == "_main_":
    a = inputFloat(" Enter float:")
    b = inputFloat(" Enter int:")
    print(sum(1.1,2.3))
sum()