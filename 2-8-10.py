from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# HTML 가져오기
base = "https://search.naver.com/search.naver?where=image&query="
quote = rep.quote_plus("사자")
url = base + quote

# print(url)

res = req.urlopen(url)
savePath ="C:\\imagedown\\"

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

soup = BeautifulSoup(res, "html.parser")
#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(1) > div > div.thumb.__web-inspector-hide-shortcut__ > a > img
#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-childs > div > div.thumb
#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(2) > div > div.thumb > a
print(soup.prettify())
 # > a.link_thumb._imageBox._infoBox
#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(5) > div > div.thumb
# > div > div > div.thumb.__web-inspector-hide-shortcut__ > a > img
# li_list = soup.find("div",{"class" : "thumb"})
# print(li_list)
# for div in li_list:
#   print("div =", div)
  # fullfilename = os.path.join(savePath, savePath+str(i)+'.jpg')
  # print(fullfilename)
  # req.urlretrieve(div['data-source'],fullfilename)
  # print(i)
