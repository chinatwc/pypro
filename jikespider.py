# -*- coding: utf-8 -*-
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class spider(object):
	def __init__(self):
		print u'开始爬去内容...'

	def getsource(self,url):
		html = requests.get(url)
		return html.text
	def changepage(self,url,total_page):
		now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
		page_group = []
		for i in range(now_page,total_page+1):
			link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
			page_group.append(link)
		return page_group
	def geteverclass(self,source):
		everyclass = re.findall('<li deg="".*?</li>',source,re.S)
		return everyclass
	def getinfo(self,eachclass):
		info={}
		info['title'] = re.search('target="_blank">(.*?)</a>',eachclass,re.S).group(1)
		info['content'] = re.search('</h2><p>(.*?)</p>',eachclass,re.S).group(1)
		timeandlevel = re.findall('<em>(.*?)</em>',eachclass,re.S)
		info['classtime'] = timeandlevel[0]
		info['classlevel'] = timeandlevel[1]
		info['learnnum'] = re.search('"learn-number">(.*?)</em>',eachclass,re.S).group(1)
		return info
	def saveinfo(self,classinfo):
		f = open('info.txt','a')
		for each in classinfo:
			f.writelines('title:' + each['title' + '\n'])
			f.writelines('content:' + each['content' + '\n'])
			f.writelines('classtime:' + each['classtime' + '\n'])
			f.writelines('classlevel:' + each['classlevel' + '\n'])
			f.writelines('learnnum:' + each['learnnum' + '\n\n'])


if __name__ == '__main__':

	classinfo = []
	url = "http://www.jikexueyuan.com/course/?pageNum=1"
	jikespider = spider()
	all_link = jikespider.changepage(url,20)
	for link in all_link:
		print u'正在处理页面：' + link
		html = jikespider.getsource(link)
		everyclass = jikespider.geteverclass(html)
		for each in everyclass:
			info = jikespider.getinfo(each)
			classinfo.append(info)
	jikespider.saveinfo(classinfo)
