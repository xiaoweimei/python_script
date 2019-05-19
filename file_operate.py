import os,sys
import time,shutil
dir=r'F:\limu_mica'
lulu=[]
dudu=[]
bubu=[]
for i in (os.listdir(dir)):
    lulu.append(dir+'\\'+str(i))
for k in lulu:
    for i in (os.listdir(k)):
        dudu.append(k+'\\'+str(i))
for j in dudu:
    if os.path.isdir(j):
        for i in (os.listdir(j)):
            bubu.append(j+'\\'+str(i))
    else:
        bubu.append(dir+'\\'+str(i))
            
#        print(j+)
#        if os.path.isdir(dir+'\\'+str(i)):
#            return printname(dir+'\\'+str(i))
#        else:
#            print(i)
print(lulu)
j=0
for i in bubu:
    print(i)
    b=i[13:]
    c=b[len(b)-b[::-1].index('\\')-1:]
#    print(c)
    d=(b.replace(c,'-'+str(j)+'.bmp'))
    e=(d.replace(d[d.index('\\')],'-'))
    newname=i[0:13]+e
    print(newname)
    shutil.copy(i,newname)
    time.sleep(1)
    j+=1
#    time.sleep(1)

print(type(bubu))

'''
for i in (os.listdir(os.getcwd())):
    print(dir+str(i))
    if os.path.isdir(dir+'\\'+str(i)):
        return()
        print (str(i)+"is a directory")
    else:
        print (str(i)+" isnnn't a directory")
'''
print(1234)
