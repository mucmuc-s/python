# print('abc')
# def add(name,*c):
#     sum=0
#     b=0
#     for i in c:
#         sum+=i
#     b=sum/(len(c))
#     print('%s平均值为:%s'%(name,b))
# add('飞飞',1,2,3,4)
# def func(**h):
#     print(h)
# a={'a':10,'bin':'yes'}
# func(**a)


# b=[3,5,7]
# def func():
#     a=100
#     list=[1,2,3,4]
#     def cun():
#         nonlocal a
#         for i in list:
#             print(i)
#         a+=10
#         for index,m in enumerate(b):
#             b[index]+=10
#         print(a,b)
#     cun()
# func()
def func():
    print('abc')
    def imn():
        print('mmm')
    return imn
p=func()
p()