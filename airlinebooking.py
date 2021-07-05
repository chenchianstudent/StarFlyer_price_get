#星月航空機票查詢  相關影片:https://www.youtube.com/watch?v=gCd3Fh9w3Do
import requests
from bs4 import BeautifulSoup as bs
payload = {
           'hidloc':' en_US',
           'guid':' ',
           'screenId':' BKG001',
           'contextName':' /onlinereservation',
           'multiTabAccessRequired':' false',
           'ibeScreenId':' IBE001',
           'agencyId':' ',
           'agencyManagername':'', 
           'happyHourChannel':' ',
           '_eventId':' proceed',
           'actionName':' ',
           'mapslength':' ',
           'selectedCurrency':'', 
           'locales':' en_US',
           'wvm':' WVMD',
           'TKN_EXCHG_PARAM':' 64648971EEE75CB5DACEA1C946C48EE7',
           'dateValidationRequired':' DOB,SEARCH',
           'loyaltyValidationOutput':' ',
           'tripType':' RT',
           'origin':' TPE',
           'destination':' KKJ',
           'search-date-outward':' 03/03/2020',
           'travelDate':' 03-Mar-2020',
           'search-date-return':' 04/03/2020',
           'travelDate':' 04-Mar-2020',
           'adults':' 1',
           'children':' 0',
           'infants':' 0',
           'promoCode':' ',
           'tmpCabinClass':' Economy',
           'cabinClass':' ECONOMY',
           'channel':' PB',
           'originSel':' ',        
        }
rs = requests.session()
post_response = rs.post('https://www.starflyer.jp/onlinereservation/ibe/booking',data = payload)
soup = bs(post_response.text,'html.parser')
ans = soup.find(id = "searchForm")
print(ans)


#print(driver.page_source)