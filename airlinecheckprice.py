#星悅航空機票查詢  相關影片:https://www.youtube.com/watch?v=gCd3Fh9w3Do
import requests
from bs4 import BeautifulSoup as bs
rs = requests.session()
get_rs = rs.get('https://www.starflyer.jp/int_tw/fare/fare_list/universe.html')
soup = bs(get_rs.text,'html.parser')
x=[]
y=[]
for i in soup.select('.m-link-l'):
    x.append(i.text)
for r in soup.select('.m-txt-price'):
    y.append(r.text)
print('STAR UNIVERSE價格')
print('當日也OK！ 即使遇到突然休假或者緊急出差等狀況時也可變更預訂， 適用於靈活彈性的旅程。')
print('------------------------------------------------------')
for a,b in zip(x,y):
    print(a,b)
    print('------------------------------------------------------')
        
        
   


rs2 = requests.session()
get_rs2 = rs2.get('https://www.starflyer.jp/int_tw/fare/fare_list/planet.html')
soup = bs(get_rs2.text,'html.parser')
x1=[]
y1=[]
for i in soup.select('.m-link-l'):
    x1.append(i.text)
for r in soup.select('.m-txt-price'):
    y1.append(r.text)
print('STAR PLANET價格')
print('登機3天前也有合理的價格！即將出發前也可享有划算的旅程。')
print('------------------------------------------------------')
for a,b in zip(x1,y1):
    print(a,b)
    print('------------------------------------------------------')



rs3 = requests.session()
get_rs3 = rs3.get('https://www.starflyer.jp/int_tw/fare/fare_list/comet.html')
soup = bs(get_rs3.text,'html.parser')
x2=[]
y2=[]
for i in soup.select('.m-link-l'):
    x2.append(i.text)
for r in soup.select('.m-txt-price'):
    y2.append(r.text)
print('STAR COMET價格')
print('登機7天前的限定票價！早期預訂時可使用的最便宜票價。')
print('------------------------------------------------------')
for a,b in zip(x2,y2):
    print(a,b)
    print('------------------------------------------------------')