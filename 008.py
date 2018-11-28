# _*_ coding:UTF-8 _*_

# 元组
## 或许还记得之前的列表使用的是[], 元组使用的是() 同一个元组里可以存放任意数据类型
tuple_a1 = ()
tuple_a2 = (11,) # 元组如果只有一个元素，那么后方必须加上逗号,否则会被认为是一个基本数据类型，而不是元组
tuple_a3 = (11,22,33,44,55,66)
tuple_a4 = (1.1101, 3.1415, 2018, 2020, "china", 3+4j, 2018)
tuple_a5 = 22,33,44,55,66

print("tuple_a4[2]元素为 :", tuple_a4[2])
print("tuple_a4[2:5]元素为 :", tuple_a4[2:5])

## 内建方法 求长度：len()、求最大值、max()、最小值min()、统计出现次数count(obj)、index(obj)
tuple_t1 = (1.1101, 3.1415, 2018, 2020, 2018)
print("tuple_t1 :", len(tuple_t1))
print("tuple_t1 :", max(tuple_t1))
print("tuple_t1 :", min(tuple_t1))
print("tuple_t1“2018”元素出现次数为 :", tuple_t1.count(2018),"次")
print("tuple_t1 :", tuple_t1.index(2018))

# 字典
## 键是唯一的，键的值不能改变，数据类型可以是数字，字符串或者元组
## 值不必唯一，值可以是任何数据类型
## 字典使用{} 定义，值用冒号隔开，键值对之间用逗号隔开
### 创建字典
dict1 = {200812050011:"FanJun", 200812050012:"ZYY", 200812050013:"ZB"}
dict2 = {11:"HuBei", 12:"HeiBei", 13:"ChongQing"}
dict3 = {"Excellent":100, "Good":80, "Pass":60, "Fail":50}

### 字典嵌套
dict4 = {"A":["FanXiao2","Xiao2JiangHu"], "B":["XiaoLi","RuHua"]}

print("dict2[11] :", dict2[11])
print("dict3['Excellent'] :", dict3['Excellent'])
print("dict1.get(200812050011) :", dict1.get(200812050011))

### 修改元素
dict3['Fail']: 55
print("dict3[Fail] :", dict3.get('Fail'))

# 集合 特点有三个[确定性，互异性，无序性]
count1 = {"中国", "美国", "俄罗斯"}
count2 = set("中国")
count3 = set()

print("count1 :", count1)
print("count2 :", count2)
print("count3 :", count3)

## 增加、移除元素
setA1 = {"AAA", "BBB", "CCC"}
setA2 = {"DDD", "EEE", "FFF"}
print("setA1 :", setA1)
setA1.add('DDD')
print("setA1.add('DDD)' :", setA1)
setA1.add("AAA")
print("setA1.add('AAA') :", setA1)
setA1.remove('AAA')
print("setA1.remove('AAA') :", setA1)

## 集合运算
### 交集
print("setA1 & setA2 :", setA1&setA2)
### 并集
print("setA1 | setA2 :", setA1|setA2)
### 补集
print("setA1 - setA2 :", setA1 - setA2)

## 队列
### 导入duque
from collections import deque

### 基于列表初始化队列
queue = deque(['AAA','BBB','CCC'])
### 队列尾部添加元素
queue.append('DDD')
print('queue', queue)
### 队列头部添加元素
queue.popleft()
print('queue', queue)

### 重复队列头移除队列（主要看效果）
queue.popleft()
print('queue', queue)