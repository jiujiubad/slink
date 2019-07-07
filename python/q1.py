# -*- coding: UTF-8 -*-
import base64, requests, os
path = 'text/q1.txt'
res = 'q6MjphdXRoX2NoYWlu'
group = '0707-15点-q1'

group = base64.urlsafe_b64encode(group).strip('=')
try:
    with open(path,'r') as f:
        txt = f.read()
        txt = (base64.b64decode(txt+'=='))
        txt = txt.strip().split('\n')
        yy = []
        for i in txt:
            j = i.split('ssr://')[1]
            j = j.strip()
            data = base64.urlsafe_b64decode(j + '=' * (-len(j) % 4))
            data2 = base64.urlsafe_b64encode(data.split('group=')[0]+'group='+group)
            data = 'ssr://'+data2.strip('=')
            yy.append(data)
        d = '\n'.join(yy)
        # d = (base64.b64encode(d)).strip('=')
        # d = (base64.b64decode(d+'==')).decode('utf-8')
        print (d)
        with open(res,'w+') as ff:
            ff.writelines(d)
except Exception as e:
    print (e)