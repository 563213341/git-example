'''
def cc(name,coun):
    part = name+','+coun
    return part.title()      #8.6已完成
aa=cc('wuxi','ch')
print(aa)
bb=cc('niuyao','am')
print(bb)
pp=cc('mosike','damao')
print(pp)'''

'''
def ma(name1,name2,num=''):
    pname={'歌手名':name1,'专辑名':name2}       #8.7已完成
    if num:
        pname['歌曲数']=num
    return pname
aa=ma('aaa','aaaa')
print(aa)
bb=ma('bbb','bbbb','8')
print(bb)
cc=ma('ccc','cccc')
print(cc)'''


def ma(name1,name2):
    pname={'歌手名':name1,'专辑名':name2}       #8.8已完成
    return pname

while True:
    print('请输入相关信息，输入q退出')
    aname=input('请输入歌手名：')
    if aname=='q':
        break
    bname=input('请输入专辑名：')
    if bname=='q':
        break
   
    aa=ma(aname,bname)
    print(aa)

