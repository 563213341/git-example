
ak=[]
while True:
    guestname=input('请输入姓名:')
    pt=print(guestname+'，欢迎你的到来')
    ak.append(guestname)
    print(ak)
    
guest='guestbook.txt'
with open(guest,'w') as gb:
    gb.write(ak)

