# -*- coding: UTF-8 -*-
import base64, requests, os, shutil, datetime

# 创建目录
s1 = str(datetime.datetime.now().year) + str("%02d"%(datetime.datetime.now().month))
p1 = 'work/link-export/'+s1
p2 = 'work/link-import/'+s1
p3 = 'work/sub-import'
if not os.path.exists(p1):
    os.mkdir(p1) 
if not os.path.exists(p2):
    os.mkdir(p2) 
shutil.rmtree(p3)
os.mkdir(p3)

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
                group = base64.urlsafe_b64encode(file_name.split('.txt')[0]).strip('=')
                for i in txt:
                    j = i.split('ssr://')[1]
                    j = j.strip()
                    data = base64.urlsafe_b64decode(j + '=' * (-len(j) % 4))
                    data2 = base64.urlsafe_b64encode(data.split('group=')[0]+'group='+group)
                    data = 'ssr://'+data2.strip('=')
                    yy.append(data)
                d = '\n'.join(yy)
                # d = (base64.b64encode(d)).strip('=') #编码
                # d = (base64.b64decode(d+'==')).decode('utf-8') #解码
                print (d)
                
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


# 订阅文件（含ssr链接的txt版）
dir_names = ['work/sub-import/']
s1 = 'work/sub-export/mac.txt'
s2 = 'work/sub-export/mac'

file = open(s1,'w+') #清空文件
for dirname in dir_names:
    file_names = os.listdir(dirname)  
    file = open(s1,'a+') #a+是追加，若文件不存在就创建

    for filename in file_names:  
        filepath = dirname + filename   
        print filepath 
        for line in open(filepath):  
            file.writelines(line)  
        file.write('\n')  
    file.close() 

# 订阅文件（base64加密版）
try:
    with open(s1,'r') as f:
        d = f.read()
        d = (base64.b64encode(d)).strip('=')
        print (d)
        with open(s2,'w+') as ff:
            ff.writelines(d)
except Exception as e:
    print (e)