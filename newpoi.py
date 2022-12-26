import requests
#https://restapi.amap.com/v3/place/around?key=<用户的key>&location=116.473168,39.993015&radius=10000&types=011100


def urlget(dic1,fn):
    lis1=['key','location','radius','types']
    url='https://restapi.amap.com/v3/place/around?'
    for words in lis1:
        url+=(str(words)+'='+str(dic1[words]).strip('(').strip(')').replace(' ','')+'&')
    print(url)
    for i in range(1,6):
        url1=url+('page='+str(i))
        print(url1)
        
        r=requests.get(url1)
        js=eval(r.text)
        print(js)
        write(js,fn)
        if len(js['pois'])!=20:break
        

def write(js,fn):
    global p
    h = len(js['pois'])
    with open('./csv/%s.csv'%fn,'a+',newline='') as f:
        for n in range(0,h):
            p+=1
            print('写入第%i条' % p)
            for name in lis2:
                try:
                    con = js['pois'][n][name]
                    f.write('"%s",' % con)
                except:continue
            f.write('\n')

lis2=['name','pname','cityname','address','location','type','tel','distance']
dic1={'key':'','location':'','radius':'1000','types':''}
  
p=0
locations=[(119.281123,26.056889)]
#typess=['080300','050000','160000','070000','060000']
#typess=['150700','150600','150500','150400','150300','150200','150100','151200','151300']
typess=['120300']
for loc in locations:
    for types in typess:
        dic1['location']=loc
        dic1['types']=types
        fn=str(loc)+str(types)
        #fn=str(loc)+'other'
        #
        urlget(dic1,fn)
        
        
