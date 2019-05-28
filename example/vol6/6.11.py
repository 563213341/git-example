'''
cities={
    '无锡':{'cou':'china1','pop':'五百万','fac':'穷'},
    '苏州':{'cou':'china2','pop':'700w','fac':'富'},
    '纽约':{'cou':'china3','pop':'400w','fac':'很'}
    }
for city,stu in cities.items():                              #6.11有问题
    print('城市名字是：'+city)
    for v in stu['fac']:
        print('有钱程度是 '+v.title())
    for p in stu['cou']:
        print('国家是 '+p.title())
    for t in stu['pop']:
        print('人口是 '+t.title())'''



cities={
    '无锡':{'cou':'china1','pop':'500w','fac':'穷'},
    '苏州':{'cou':'china2','pop':'700w','fac':'富'},
    '纽约':{'cou':'china3','pop':'400w','fac':'很'}
    }
for city,stu in cities.items():                              
    print('城市名字是：'+city)
    cp=stu['cou']+' '+stu['pop']
    mon=stu['fac']
    print('基本情况是：'+cp)
    print('贫富情况是：'+mon)
