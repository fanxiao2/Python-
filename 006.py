# _*_ conding:UTF-8 _*_

strone = "hello world !"
strtwo = "welcome to the world of python !"

## 访问字符串中的单个字符或者子串
print('strone: ', strone)
print('strtow: ', strtwo )
print('strtwo[1]: ', strtwo[1])
print('strtwo[0:6]: ', strtwo[0:7])
print('strtwo[23:29]: ', strtwo[24:30])

# 修改字符串

## 字符串拼接
strone = strone + strtwo
print('拼接后的strone: ', strone)

## 替换字符串
strone = strone.replace(strtwo, "My Name is Fjun !")
print('替换后的strone: ', strone)

## 字符串截取
print('strone[0:6]:', strone[0:6])

## 字符串复制
print('strone * 2 :\n' ,strone *2)

## 判断字符串是否包含对应字符 (返回True或False)
print("world 是否在strone字符串中 :", 'world' in strone)
print("Good 是否在strtwo字符串中 :", 'Good' in strtwo)

# 字符串内建函数
strt1 = "  hello world! hello"
strt2 = "hello"
## 返回字符串长度: len(str)
print('strt1字符串长度 :', len(strt1))
## 分割字符串：split(str)
print('strt1以空格分开的效果: ', strt1.split('  '))
## 删除字符串前后(首位)空格符： strip()
print('strt1被删除前后空格的效果: ', strt1.strip())
## 返回strt2 在 strt1出现的次数，如果begin 或者 end指定则返回指定范围内strt2出现的次数
#count(strt2, begin>=0, end<=len(str1)
print('strt2在strt1中出现的次数: ', strt1.count(strt2))
print('strt2在strt1中出现的次数(指定范围):', strt1.count(strt2, 1, 10))

## 检查字符串是否是object结束，如果begin 或者 end指定则检查指定范围内是否以obj结束 （如果是返回True 否则返回False）
print('strt1是否以strt2结尾: ', strt1.endswith(strt2))
print('strt1是否以strt2结尾（指定范围）:', strt1.endswith(strt2, 1,9))

## find
print('strt1中是否包含strt2: ', strt1.find(strt2))
print('strt1中是否包含strt2（指定范围）:', strt1.find(strt2, 1,9))