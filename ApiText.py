import urllib.request,urllib.parse
import json

ak = 'k3PezGsgOKhaVbEQUsqV8xQe'
sk = 'TKlIbYYMhlCP4U95ZR6kcQ6rMcGGl3mz'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' %(ak,sk)
#https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=k3PezGsgOKhaVbEQUsqV8xQe&client_secret=TKlIbYYMhlCP4U95ZR6kcQ6rMcGGl3mz
request = urllib.request.Request(host)
request.add_header('Content-Type','application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
json_all = json.loads(content)
access_token = json_all['access_token']
#print (json_all)


url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s' %access_token
data = urllib.parse.urlencode(
    {'image':'http://web1908121113004.bj01.bdysite.com/abc/python.jpg',
     'detect_language': 'true'
     }).encode()
req = urllib.request.Request(url,method='POST')
req.add_header('Content-Type','application/x-www-form-urlencoded')
res = urllib.request.urlopen(req,data).read().decode('utf-8')
ocr = json.loads(res)
print (ocr)
for item in ocr['words_result']:
   print (item['words'])

