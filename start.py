# -*- coding: UTF-8 -*-
import base64, requests, os, shutil, datetime

# create the Backup folder
s1 = str(datetime.datetime.now().year) + str("%02d"%(datetime.datetime.now().month))
p1 = 'work/downloads/'+s1
p2 = 'work/converted/'+s1
if not os.path.exists(p1):
    os.mkdir(p1) 
if not os.path.exists(p2):
    os.mkdir(p2) 

g = os.walk("work/import")  
for path,dir_list,file_list in g:  
    for file_name in file_list:  

        # 备份输入文件
        p3 = os.path.join(path, file_name) 
        shutil.copy(p3, p2) 
    
        try:
            with open(p3,'r') as f:
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
                
                # 输出文件，并备份
                res = 'work/export/'+file_name
                with open(res,'w+') as ff:
                    ff.writelines(d)
                shutil.copy(res, p1) 

        except Exception as e:
            print (e)