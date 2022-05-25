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


  #인터파크 베스트 아이템을 csv 파일로 작성해보기
with open('interpark.csv', 'w') as fp:
  line='순위, 제품명, 가격, 배송료\n'
  fp.write(line)
  for i in range (len(name)):
    price = num[i].text.replace(',','')
    ben = benefit[i].text.replace('\n','')
    ran = rank[i].text
    if ben == '':
      line = f'{ran}, {name[i].text}, {int(price)}원, 유료배송\n'
    else:
      line = f'{ran}, {name[i].text}, {int(price)}원, {str(ben)}\n'
    fp.write(line)

#베스트 아이템 순위 비교 시스템
n=list(map(int, input('몇 번째 순위의 베스트 아이템을 비교할까요?(입력 예시:1 2 3):').split()))

for i in n:
  price = num[i-1].text.replace(',','')
  ben = benefit[i-1].text.replace('\n','')
  ran = rank[i-1].text
  if ben == '':
    line = f'{ran}, {name[i-1].text}, {int(price)}원, 유료배송'
  else:
    line = f'{ran}, {name[i-1].text}, {int(price)}원, {str(ben)}'
  print(line)

with open('interpark_vigyo.csv', 'w') as fp:
  line='순위, 제품명, 가격, 배송료\n'
  fp.write(line)
  for i in n:
    price = num[i-1].text.replace(',','')
    ben = benefit[i-1].text.replace('\n','')
    ran = rank[i-1].text
    if ben == '':
      line = f'{ran}, {name[i-1].text}, {int(price)}원, 유료배송\n'
    else:
      line = f'{ran}, {name[i-1].text}, {int(price)}원, {str(ben)}\n'
    fp.write(line)
