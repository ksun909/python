import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url1="https://ssl.pstatic.net/melona/libs/1399/1399998/3c388543b5b287ba01af_20220630100624832.jpg"
url2="https://tv.naver.com/v/28039069"
path1="C:/Users/ksun9/OneDrive/바탕 화면/!!!Python/section2/t101.jpg"
path2="C:/Users/ksun9/OneDrive/바탕 화면/!!!Python/section2/t102.htm"

req.urlretrieve(url1,path1)
req.urlretrieve(url2,path2)
# f=req.urlopen(url2)
# print(f.status)
# print(f.geturl())

# print("headers :",mem.getheaders())
# print("info :",mem.info(),"\n")
# print("getcode :",mem.getcode())
# print("read :",mem.read(10).decode('utf-8'))
# print(urlparse('http://www.encar.co.kr?test=test').query)
?
# print("headers :",mem.getheaders())
# print("info :",mem.info(),"\n")
# print("getcode :",mem.getcode())
# print("read :",mem.read(10).decode('utf-8'))
# print(urlparse('http://www.encar.co.kr?test=test').query)
# print("headers :",mem.getheaders())
# print("info :",mem.info(),"\n")
# print("getcode :",mem.getcode())
# print("read :",mem.read(10).decode('utf-8'))
# print(urlparse('http://www.encar.co.kr?test=test').query)).decode('utf-8'))
