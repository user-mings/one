#获取键盘上输入的数据 -----> input(...)
# name = input("请输入你的名字:")
# age = input("请输入你的年龄")
# print(f"大家好,我的名字是{name}.今年{age}岁")

#案例
# total_amount = 10000#总金额
# password = input("请输入密码:")#密码
# print(f"密码正确:{[password]}")
# amount = input("请输入取款金额:")#取款金额 ----> input输入固定的为str类型
# #计算余额
# print(f"银行卡余额{total_amount-int(amount)}")#str类型不能与int类型运算 ----> int(...)强制转换为int类型

#练习
num1 = input("第一个数:")
num2 = input("第二个数:")
#计算两数之和
# print(f"两数之和是{int(num1) + int(num2)}")
print(f"两数之和:{float(num1) + float(num2)}")
