import poi
maxx = int(input('最大页码(一页20条)'))
minn = int(input('最小'))
list1 = ['name','pname','cityname','address','location','type']#填写需要返回的信息
with open('sheqv.csv','a+',newline='') as f:
    #文件名，内容不会覆盖
    for name in list1:
        f.write('%s,' % name)
    f.write('\n')
    for nn in range (minn,(maxx+1)):
        js=poi.poi('','140000','140109','True',1,20,nn,'base','','')
        #'公园',110100,'210200','True',1,20,1,'base','',''
        #填写keywords,types,city,citylimit,children,offset,page,extensions,sig,callback
        print(nn)
        n = 0
        h = len(poi.poi_class(js,name))
        for n in range(0,h):
            print('写入第%i条' % (nn*20+n+1-20))
            for name in list1:
                con = poi.poi_class(js,name)[n]           
                f.write('''"%s",''' % con)
            n += 1
            f.write('\n')
