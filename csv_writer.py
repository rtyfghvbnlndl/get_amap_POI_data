import poi
maxx = int(input('最大页码(一页20条)'))
list1 = ['name','pname','cityname','address','location','tel','id']
with open('keyword.csv','a+',newline='') as f:
    #文件名，内容不会覆盖
    for name in list1:
        f.write('%s,' % name)
    f.write('\n')
    #填写需要返回的信息
    for nn in range (1,(maxx+1)):
        js=poi.poi('公园',110100,'210200','True',1,20,nn,'base','','')
        #填写keywords,types,city,citylimit,children,offset,page,extensions,sig,callback
        n = 0
        for n in range(0,20):
            print('写入第%i条' % (nn*20+n+1-20))
            for name in list1:
                con = poi.poi_class(js,name)[n]
                f.write('''"%s",''' % con)
            n += 1
            f.write('\n')