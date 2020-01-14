import urllib.request,urllib.response
import  json
ak = 'k3PezGsgOKhaVbEQUsqV8xQe'
sk = 'TKlIbYYMhlCP4U95ZR6kcQ6rMcGGl3mz'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' %(ak,sk)
request = urllib.request.Request(host)
request.add_header('Content-Type','application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
json_all = json.loads(response)
access_token = json_all['access_token']
print (access_token)