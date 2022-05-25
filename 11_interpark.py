#인터파크 베스트 아이템(순위, 제품명, 가격, 무료배송여부) 크롤러
from urllib.request import urlopen

url = 'https://shopping.interpark.com/best/main.do'

htmlData = urlopen(url).read()

htmlData=htmlData.decode('utf8')

from bs4 import BeautifulSoup as bs

html = bs(htmlData, 'html.parser')

name = html.select('.name')
num = html.select('.number')
benefit = html.select('.benefit')
rank = html.select('h3')

for i in range (len(name)):
  price = num[i].text.replace(',','')
  ben = benefit[i].text.replace('\n','')
  ran = rank[i].text
  if ben == '':
    line = f'{ran}, {name[i].text}, {int(price)}원, 유료배송'
  else:
    line = f'{ran}, {name[i].text}, {int(price)}원, {str(ben)}'
  print(line)

