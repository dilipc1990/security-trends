from lxml import etree
import urllib2
import csv

strURL="https://www.databreaches.net/2015/02/feed/,https://www.databreaches.net/2014/02/feed/,https://www.databreaches.net/2014/03/feed/,https://www.databreaches.net/2014/04/feed/,https://www.databreaches.net/2014/05/feed/,https://www.databreaches.net/2014/06/feed/,https://www.databreaches.net/2014/07/feed/,https://www.databreaches.net/2014/08/feed/,https://www.databreaches.net/2014/09/feed/,https://www.databreaches.net/2014/10/feed/,https://www.databreaches.net/2014/01/feed/,https://www.databreaches.net/2014/11/feed/,https://www.databreaches.net/2014/12/feed/,https://www.databreaches.net/2015/01/feed/,https://www.databreaches.net/2015/03/feed/,https://www.databreaches.net/2015/04/feed/,https://www.databreaches.net/2015/05/feed/,https://www.databreaches.net/2015/06/feed/,https://www.databreaches.net/2015/07/feed/,https://www.databreaches.net/2015/08/feed/,https://www.databreaches.net/2015/09/feed/,https://www.databreaches.net/2015/10/feed/,https://www.databreaches.net/2015/11/feed/,https://www.databreaches.net/2016/01/feed/,https://www.databreaches.net/2016/02/feed/,https://www.databreaches.net/2016/03/feed/,https://www.databreaches.net/2016/04/feed/,https://www.databreaches.net/2016/05/feed/,https://www.databreaches.net/2016/06/feed/,https://www.databreaches.net/2016/07/feed/,https://www.databreaches.net/2016/08/feed/,https://www.databreaches.net/2016/09/feed/,https://www.databreaches.net/2013/01/feed/,https://www.databreaches.net/2013/02/feed/,https://www.databreaches.net/2013/03/feed/,https://www.databreaches.net/2013/04/feed/,https://www.databreaches.net/2013/05/feed/,https://www.databreaches.net/2013/06/feed/,https://www.databreaches.net/2013/07/feed/,https://www.databreaches.net/2013/08/feed/,https://www.databreaches.net/2013/09/feed/,https://www.databreaches.net/2013/10/feed/,https://www.databreaches.net/2013/11/feed/,https://www.databreaches.net/2013/12/feed/,https://www.databreaches.net/2012/01/feed/,https://www.databreaches.net/2012/02/feed/,https://www.databreaches.net/2012/03/feed/,https://www.databreaches.net/2012/04/feed/,https://www.databreaches.net/2012/05/feed/,https://www.databreaches.net/2012/06/feed/,https://www.databreaches.net/2012/07/feed/,https://www.databreaches.net/2012/08/feed/,https://www.databreaches.net/2012/09/feed/,https://www.databreaches.net/2012/10/feed/,https://www.databreaches.net/2012/11/feed/,https://www.databreaches.net/2012/12/feed/,https://www.databreaches.net/2011/01/feed/,https://www.databreaches.net/2011/02/feed/,https://www.databreaches.net/2011/03/feed/,https://www.databreaches.net/2011/04/feed/,https://www.databreaches.net/2011/05/feed/,https://www.databreaches.net/2011/06/feed/,https://www.databreaches.net/2011/07/feed/,https://www.databreaches.net/2011/08/feed/,https://www.databreaches.net/2011/09/feed/,https://www.databreaches.net/2011/10/feed/,https://www.databreaches.net/2011/11/feed/,https://www.databreaches.net/2011/12/feed/,https://www.databreaches.net/2010/01/feed/,https://www.databreaches.net/2010/02/feed/,https://www.databreaches.net/2010/03/feed/,https://www.databreaches.net/2010/04/feed/,https://www.databreaches.net/2010/05/feed/,https://www.databreaches.net/2010/06/feed/,https://www.databreaches.net/2010/07/feed/,https://www.databreaches.net/2010/08/feed/,https://www.databreaches.net/2010/09/feed/,https://www.databreaches.net/2010/10/feed/,https://www.databreaches.net/2010/11/feed/,https://www.databreaches.net/2010/12/feed/,https://www.databreaches.net/2009/01/feed/,https://www.databreaches.net/2009/02/feed/,https://www.databreaches.net/2009/03/feed/,https://www.databreaches.net/2009/04/feed/,https://www.databreaches.net/2009/05/feed/,https://www.databreaches.net/2009/06/feed/,https://www.databreaches.net/2009/07/feed/,https://www.databreaches.net/2009/08/feed/,https://www.databreaches.net/2009/09/feed/,https://www.databreaches.net/2009/10/feed/,https://www.databreaches.net/2009/11/feed/,https://www.databreaches.net/2009/12/feed/"
URL = strURL.split(",")
country=""
for i in URL:
	print i
	
	headers = { 'User-Agent' : 'Mozilla/5.0' }
	req = urllib2.Request(i, None, headers)
	reddit_file = urllib2.urlopen(req).read()

	reddit = etree.fromstring(reddit_file)

	with open('test1.csv', 'a') as testfile:
	 csv_writer = csv.writer(testfile,lineterminator='\n',)
	 for item in reddit.xpath('/rss/channel/item'):
		 try:
			data = [  item.xpath("./title/text()")[0].encode("utf-8"),
			item.xpath("./description/text()")[0].encode("utf-8"), item.xpath("./pubDate/text()")[0].encode("utf-8")]
			varLen = len(item.xpath("./category/text()"))
			for j in range(varLen):
				value=""
				if (item.xpath("./category/text()")[j].upper() == "U.S."):
					country='U.S'
				elif (item.xpath("./category/text()")[j].upper() == "NON-U.S."):
					country='Non-U.S'
				else : value = item.xpath("./category/text()")[j]
				
				data.append(value)
			data.insert(0, country)
			csv_writer.writerow(data)
		 except Exception as e:
				print str(e)