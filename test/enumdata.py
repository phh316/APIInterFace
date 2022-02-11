# def A():
#     a = 25
#     def B(x):
#         return a * x * x
#     return B
# a = 10
# s = A()
# print(s(2))
# def f1(a):
#         def f2(b):
#                 nonlocal a
#                 new_val = a + b
#                 a = new_val
#                 return new_val
#         return f2
# s = f1(0)
# print(s(3))
# print(s(5))
# print(s(6))

# a = [1,2,3,4,5,6,7,8,9]
# def f1(x):
#         return x * x
# f = map(f1,a)
# a = map(lambda x:x * x,a)
# print(list(f))
# print(list(a))



# a = [1,2,3,4,5,6,7,8,9]
# b = [1,2,3,4,5,6,7,8,9]
# f = map(lambda x,y:x+y,a,b)
# print(list(f))
#
# a = [1,2,3,4,5,6]
# b = [1,2,3,4,5,6,7,8,9]
# f = map(lambda x,y:x+y,a,b)
# print(list(f))

from functools import reduce

# a = [1,2,3,4,5,6,7,8,9]
# r = reduce(lambda x,y:x + y,a)
# #(((((((1+2)+3)+4)+5)+6)+7)+8)+9
# print(r)

# a = [1,2,3,4,5,6,7,8,9]
# r = filter(lambda x:True if x >1 else False,a)
# b = ['a','B','c','D','f','D']
# r = filter(lambda x:True if x >1 else False,B)
# print(list(r))



import time
def log(func):
    def get_time(*name,**kwargs):
        print(time.time())
        func(*name,**kwargs)
    return get_time

@log
def f1(fun_name,fun_name2,**kwargs):
    print("this is a function "+fun_name +' '+fun_name2+' '+str(kwargs))
f1('001','002',a=1,b=2,c=3)









