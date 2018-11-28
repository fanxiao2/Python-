# _*_conding:UTF-8 _*_

# 条件控制语句 if-else
a = 10
b = 5

if a >= b:
	print('输出数字 :', a)
else:
	print('输出数字 :', b)

print("-----------------------------------")

a1 = int(input("请输入号码a1 :"))
a2 = int(input("请输入号码a2 :"))

if a1 > a2:
	print('a1大于a2 :', a1)
elif a1 == a2:
	print('a1等于a1 :', a1)
else:
	print('输出数字 :', a2)
	
print("------------------------------------")

## 创建一个学号成绩字典
id_results = {'200812050011': 100, '200812050012': 85, '200812050013': 70}
## 接受从控制台的学号，默认为字符串
stu_id = input("请输入学号 :")
## 删除输入学号尾部的空格
stu_id = stu_id.strip()
## 判断输入的学好是都在字典中
if stu_id in id_results.keys():
	print("你的分数是 :", id_results.get(stu_id))
else:
	print("查无此号!")

print("------------------------------------")

# For循环
### 测试数据
num_test = [12,34,56,78,90,87,65,43,21]
sumOfNum = 0

#遍历列表中的元素，并求和
for element in num_test:
	sumOfNum += element

#求平均值并打印
average = sumOfNum/len(num_test)
print("平均值是: %f"%(average))

for index in range(10):
	print("index", index)
	
# for循环结合range()遍历
## 数据
city = ['WuHan', 'BeiJing', 'ShangHai', 'ShanZhen', 'ChongQing']
## 遍历
for index in range(0, len(city), 2):
	print("city[%d]:%s"%(index, city[index]))

print("------------------------------------")

# while循环
w_num = [12,23,34,45,56,67,78,89]
sumOfNum = 0
index = 0

while index < len(num_test):
	sumOfNum += num_test[index]
	index +=1

## 求平均值
average = sumOfNum/len(num_test)
print("平均值是:%f"%(average))

print("------------------------------------")

# break 跳出循环体
## 测试数据
num_t1 = [12,34,56,78,90,98,76,54,32]
for i in range(len(num_t1)):
	if num_t1[1] < 30:
		print("拜拜")
		break
	else:
		print(num_t1[i])
	
## 开发中可能会常用到的是while与break结合	
while True:
	a = input('请输入数字 :')
	if int(a) > 80:
		print('对头')
		break
	else:
		print("小了")

print("------------------------------------")
		
## continue 语句 是break的对头 不会退出循环体
num_t2 = [12,34,56,78,90,98,76,54,32]
for i in range(len(num_t2)):
	if num_t2[i] < 50:
		print("欧了")
		continue
	print(num_t2[i])
	
print("------------------------------------")
	
## 空语句 pass语句，主要用于占位
num_t3 = [12,34,56,78,90,98,76,54,32]
for i in range(len(num_t3)):
	if num_t3[i] < 60:
		print("好勒")
	else:
		pass