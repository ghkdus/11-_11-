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

#베스트 아이템을 모두 구입하면 얼마를 지불해야 할까요?
#유료배송의 경우 배송비는 2500원입니다.
#단, 유료배송 제품의 경우 처음 한 번만 배송비를 지불합니다.

n=int(input('인터파크 베스트 아이템을 몇개씩 주문할까요?:'))
totalprice = 0

if n == 0:
  print('배송료를 포함한 총 금액은 0원입니다.\n이용해주셔서 감사합니다.')
elif n==1:
  order=0
  for i in range(len(name)):
    price = int(num[i].text.replace(',',''))
    totalprice = totalprice+price
    ben = benefit[i].text.replace('\n','')
    if ben!='무료배송':
      order = order + 2500
  print(f'배송료를 포함한 총 금액은 {totalprice+order}원 입니다.\n이용해주셔서 감사합니다.')
elif n>1:
  order=0
  for i in range(len(name)):
    price = int(num[i].text.replace(',',''))
    totalprice = totalprice+price
    ben = benefit[i].text.replace('\n','')
    if ben !='무료배송':
      order = order + 2500
  print(f'배송료를 포함한 총 금액은 {n*totalprice + order}원 입니다.\n이용해주셔서 감사합니다.')
