import os
import re
import sqlite3
from uuid import uuid1
import requests
from bs4 import BeautifulSoup
from random import choice



conn = sqlite3.connect('gushici.db')
cursor = conn.cursor()
#cursor.execute('create table author (id varchar(20) PRIMARY KEY , xm varchar(30), cd varchar(20),url varchar(250))')
#cursor.execute('create table shici (id varchar(20) PRIMARY KEY , author_id varchar(20), bt varchar(255), lb varchar(50),nr varchar(1000))')
#exit()

def get_cd(urlstr):
    resp=requests.get('https://sou-yun.cn/'+urlstr)
    resp.encoding = "utf-8" #设置接收编码格式
    sp = BeautifulSoup(resp.text,'lxml')
    sp = sp.find(id='content')
    return sp
    
url = "https://sou-yun.cn/QueryPoem.aspx"

response = requests.get( url )
response.encoding = "utf-8" #设置接收编码格式
soup = BeautifulSoup(response.text,'lxml')
soup=soup.find(name='div',attrs={'style':'padding-bottom: 1em;'})
item=soup.find_all('a')
cnt=0
for i in item:
    #if cnt<1:
        try:
           sp1=get_cd(str(i['href']))
           sp1=sp1.find_all('a')
           cnt1=0
           for k in sp1:
               cnt=cnt+1
               print(k['href'],k.string,i.string)
               cursor.execute('insert into author (id, xm,cd,url) values (\''+str(cnt)+'\',\''+k.string+'\',\''+i.string+'\',\''+k['href']+'\')')
        except Exception as e:
           print('错误：',e)
cursor.close()
conn.commit()
conn.close()
    
#保存文件




