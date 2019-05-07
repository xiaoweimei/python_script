# -*- coding: cp936 -*-
import urllib.request
import re,time,os,sys
import chardet
path="C:\\Users"
os.makedirs(path)
for i in range(1,307):
    site="http://www.sklabig.cn/Ch/Graduate.asp?show=1&id="+str(i)
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    try:
        page1 = urllib.request.Request(site,headers=head)  #urllib.urlopen()方法用于打开一个URL地址
        page = urllib.request.urlopen(page1)  #urllib.urlopen()方法用于打开一个URL地址
        team=page.getcode()
        html = page.read() #read()方法用于读取URL上的数据
        reg = r'<img.*src="(.*.jpg)".*width.*>'    #正则表达式，得到图片地址
        regna =r'<td.*45%">(.*)</td>'
        regdo =r'<td>(.*).*&nbsp.*</td>'
        imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
        imgname=re.compile(regna)
        imgdoname=re.compile(regdo)
        encode_type = chardet.detect(html)
        html = html.decode(encode_type['encoding'])
        imglist = re.findall(imgre,html)
        imglistna = re.findall(imgname,html)
        imglistdo = re.findall(imgdoname,html)
        sites="http://www.sklabig.cn"+str(''.join(imglist))[2:]#
        for j in imglistna:
            name=str(j)
        for d in imglistdo:
            doname=str(d)
        lastname1=doname+"-"+name+".jpg"
        lastname=lastname1.replace("&nbsp;","")
        if sites=="http://www.sklabig.cn":
            pass
        else:
            print (sites)
            urllib.request.urlretrieve(sites,path+'\\'+str(lastname))
    except:
        print("somenthing wrong")
    finally:
        print("get one")
#for imgurl in imglist:
#urllib.urlretrieve(imgurl,'C:\Users\Miss Han\Desktop\%s.jpg' % x)
#x+=1

#print site
#html = getHtml(site)
#print getImg(html)
