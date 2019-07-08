# -*- coding: UTF-8 -*-
import base64, requests, os, shutil, datetime

dir_names = ['group/un-used/', 'group/using-qq/', 'group/using-yt/']
p1 = 'mac.txt'
p2 = 'mac'

file = open(p1,'w+') #清空文件
for dirname in dir_names:
    file_names = os.listdir(dirname)  
    file = open(p1,'a+') #a+是追加，若文件不存在就创建

    for filename in file_names:  
        filepath = dirname + filename   
        print filepath 
        for line in open(filepath):  
            file.writelines(line)  
        file.write('\n')  
    file.close() 

try:
    with open(p1,'r') as f:
        d = f.read()
        d = (base64.b64encode(d)).strip('=')
        print (d)
        with open(p2,'w+') as ff:
            ff.writelines(d)
except Exception as e:
    print (e)

# g = os.walk("work/import")  
# for path,dir_list,file_list in g:  
#     for file_name in file_list:  

#         # Backup the import
#         p3 = os.path.join(path, file_name) 
#         shutil.copy(p3, p2) 
    
#         try:
#             with open(p3,'r') as f:
#                 txt = f.read()
#                 txt = (base64.b64decode(txt+'=='))
#                 txt = txt.strip().split('\n')
#                 yy = []
#                 group = base64.urlsafe_b64encode(file_name.split('.txt')[0]).strip('=')
#                 for i in txt:
#                     j = i.split('ssr://')[1]
#                     j = j.strip()
#                     data = base64.urlsafe_b64decode(j + '=' * (-len(j) % 4))
#                     data2 = base64.urlsafe_b64encode(data.split('group=')[0]+'group='+group)
#                     data = 'ssr://'+data2.strip('=')
#                     yy.append(data)
#                 d = '\n'.join(yy)
#                 # d = (base64.b64encode(d)).strip('=')
#                 # d = (base64.b64decode(d+'==')).decode('utf-8')
#                 print (d)
                
#                 # Backup the export
#                 res = 'work/export/'+file_name
#                 with open(res,'w+') as ff:
#                     ff.writelines(d)
#                 shutil.copy(res, p1) 

#         except Exception as e:
#             print (e)