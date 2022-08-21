from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="

queto = rep.quote_plus("사자")
url = base + queto

res=req.urlopen(url).read()
soup=BeautifulSoup(res,"html.parser")

print(soup.select("#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid "))



#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(1) > div > div.thumb > a > img

print(soup)

# res = req.urlopen(url).read()
# soup = BeautifulSoup(res, "html.parser")
#
# top = soup.select("div#contents_productAd > div.list_goods_wrap > ul.list_goods > li.goods_item > a > p > span.title")
# for i,e in enumerate(top,1):
#     for x in e:
#         print(i,'=-==', x.string)

# print(top)
