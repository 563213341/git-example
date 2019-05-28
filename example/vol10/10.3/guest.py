filename='guest.txt'
while True:
    a=input('请输入访客姓名：')
    with open(filename,'w') as fn:
        fn.write(a+'\n')
    if a=='no':
        break


