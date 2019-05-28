'''
def show_great(names):
    for name  in names:             #8.9已完成
        print(name)
  
a=['alen','bobo','cris']
show_great(a)'''



def show_great(bnames,anames):
    while bnames:
        aname='the Great '+bnames.pop()
        anames.append(aname)
        
def show_mag(names):
    for name  in names:                 #8.10有问题    #8.11已完成
        print(name)

    
a=['alen','bobo','cris']
b=[]
show_mag(a)
show_great(a[:],b)
show_mag(a)
show_mag(b)

