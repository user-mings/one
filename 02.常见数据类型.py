# #type() ---> 获取指定的字面量或变量的数据类型
# from types import NoneType
#
# print("Hello Python")
#
# print(type("Hello"))#str
# print(type(30))#int
# print(type(3.14))#float
# print(type(True))#bool
# print(type(False))#bool
# print(type(None))#NoneType
#
# num = 50
# print(type(num))#int
#
# #isinstance(数据,类型) ----> bool值 ----> 判定数据是否是指定的类型, 是:True , 否:False
# print(isinstance(num,int))#True
# print(isinstance(num,bool))#False
# print(isinstance(num,str))#False
# print(isinstance(num,float))#False
# print(isinstance(num,NoneType))#False

#字符串
#定义字符串的三种方式
s1 = "Hello"#双引号定义
s2 = 'Python'#单引号定义
s3 = """
Hello:
    欢迎大家进行Python的学习
    请多关注
"""#三引号定义

print(s1)
print(s2)
print(s3)

#\'表示单引号  \"表示双引号 \n换行符 \t制表符
mgs = 'It\'s very interesting'
print(mgs)

msg2 = "It's very interesting"
print(msg2)

msg3 = "\"It's very good\""
print(msg3)

mgs4 = """Hello:\n\tIt's very interesting"""
print(mgs4)