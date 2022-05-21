import requests
import pprint
import json
#파이썬 api 가져오기
#request.get을 사용하면 get request를 보냈을 때 파라미터를 얻을 수 있음.
#request.get의 의미 -> request이름의 객체에 대해서 get 메소드를 실행함

url = 'http://api.data.go.kr/openapi/tn_pubr_public_pblprfr_event_info_api?serviceKey=GGptI85bzwAdmoMUMJHhH5vxdSEnRs2sQiw66nGoeiuIOOuKS02DamuwgoP6ARuyFWbjBIqavKEotsahY5Dc8g%3D%3D&pageNo=0&numOfRows=100&type=xml'
response = requests.get(url)
print(response.text)

