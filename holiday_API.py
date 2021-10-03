from urllib import parse
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
def get_request_query(url, operation, params, serviceKey):
  params = urlparse.urlencode(params)
  request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
  return request_query
URL = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'
OPERATION = 'getHoliDeInfo' # 국경일 + 공휴일 정보 조회 오퍼레이션
SERVICEKEY = ""
solYear  = '2020'
PARAMS = {'solYear':solYear, 'numOfRows': 50}
request_query = get_request_query(URL, OPERATION, PARAMS, SERVICEKEY)
response = requests.get(request_query,verify = False)
soup = BeautifulSoup(response.text)
items = soup.find('items')
for item in items:
	item_dict = {
		"name" : item.find("datename").text.strip(),
		"date" : datetime.strptime(item.find("locdate").text.strip(), '%Y%m%d')
		}
	item_list.append(item_dict)
 
