import keyword
import random

print("Hello Python")

print("----------------------------------")

print("下面是Python的保留字")
print("保留字即关键字，我们不能把它们用作任何标识符名称n")
# 打印关键字
print(keyword.kwlist)

# 这是注释

'''
这也是注释  
'''

"""
这还是注释
"""

print("上面这些是Python的保留字")  # 你猜对了，这依然是注释

print("----------------------------------")

print("缩进表示代码块：")
num = random.randint(0, 2)
if 0 == num:
    print("00000000")
elif num == 1:
    print("11111111")
else:
    print("22222222")

print("----------------------------------")
print("申明变量：")
a = 1
b = False
c = 1.1
d = 1 + 1j

# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
print(a, + \
    b, c, + \
          d)

print("----------------------------------")

# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
# 转义符 '\'
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
print(r"this is a line with two \n\n")
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
str = 'abcdefghijklmn '
print(str * 3)
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str + '你好')  # 连接字符串
# 不会越界
print(str[100:-1])  # 打印空字符串
print("----------------------------------")

while input("你是猪吗？\nyse or no?\n") != "yes":
    print("回答错误！！！\n")
else:
    print("恭喜你，小猪猪！")

print("----------------------------------")

import sys

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

print("----------------------------------")

from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
