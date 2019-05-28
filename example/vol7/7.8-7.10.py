'''
so=['a','b','c']
fs=[]
for a in so:
    print('最爱的是 '+a)            #7.8已完成

while so:
    t=so.pop()
    fs.append(t)

for q in fs:
    print(q+'已经做好了')'''

so=['a','b','c','c','c','c']
print('c 已经卖完了,不信你看下面清单')      #7.9已完成

while 'c' in so:
    so.remove('c')
print(so)

'''
a={}
while True:
    q=input('用户名：')                    #7.10已完成
    p=input('想去的地方是:')
    a[q]=p
    

    c=input('还有人想参加调查吗？')
    if c=='no':
        break

for v,b in a.items():
    print(v+' 最想去的地方是：'+b)'''
