"""
成员检测与标识号检测
    in 和 not in运算判断某个对象是否为序列的成员
    in:判断对象是否在序列（列表，字符串，元组，字典）中，在-True
    not in       不在                              True
"""

# a = {1,'2',2,3}
# print('r' in 'fare')    #True
# print(1 in a)   #True
# print(1 not in a)   #False



"""
判断两个对象是否相同，is 和 is not
数字，字符，元组 表面一样>>-完全一样
列表，集合，字典 表面一样>>-其实不一样 其实不是同一个对象
"""
# a = 's'
# b = 's'
# v = 1
# print(a is b)   #True
# print(v is not b) #True
#
#
# print('====================')
# cc = {1,3,4}
# cc_1 = {1,3,4}
# print(cc is cc_1)   #False
#
# cs = {'ss':1,'1':1,1:1}
# cs_1 = {'ss':1,'1':1,1:1}
# print(cs is cs_1)   #False
#
# pp = [1,2,3,4,5]
# pp_1 = [1,2,3,4,5]
# print(pp is pp_1)   #False
#
# pd = (1,2,3,4)
# pd_1 = (1,2,3,4)
# print(pd is pd_1)   #True



"""
python的数据类型转换
    1.字符串型 String
    2.数字类型 Number
        整型 int
        浮点型 float
        布尔型 Bool
    3.表类型 List
    4.元组类型 Tuple
    5.字典类型 Dictionary
    6.集合类型 Set
    
    
    
    
    
    
    
    
#不同类型间不能进行运算
    数据类型转换
        自动类型转换
            不同类型的数据进行运算是，结果会想更高精度进行计算
            精度等级：布尔<整型<浮点型<复数
        强制类型转化
"""



"""
#111111111111111111111111111111111111
数字之间可转换
纯数字的字符串（可带正负号）和数字间可相互转换
布尔型和数字键可以相互转换
其他和数字间不可转换
"""
# a = True
# print(int(a))
# a = 10
# print(float(a)) #10.0
# b = 10.0
# print(int(a))   #10
#
# # c='sssss'
# # print(int(c))   #報錯
# d='1111'
# print(int(d))   #纯数字字符串(可加正负号）可转换
# d='-2'
# print(int(d))
# d='+2'
# print(int(d))

# c = (1,2,4)
# print(int(c))   #报错

# c = {1,2,4}
# print(int(c))   #报错

# c = {1:1}
# print(int(c))   #报错

# c = [1,2,3]
# print(int(c))   #报错





"""
#布尔型转换
#22222222222222222222222
1.容器类型转换布尔型
    容器类型数据：字符串，列表，元组，集合，字典
        空为False
    非容器类型数据：数字类型，布尔类型
2.数字类型转换布尔类型
    int 0-flase 其他true
    float 0.0-flase 其他true
"""

# a = 1
# print(bool(a))
# a = 0
# print(bool(a))

# a = 0.0 #flase
# print(bool(a))
# a = 0.1
# print(bool(a))


########容器类
# a = ''
# b = []
# c = ()
# d = set()
# e = {}
# print(bool(a),bool(b),bool(c),bool(d),bool(e))
# print('#######################################')

"""
list()
    1.数字无法转列表
    2.字符串转列表，会把每个字符当成列表中的元素
    3.元组转列表，会把每个元素当成列表中的元素
    4.字典转列表，只保留键
    5.集合
"""
# b = 'asdg'
# c = [1,23,4]
# e = {1,'a'}
# f = {'s':1,2:6}
# print(list(b),list(c),list(e),list(f))
# d = ('a','b','c')
# print(d)

"""
tuple()
其他类型转元组，和其他类型转列表相同
"""

"""
set()其他类型转集合
    1.数字不能转
    2.字典只留键
    3.总之和其他转列表相同
"""
# b = 'asdg'  #字符串
# c = [1,23,4]    #列表
# e = {1:1,'a':'ssss'}     #字典
# d = (1,1124)
# print(set(b),set(c),set(d),set(e),)


"""
其他转字典
dict()
    1.数字，字符串，集合不能转
    2.列表转，列表必须为等长二级容器，子容器中的元素的个数必须为2
    3.元组转，列表必须为等长二级容器，子容器中的元素个数必须为2
"""
###注意：不能这样写
# a = [1,23,4]
# b = ('a','c')
# print(dict(a),dict(c)

#所谓等长二级容器：列表中套一个列表,里面的列表的元素个数相同必须是两个元素
c = [[1,2],[3,6],[123,567]] #{1: 2, 3: 6, 123: 567}
print(dict(c))
d = ((1,3),('s','sss')) #{1: 3, 's': 'sss'}
print(dict(d))