import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="https://www.naver.com"
save1="C:/Users/ksun9/OneDrive/바탕 화면/!!!Python/section2/t13.html"

req.urlretrieve(url,save1)
