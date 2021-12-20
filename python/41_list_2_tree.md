#### python list to tree

##### data
```
{
    "fileList": [
        {
            "ID": "1290920574969873453",
            "PID": "0",
            "Name": "1580614236360678092",
            "Size": 0,
            "NodeType": 2,
            "OssBucket": null,
            "OssPath": null
        },
        {
            "ID": "1290920574969873523",
            "PID": "1290920574969873453",
            "Name": "新建文件夹",
            "Size": 0,
            "NodeType": 2,
            "OssBucket": null,
            "OssPath": null
        },
        {
            "ID": "1290920574969873574",
            "PID": "1290920574969873523",
            "Name": "新建文件夹4",
            "Size": 0,
            "NodeType": 2,
            "OssBucket": null,
            "OssPath": null
        },
        {
            "ID": "1291504856239808488",
            "PID": "1290920574969873453",
            "Name": "方法",
            "Size": 0,
            "NodeType": 2,
            "OssBucket": null,
            "OssPath": null
        },
        {
            "ID": "1290920574969899936",
            "PID": "1290920574969873453",
            "Name": "white-and-yellow-flower-with-green-stems-36764.jpg",
            "Size": 196992,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/fachan/1290920574969900277.jpg"
        },
        {
            "ID": "1290920574969900738",
            "PID": "1290920574969873453",
            "Name": "3.产学研项目-系统设计方案1.5.pdf",
            "Size": 587536,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/fachan/1290920574969900869.pdf"
        },
        {
            "ID": "1291503921659275903",
            "PID": "1290920574969873523",
            "Name": "4.pptx",
            "Size": 33150,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/fachan/1291503921659276412.pptx"
        },
        {
            "ID": "1291503979318169174",
            "PID": "1290920574969873523",
            "Name": "tech-coin-js(1).png",
            "Size": 4545,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/fachan/1291503979318274096.png"
        },
        {
            "ID": "1291503981790863105",
            "PID": "1290920574969873523",
            "Name": "tech-coin-js(2).png",
            "Size": 4545,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/fachan/1291503981790976044.png"
        },
        {
            "ID": "1291504856105939581",
            "PID": "1290920574969873453",
            "Name": "律享空间小法蝉对接接口设计V0.10.docx",
            "Size": 63263,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/fachan/1291504856106067779.docx"
        },
        {
            "ID": "1291504856337389323",
            "PID": "1291504856239808488",
            "Name": "VB2.docx",
            "Size": 11577,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/fachan/1291504856336028478.docx"
        },
        {
            "ID": "1291504856411591146",
            "PID": "1291504856239808488",
            "Name": "发斯蒂芬.pptx",
            "Size": 33150,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/fachan/1291504856411217951.pptx"
        },
        {
            "ID": "1291505617409246870",
            "PID": "1290920574969873453",
            "Name": "VB丰富的.docx",
            "Size": 11577,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/fachan/1291505617407349877.docx"
        },
        {
            "ID": "1291505617622329041",
            "PID": "1290920574969873453",
            "Name": "律享空间小法蝉对接接口设计V0.10(1).docx",
            "Size": 63263,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/fachan/1291505617622427228.docx"
        },
        {
            "ID": "1291508222339510711",
            "PID": "1290920574969873453",
            "Name": "我来看看预览.docx",
            "Size": 11577,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/zeda/1291508222338244233.docx"
        },
        {
            "ID": "1291508292194741143",
            "PID": "1290920574969873453",
            "Name": "测试用图片12.jpg",
            "Size": 2001107,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/zeda/1291508292194901087.jpg"
        },
        {
            "ID": "1291509922375977543",
            "PID": "1290920574969873523",
            "Name": "1.2 - 0715的副本.zip",
            "Size": 2152204,
            "NodeType": 1,
            "OssBucket": "swartz-doc",
            "OssPath": "test/zeda/1291509922376089956.zip"
        }
    ]
}
```

##### code
```
class CommonUtil(object):

    @staticmethod
    def make_tree(data):
        result = []
        key_map = {}
        for item in data:
            key_map[item['ID']] = item

        for i in data:
            # 判断pid 是0 就正常添加进去
            if i['PID'] == "0":
                result.append(key_map[i['ID']])
            # 子分类
            else:
                pid = i['PID']
                # 判断他的父类 有没有child键
                if "children" not in key_map[pid]:
                    key_map[pid]["children"] = []  # 创建child键
                # 将当前子类填充到父类child里
                key_map[pid]['children'].append(key_map[i['ID']])
        return result
```

##### ref
```
https://www.alfred-alan.com/blog/python/2021-08-18-make-tree/

https://www.coder.work/article/3169142

https://www.programminghunter.com/article/19791036148/

https://codeleading.com/article/48725752138/
```




