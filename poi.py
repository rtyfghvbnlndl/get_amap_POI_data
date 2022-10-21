import requests
import jsonpath

def poi(keywords,types,city,citylimit,children,offset,page,extensions,sig,callback,if_end):
    key = '输入'
    if if_end == 666:
        return[]
    else:
        js = requests.get('https://restapi.amap.com/v3/place/text?key=%s&keywords=%s&types=%s&city=%s&citylimit=%s&children=%i&offset=%i&page=%i&extensions=%s&sig=%s&callback=%s'
        % (key,keywords,types,city,citylimit,children,offset,page,extensions,sig,callback))
        js = eval(js.text)
        return js
def poi_class(js,name):
    a = jsonpath.jsonpath(js,'$.pois[*].%s' % name)
    if a == False:
        return []
    else:
        return a
def clean(list):
    list1 = []
    for l in list:
       if l not in list1:
            list1.append(l)
    return list1
if __name__ == '__main__':
    js=poi('公园','110100','210200','True',1,20,1,'base','','')
    print(js)
    address = poi_class(js,'address')
    print(address)
    print(type(address))