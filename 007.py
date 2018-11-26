# _*_ coding:UTF-8 _*_

# 创建3个不同的列表，同一个列表 中可以存放任意基本数据类型
list1 = [1,2,3,4,5,6,7,8];
list2 = ["BeiJing","ShangHai","WuHan","ChengDu","ShenZhen"];
list3 = [3.1415, 2.1314, 521, 2018, 2040, "China", 3+4j];
list4 = []

## 通过索引下标访问列表中元素 (查)
print("list1[5]元素为 :", list1[5])
print("list2[2]元素为 :", list2[2])
print("list3[3]元素为 :", list3[3])
print("list4元素为 :", list4)

## 通过下标访问多个元素
print("list2[0]+list3[3]元素为 :", list2[0], "+", list3[3])

## 改
print("list2[2] 元素为 :", list2[2])
list2[2] = "ChongQing"
print("更改后的list2[2] 元素为:", list2[2])

## 删
print("修改前的list3元素为 :", list3)
del list3[2]
list3.remove(3+4j)
print("删除后的list3元素为 :", list3)
list3.clear()
print("清空列表之后元素为 :", list3)

## 增
### 1. append(object): 添加新元素，并将元素添加到列表末尾
### 2. insert(index, oject): 插入新元素到指定索引位置

list3.append("Hello List3")
list3.insert(1, "Hello Python List")
print("增加后的list3", list3)

# 列表内建函数

listtest = [2011, 2013, 2015, 2017 ,2019, 2011];
## 求列表长度（元素个数）
print("listtest长度 :", len(listtest))
## 求元素最大值
print("listtest最大值 :", max(listtest))
## 求元素最小值
print("listtest最小值 :", min(listtest))
## 统计元素在列表中出现的次数
print("2011在listtest出现次数为 :",  listtest.count(2011))
## 找出列表中某个值第一个匹配项的索引位置
print("2011在listtest中第一个值的索引位置  :", listtest.index(2011))
## 复制一个现有列表
listt2 = listtest.copy()
print("listt2 :", listt2)
## 反转列表
listtest.reverse()
print("反转后的listtest :", listtest)

# 列表常用操作
lista1 = [1,2,3,4,5]
lista2 = [6,7,"ShangHai",8,9]
## 拼接
print("lista1 + lista2 :", lista1 + lista2)
## 乘法
print("lista1  * 2:", lista1 * 2)
## 迭代
for element in lista1:
	print(element)
	
## 判断元素是否存在于列表中
print("2是否在lista1中 :", 2 in lista1)
print("10是否在lista2中 :", 10 in lista2)
## 嵌套

lista3 = [lista1, lista2]
print("lista3:", lista3)

# 栈
## append(obj): 添加元素到列表尾部
## pop(): 从列表尾部取出元素

listp1 = [1,2,3,4,5,6]
### 向尾部添加元素
listp1.append(168)
print("listp1 :", listp1)

### 从尾部取出元素
print("listp1尾部元素为 :", listp1.pop())