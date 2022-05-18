import json

import requests

url="https://noss.qa.tcshuke.com/__authz_client_resources_/login"
data={
    "password":"bufu@2015",
    "account":"tongshuai.jia",
    "url":"http%3A%2F%2Fjr.qa.17usoft.net%2Fins-noss%2Fhome"
}
resp=requests.post(url=url,params=data)
cookies =resp.cookies
# print(cookies)
header={"Content-Type":"application/x-www-form-urlencoded; charset\u003dUTF-8"}
# getMemberName
url2="https://noss.qa.tcshuke.com/newOfflineRepay/getMemberName?memberId=1249536822"
print(requests.get(url=url2,cookies=cookies).text)