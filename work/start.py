# -*- coding: UTF-8 -*-
import base64, requests, os, shutil, datetime, random

# 创建目录
s1 = str(datetime.datetime.now().year) + str("%02d"%(datetime.datetime.now().month))
p1 = 'work/link-export/'+s1
p2 = 'work/link-import/'+s1
p3 = 'work/temp'
if not os.path.exists(p1):
    os.mkdir(p1) 
if not os.path.exists(p2):
    os.mkdir(p2) 
shutil.rmtree(p3)
os.mkdir(p3)

# base64 解码，修改 ssr 分组名称
g = os.walk("work/today")  
for path,dir_list,file_list in g:  
    for file_name in file_list:  

        f1 = os.path.join(path, file_name) 
        try:
            with open(f1,'r') as f:
                txt = f.read()
                txt = (base64.b64decode(txt+'=='))
                txt = txt.strip().split('\n')
                yy = []
                
                # ssr 备注分组合并一个
                group = str("%02d"%(datetime.datetime.now().month)) + str("%02d"%(datetime.datetime.now().day))
                
                for i in txt:
                    j = i.split('ssr://')[1]
                    j = j.strip()
                    data = base64.urlsafe_b64decode(j + '=' * (-len(j) % 4))
                    data2 = base64.urlsafe_b64encode(data.split('group=')[0]+'group='+group)
                    data = 'ssr://'+data2.strip('=')
                    yy.append(data)
                d = '\n'.join(yy)
                
                # 备份（输出的文件）
                res = p3+'/'+file_name
                with open(res,'w+') as ff:
                    ff.writelines(d)
                # 备份（输出的文件）
                shutil.copy(res, p1) 
                # 备份（输入的文件)
                shutil.copy(f1, p2) 

        except Exception as e:
            print (e)


# 合并成一个 txt 文件
dir_names = ['work/temp/'] #可追加文件夹
p4 = 'work/subscribe/'+s1
if not os.path.exists(p4):
    os.mkdir(p4) 

s1 = p4 + '/' + str("%02d"%(datetime.datetime.now().month)) + str("%02d"%(datetime.datetime.now().day)) + '.txt'
s2 = p4 + '/' + str("%02d"%(datetime.datetime.now().month)) + str("%02d"%(datetime.datetime.now().day)) + '-' + ('%06x' % random.randrange(16**8)).upper()

for dirname in dir_names:
    file_names = os.listdir(dirname)  
    file = open(s1,'a+') #a+是追加，若文件不存在就创建

    for filename in file_names:  
        filepath = dirname + filename  
        for line in open(filepath):  
            file.writelines(line)  
        file.write('\n')  
    file.close() 

# 生成订阅文件（txt 文件内容 base64 加密）
try:
    with open(s1,'r') as f:
        d = f.read()
        d = (base64.b64encode(d)).strip('=')
        with open(s2,'w+') as ff:
            ff.writelines(d)
except Exception as e:
    print (e)


# 使用方法：
# 把多份订阅 txt（名字改为月日第几份 080801.txt）放在 work/today 文件夹，执行 python work/start.py
# 1、其中 ssr 备注分组，根据第 30-33 行代码修改 group
# 2、link-import 和 link-export 是每份文件处理前后，subscribe 是处理完的集合文件，temp 是处理过程中用到的每次处理前会清空

## 用过的语法：
# 调试，用 print
# file = open(s1,'w+') #清空文件
# d = (base64.b64encode(d)).strip('=') #编码
# d = (base64.b64decode(d+'==')).decode('utf-8') #解码
# group = base64.urlsafe_b64encode(file_name.split('.txt')[0]).strip('=') #ssr备注分组对应分开多个
# 随机字符串：('%06x' % random.randrange(16**6)).upper()
# 随机字符串：str(uuid.uuid4())