d={'ABC':{'Android':[0,0,1,0,0,1,1],'IOS':[0,0,1,0,0,1,0],'web':[0,0,1,0,0,1,1]},
    'XYZ':{'Android':[0,0,1,0,1,1,0],'IOS':[1,1,1,0,0,1,0],'web':[0,0,1,1,0,1,1]}
}

res={}
for key,val in d.items():
    count_mobile=0
    count_web=0
    for i in range(0,7):
        count_mobile+=val['Android'][i] | val['IOS'][i] 
        count_web+=val['web'][i]
    res[key]={'mobile':count_mobile,'web':count_web}
print(res)



''' output : {'ABC': {'mobile': 3, 'web': 3}, 'XYZ': {'mobile': 5, 'web': 4}} '''
