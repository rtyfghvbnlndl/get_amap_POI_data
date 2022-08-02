import json
import requests
import jsonpath

def poi(keywords,types,city,citylimit,children,offset,page,extensions,sig,callback):
    key = '输入key才能用'
    js = requests.get('https://restapi.amap.com/v3/place/text?key=%s&keywords=%s&types=%i&city=%s&citylimit=%s&children=%i&offset=%i&page=%i&extensions=%s&sig=%s&callback=%s'
    % (key,keywords,types,city,citylimit,children,offset,page,extensions,sig,callback))
    js = eval(js.text)
    return js
def poi_class(js,name):
    a = jsonpath.jsonpath(js,'$.pois[*].%s' % name)
    return a

if __name__ == '__main__':
    js=poi('公园',110100,'210200','True',1,20,1,'base','','')
    print(js)
    address = poi_class(js,'address')
    print(address)
    print(type(address))