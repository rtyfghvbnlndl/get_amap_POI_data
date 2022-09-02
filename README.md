# get_amap_POI_data
下载高德地图webapi中的POI<br>
## 说明
修改list1 = ['name','pname','cityname','address','location','tel','id']，即可指定获得的数据类型和顺序<br>
### list2和list3是poi code和关键词。重复的内容会被删除，允许留空。然后它们会完成所有可能的组合，并搜索。<br>
以列为类别写入csv<br>
需要https://lbs.amap.com/api/webservice/guide/api/search获取key并填入<br>
## 更新
1. 修复了一页不满20条出错的问题。现在，直到返回完全空白的页面才会出错。
2. 添加了限定页数最小值的方法。
### 9月2日
1. 修改了函数，现在不会报错了。
2. 原来代码写错了，但是能用真的是存在的。已修复。
3. 添加了一次性写入多个搜索条件的功能。再也不用一次一次运行脚本了。<br>
![image](1.png)
