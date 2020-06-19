

import pymysql

import xcode_auto_configurator

db = pymysql.connect(host='rm-wz94u0e358h79pbm2vo.mysql.rds.aliyuncs.com',user='zhangzh',passwd='Dnwx1002',db='dnwx_client',
charset='utf8')

cur = db.cursor()

sql = "SELECT * FROM `wbgui_formconfig` WHERE `pjId` LIKE '%37826003%' LIMIT 0, 1000"
# sql = "SELECT * FROM `wbgui_formconfig` LIMIT 0, 10"
statisticsDic = {}
try:
    cur.execute(sql)
    index = cur.description
    # print (index)
    indexDic = {}
    for i in range(len(index)-1):
        indexDic[index[i][0]] = i
    # print (indexdic)

    row = cur.fetchall()
    index = indexDic["statistics"]
    # print(row)
    # print(index)
    #print(row[0][index])
    statistics = row[0][index]
    statisticsArr = statistics.split("#")
    for i in range(len(statisticsArr) - 1):
        arr = statisticsArr[i].split(";")
        if len(arr) > 1:
            statisticsDic[arr[0]] = arr[1]
 
    # print(statisticsDic)
    
except Exception as e:
    raise e
finally:
    db.close()
print("sql execute complete")

prejectFolderPath = "/Users/liuyaqiang/Desktop/test"
prejectPath = "/Users/liuyaqiang/Desktop/test/test.xcodeproj"

# prejectFolderPath = "/Users/liuyaqiang/Desktop/Vigame/VigameAd-UnityDemo"
# prejectPath = "/Users/liuyaqiang/Desktop/Vigame/VigameAd-UnityDemo/Unity-iPhone.xcodeproj"


xcode_auto_configurator.set_project(prejectFolderPath,prejectPath,statisticsDic)


