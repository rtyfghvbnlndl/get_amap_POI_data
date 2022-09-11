import poi
maxx = int(input('最大页码(一页20条)'))
minn = int(input('最小'))
title1 = str(input('标题头？（y）'))
list1 = ['name','pname','cityname','adname','address','location','type','tel']#!!填写需要返回的信息
list2 = ['110100','110100','','']#!!poi
list3 = ['210200','210200','','']#!!ad code
for n in range(210200,210200):#!!ad code
    list2.append(n)
list2 = poi.clean(list2)
list3 = poi.clean(list3)

nnn = 0
for ad_num in list3:
    for poi_num in list2:
        nnn += 1
        print('第',nnn,'次,条件是',ad_num,poi_num)
        with open('./csv/school_2.csv','a+',newline='') as f:
            #文件名，内容不会覆盖
            if title1 == 'y':
                for name in list1:
                   f.write('%s,' % name)
                f.write('\n')
            else:
                print('不输入标题头')
            if_end = 0
            for nn in range (minn,(maxx+1)):
                print(nn)
                js=poi.poi('',poi_num,ad_num,'True',1,20,nn,'base','','',if_end)#!!keywords|分隔
                #'公园','110100','210200','True',1,20,1,'base','',''
                #填写keywords,types,city,citylimit,children,offset,page,extensions,sig,callback
                n = 0
                h = len(poi.poi_class(js,'name'))
                if h == 0:
                    if_end = 666
                    print(nn,'空')
                else:
                    for n in range(0,h):
                        print('写入第%i条' % (nn*20+n+1-20))
                        for name in list1:
                            con = poi.poi_class(js,name)[n]           
                            f.write('''"%s",''' % con)
                        n += 1
                        f.write('\n')
