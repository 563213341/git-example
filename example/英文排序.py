'''
file = 'a.txt'
with open(file) as txt:
    line = txt.readlines()
for a in line:
    print(a)


mes=''
for a in line:
    mes +=a.rstrip()
print(mes)


count={}
for i in mes:
    count[i]=mes.count(i)

print(count)'''

filename = 'b.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
mes = ''
for line in lines:
    mes += line.rstrip()




count={}
for i in mes:
    count.setdefault(i,0)
    count[i] += 1
for k,v in count.items():
    print(str(k)+':'+str(v))
