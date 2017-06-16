from bs4 import BeautifulSoup
import re, io, sys
import urllib2
import chardet
reload(sys)
sys.setdefaultencoding('GB2312')
def readURL():
    #response = urllib2.urlopen("http://www.mof.gov.cn/zhengwuxinxi/zhengcefabu/")#"http://www.baidu.com")
    #response = urllib2.urlopen("http://szs.mof.gov.cn/zhengwuxinxi/zhengcefabu/201706/t20170613_2622005.html")
    response = urllib2.urlopen("http://nys.mof.gov.cn/zhengfuxinxi/czpjZhengCeFaBu_2_2/201706/t20170608_2618683.html")
    doc = response.read()
    print chardet.detect(doc)['encoding']
    print isinstance(doc, unicode)

    doc = doc.decode("GB2312", 'ignore').encode("GB2312", 'ignore')
    fp = open("zhengce2.html", 'w')
    fp.write(doc)
    fp.close()
    return doc
def readDoc():
    f = open("zhengce2.html")
    doc = f.read()
    f.close()
    return doc
    
def get_info():
    #readURL()
    doc = readDoc()
    #print doc.decode("GBK").encode("GBK", 'ignore')
    soup = BeautifulSoup(doc, from_encoding = 'gb18030')
    print soup.original_encoding
    #print soup.prettify().encode("utf-8")
    print soup.title.string
    print soup.p.get_text().encode("GB2312", 'ignore')
    print soup.find_all("p",align="right")[0].get_text().encode("GB2312", 'ignore')
    print soup.find_all("p",align="right")[1].get_text().encode("GB2312", 'ignore')
    print soup.find_all("p",align="justify")[0].get_text().encode("GB2312", 'ignore')
    print "\n政策正文：".decode("utf-8")
    for i in range(1, len(soup.find_all("p",align="justify"))):
        print soup.find_all("p",align="justify")[i].get_text().encode("GB2312", 'ignore')

if __name__ == "__main__":
    get_info()