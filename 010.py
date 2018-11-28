# _*_cofing:UTF-8 _*_

# 定义函数
def compare(par1, par2):
	if (par1 > par2):
		print("大")
	elif(par1 == par2):
		print("等")
	else: 
		print("小")
		
print("------------------------------------")

# 调用函数
compare(100, 20)
compare(111.11, 111.11)
compare(10, 11.1)

print("------------------------------------")

# 变量（Python变量中没有类型） 所有的类型都是对象
a = 10 # 数字
print("a =", a)
a = "Fjun" # 字符串
print("name =", a)
a = (1, 2, 3, 4, 5) # 元组
print("a =", a)
a = [1, 2, 3, 4, 5] # 列表
print("a =", a)
a = {'name': 'Fjun', 'age': 29} # 字典
print('a = ', a)

## 不可变类型
def change(a):
	a = 10

a = 20
change(a)
print('a =', a)

## 可变类型
def change(a):
	a.append(2018)
	
a = [11, 22, 33, 44]
change(a)
print("a =", a)

print("------------------------------------")

# 函数的参数类型
## 必须参数
### 参数数量要对应
def d(arg):
	arg = arg + 1
d(10) #正确
#d() #缺少参数
#d(1,2) #多余参数

### 参数顺序必须一致 
def printPeople(name, sex, age):
	print("name :", name)
	print("sex :", sex)
	print("age :", age)

printPeople("Fjun", "male", 28)
printPeople(28, "Fjun", "male") # 错误的，参数顺序不对应
## 关键字参数

def printPeople(name, sex, age):
	print("name :", name)
	print("sex :", sex)
	print("age :", age)

printPeople(name="Fjun", sex="male", age =28)
printPeople(sex="famale", age=29, name="fanxiao2")
printPeople(age=30, name="xiao2jianghu", sex="male")

print("------------------------------------")

## 默认参数 调用函数时如果没有传递参数，则会使用默认参数
def printPeople(name, sex, age=18):
	print("name :", name)
	print("sex :", sex)
	print("age :", age)

printPeople(name="Fjun", sex="male")

print("------------------------------------")
## 不定长参数
### 定义一个求和参数
def sum(num, *num_list):
	sum = num
	for element in num_list:
		sum += element
	print("sum=", sum)
	
sum(11)
sum(11, 22, 33, 44, 55)

print("------------------------------------")
# return 语句用于退出函数
## 定义一个比较函数

def compare(par1, par2):
	if(par1 > par2):
		return "大"
	elif(par1 == par2):
		return "等"
	else:
		return "小"

res = compare(111, 222)
print("res=", res)

print("------------------------------------")

## 变量作用域  作用域不同的变量不会发生冲突
a = 111 # 全局变量
def sum():
	a = 222 # 局部变量
	print("局部 a =", a)

sum()
print("全局 a =", a)

## 不同的作用域 变量可以分为四种类型： 局部作用域 L(Local)，闭包函数外的函数中 E(Enclosing)，全局作用域 G(Global), 内建作用域 B(Built-in) 使用变量时，会根据作用域进行查找，优先级顺序为：L –> E –> G –>B，即在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找 
