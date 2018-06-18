# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 22:50:34 2018

@author: luo xi yang
"""

'''百度翻译api主页：http://api.fanyi.baidu.com/api/trans/product/index'''
import http.client
import hashlib  
#import md5
import urllib
import random
import json

class Translate_api():
    def __init__(self):
        pass
    def translate(self,text):
        appid = '你的百度翻译的appid'
        secretKey = '你的百度翻译的密钥'#在百度翻译api主页可以申请。
        
         
        httpClient = None
        myurl = '/api/trans/vip/translate'
        q = str(text)
        fromLang = 'auto'
        toLang = 'auto'
        salt = random.randint(32768, 65536)
        
        sign = appid+q+str(salt)+secretKey
        m1 = hashlib.md5()
        m1.update(sign.encode("utf-8"))
        sign = m1.hexdigest()
        print(sign)
        myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
        print(myurl)
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
         
            #response是HTTPResponse对象
            response = httpClient.getresponse()
            result = response.read()
            data = json.loads(result)
            #print(data)
            #return data["trans_result"][0]["dst"]
            #print(response.read())
            return data["trans_result"][0]["dst"]
        except Exception as e:
            print(e)
            return None
        finally:
            if httpClient:
                httpClient.close()
    def colour(self):
        num=random.randrange(5)
        #num=5
        color_br=["#FF82AB","MEDIUM TURQUOISE","#D02090","#87CEEB","#FF7F50"]
        color_1=["#fff","#FFF","#FFFFFF","#FFFFFF","#FFFFFF"]
        color_2=["#fff","#FFF","#FFFFFF","#FFFFFF","#FFFFFF"]
        color_3=["black","black","black","black","black"]
        print(num,color_br[num],color_1[num],color_2[num])
        return color_br[num],color_1[num],color_2[num],color_3[num]
