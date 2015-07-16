# coding=utf-8
import urllib2
import re
import requests
from lxml import etree

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

links=[]#遍历url的地址
k=1


url = 'http://tuchong.com/contacts/?page=1'
html=urllib2.urlopen(url).read()
selector=etree.HTML(html)
links=selector.xpath('//div[@class="icon-wrapper"]/a/@href')

for i in links:
    url1=""+i
    html2=urllib2.urlopen(url1).read()#读取当前页面的内容
    selector=etree.HTML(html2)#转换为xml，用于在接下来识别
    link=selector.xpath('//figure[@class="main-collage"]/img/@src')#抓取图片，各位也可以更换为正则，或者其他你想要的内容
    
    for each in link:
    	print each
    	print u'正在下载%d'%k
    	fp=open('image/'+str(k)+'.jpg','wb')#下载在当前目录下 image文件夹内，图片格式为jpg
      	image1=urllib2.urlopen(each).read()#读取图片的内容
      	fp.write(image1)#写入图片
     	fp.close()
      	k+=1#k就是文件的名字，每下载一个文件就加1

print u'下载完成'

