'''
while True:
    t=input('请输入配料:')              #7.4,7.7已完成
    if t=='quit':
        break
    else:
        print('俺们会在披萨中添加 '+t+' 这种配料')'''

p='3岁以下免费，3-12岁10刀，12岁以上15刀'
p+='\n根据观众的不同年龄收取不同的票价，请输入您的年龄：'

'''
while True:
    t=input(p)                          #7.5已完成
    if t== 'quit':
        break
    elif int(t)<2:
        print('3岁以下免费\n')
    elif int(t)<=12 and int(t)>=3:
        print('3-12岁票价10刀\n')
    else:
        print('12岁以上票价15刀\n')'''

i=1
while True:                         #7.7已完成
    i+=1
    print(i)

