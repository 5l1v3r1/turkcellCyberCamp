import requests
header={'X-ApiKeys': 'accessKey=12300ab3bc4504d10c3ac3bb1b5f84ef7c49f6cf6b0a059fcf05099be8d1ee62; secretKey=b799df02cc38e8baa622b4ab9e659703eaf286c06426628a266cffb320393275;'}
url="https://127.0.0.1:8834/folders"
sonuc=requests.get(url=url,headers=header,verify=False)
print sonuc.json()

