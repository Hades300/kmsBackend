import os
import re 
import json


BASEDIR="./config"



class config:
    def __init__(self):
        self.basedir = BASEDIR
        filelists = list(os.walk(BASEDIR))[0][2]
        namelists = [fileName.split('.')[0].lower() for fileName in filelists]
        self.files=dict(zip(namelists,filelists))

    def get(self,name):
        if name.lower() not in self.files.keys():
            return False
        with open(os.path.join(self.basedir,self.files[name])) as f:
            return f.read()

    #TODO: 让我考虑考虑转义的事情。 要不要做呢 感觉不需要的亚子

    def set(self,name,content):
        if name.lower() not in self.files.keys():
            return False
        with open(os.path.join(self.basedir,self.files[name]),'w+') as f:
            f.write(content)

def logParser():
    #数据获取
    with open("/mnt/logs") as f:
        data = f.read()

    #正则匹配
    data = re.findall("([\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}): <<< Incoming KMS request(.*?)IPv4 connection closed: ([\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}:\d+)",data,re.S)
    res=[]
    for  i in range(len(data)):
        time = data[i][0]
        ip = data[i][2]
        tempLogs = data[i][1].split("\n\n")
        logRes = ""
        for i  in range(len(tempLogs)):
            if tempLogs[i]:                     #split后第一个是空的
                logRes+=tempLogs[i][21:]+"\n"   #手动加上换行符
        print("time:",time)
        print("ip:",ip)
        print("request:",logRes)
        # print(dict(time=time,ip=ip,request=logRes))  #dict在此
        res.append(dict(time=time,ip=ip,request=logRes))

    # json格式化后写入 注意加上换行符 方便按条读取
    with open("/mnt/parsedLogs","a+") as f:
        for item in res:
            f.write(json.dumps(item)+"\n")

