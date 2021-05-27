#import lxml.html as html
from lxml import etree
from pandas import DataFrame
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

#socialnetwork = 'http://172.16.13.108:9090/media/T1PERF/'
#socialnetwork = 'https://www.dssl.ru/'
#socialnetwork = 'https://vk.com/'
socialnetwork = 'https://social.hse.ru/'

#targets = ['20190228.170726_Trassir-4.1-QuattroStation-M10-9633/result.html']
#targets = ['files/trassir/models/manufacture/Dallmeier.html']
#targets = 'files/trassir/models/manufacture/Dallmeier.html'
#targets = ['?hl=ru']
#targets = ['id326434902']
targets = ['vml/events', 'vml']

for target in targets:
	target = targets.pop(-1)
	page = etree.parse(StringIO("<html><p>{0}{1}</p></html>".format(socialnetwork, target)))
	print(page)
	e = page.getroot().\
		find_class('sv-control').\
		pop()
	print ("{}".format(e))
	print('parsing target {0} done!'.format(target))

print('parsing all targets done!')

#page = html.parse(%s%s)

#page = html.parse("{0}{1}".format(socialnetwork, targets))
#page = "{0}{1}".format(socialnetwork, targets)
#tree = etree.HTML(page)
#tree = etree.parse(page)
#for block in tree.xpath("//div[@class='container']"):
#	table = block.xpath("//div[@class='fixed']")[0].text
#	print(table) 
	

#for block in tree.xpath("//div[@class='page_name']"):
#("//h2[@class='page_name']"):
#    img = block.xpath("//img/@src")[0]
#    name = block.xpath("//tr[@class='name']")[0].text
#    id = block.xpath("//tr[@class='id']")[0].text