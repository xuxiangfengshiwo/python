#coding:utf8
import os
import re

#target
source = 'A12'
target = 'NIO'


#find match files
cmd = 'D:\\software\\Git\\usr\\bin\\find.exe ./ -name \'*' + source + '*\''
print (cmd)

fp = os.popen(cmd, 'r')
content = fp.read()
fp.close()

##print (content)
##print (type(content))

#source file list
sourceflist = content.split()
print (sourceflist)
#target file list
targetflist = re.sub(source, target, content).split()
print (targetflist)

#cp to new files
for i in range(len(sourceflist)):
    print ('source:' + sourceflist[i] + ' ' + 'target:'+ targetflist[i])
    cmd = 'D:\\software\\Git\\usr\\bin\\cp.exe ' + sourceflist[i] + ' ' + targetflist[i]
    print (cmd)
    ret = os.system(cmd)
    print (ret)




