from urllib.request import urlopen
import codecs
from bs4 import BeautifulSoup

# url = "http://localhost:5000"
# html = urlopen(url)
# bs = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
# print(bs)

url = "https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=107201&idx_cd=1072&freq=Y&period=N"
html = urlopen(url)
bs = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
print(bs)