while True:
    num1=input('输入第一个数字：')
    num2=input('输入第二个数字：')
    try:
        c=int(num1)+int(num2)                           #10.6 10.7已完成
    except  ValueError:
        print('程序出错，请确保请输入的是数！')
    else:
        print(c)


