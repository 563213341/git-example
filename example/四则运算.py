print('欢迎使用简单四则运算计算器')
print('a为加法模式，b为减法模式，c为乘法模式，d为除法模式')

while True:
    model=input('请输入代码选择模式：')
    num1=input('请输入第一个数字：')
    num2=input('请输入第二个数字：')
    if model=='a':
        number=float(num1)+float(num2)
        print(number)

    elif  model=='b':
        number=float(num1)-float(num2)
        print(number)

    elif  model=='c':
        number=float(num1)*float(num2)
        print(number)

    elif  model=='d':
        number=float(num1)/float(num2)
        print(number)
