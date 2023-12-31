"""
字典：键值对
    1.{}
    2.dict()
        b = dict((['您是',1],[13,890],[1,1])) #{'您是': 1, 13: 890, 1: 1}   #先写元组，再写列表
    空字典 直接写大括号
        print({})   #{}
"""

# a = {
#     '姓名':'s',
#     1:18,
#     (1,3):'123'
# }
#
# b = dict((['您是',1],[13,890],[1,1])) #{'您是': 1, 13: 890, 1: 1}   #先写元组，再写列表
# print(b)
#
# #空字典
# print({})   #{}


"""
字典的操作方法：
    1.get 字典中获取指定的键的值>>-获取值
    2.keys 获取字典中的所有的键，只能获取外层的键 
    3.items 以列表的形式返回字典中所有的键值对
    4.values 以列表的方式返回字典中所有的值
    5.clear 清空字典
    6.copy 创建字典副本，修改原字典对象不会影响副本
    7.formkeys函数用于创建一个新的字典
        参1 一个序列（列表，元组，集合），用于作为字典的键
        参2 任意数据类型，作为每个键的值   #注意：每个键的值是一样的
    8.pop 从字典中移除指定键，返回键对应的值
    9.popitem
        从字典删除最后一项，并以元组形式返回改向所对应的键和值
    10.setdefault   设置默认值
        若该键已经存在，则忽略设置，否则添加该键和值
        倘若键的有相同名字的键，那么只会剩一个键
    11.update 将字典1的值更新到字典1
        若字典2的键在字典1已经存在，则进行修改，否则对字典1添加
"""
# b['您是'] = '小鬼'
# print(b)
# # del b['您是']
# # print(b)
#
# print(b.get('您是'))
# print(b.get('名字'))  #None 没有返回空
# print(b.get('名字', '可恶的家伙')) #可恶的家伙  #没有的话可以给默认值（第二个参数）
# print(b)    #print(b) #不会改变原来的字典
#
#
#
# ddd = {
#     'hao':'chgi',
#     1:1,
#     'en':{
#         '烦死了':'杂鱼',
#         34:88
#     }
# }
# print(ddd.keys()) #dict_keys(['hao', 1, 'en'])   #打印所有的键，只有外层的

# list1 = [1,2,3,4,5,6]
# dic = {}
# dic_o = dic.fromkeys(list1) #此函数有返回值
# print(dic_o)    #{1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
#
# dic_o1 = dic.fromkeys(list1,['a','b','c','大黄']) #{1: ['a', 'b', 'c', '大黄'], 2: ['a', 'b', 'c', '大黄'], 3: ['a', 'b', 'c', '大黄'], 4: ['a', 'b', 'c', '大黄'], 5: ['a', 'b', 'c', '大黄'], 6: ['a', 'b', 'c', '大黄']}
#                                                  #每个键的值是一样的
# print(dic_o1)
#
#
#
# ppd = {'s':1,2:1,3:0,4:999}
# print(ppd)
# print(ppd.pop('s'))  #1
# print(ppd)  ##{2: 1, 3: 0, 4: 999}1