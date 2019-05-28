'''
def ann(*things):
    print('你想要什么材料')
    for thing in things:
        print('你要的是：'+thing+'\n')       #8.12已完成
ann('aa')
ann('cc','bb')
ann('oo','bb','bb')'''

'''
def bp(first,last,**msg):
    msb={}
    msb['fa']=first
    msb['ln']=last                         #8.13已完成
    for k,v in msg.items():
        msb[k]=v
    return msb

a=bp('zhu','yi',loc='wx',coun='ch',pla='ea')
print(a)'''

'''
def mk(ppai,cjia,**otmsg):
    msb={}
    msb['厂家：']=ppai
    msb['型号：']=cjia                         #8.14已完成
    for k,v in otmsg.items():
        msb[k]=v
        
    return msb

a=mk('honda','civic',col='blue',tp=True)
print(a)'''
