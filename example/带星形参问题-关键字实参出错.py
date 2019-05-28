
def mp(size,*things):
    print('选择pizza的尺寸：'+str(size))
    print('用以下配料做pizza')
    for thing in things:
        print('--'+thing+'\n')

mp(12,'tomato')
mp(28,'potapo','tomato','egg','pdd')


#size使用关键字参数时提示出错 
