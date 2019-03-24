import requests
header={'X-ApiKeys': 'accessKey=12300ab3bc4504d10c3ac3bb1b5f84ef7c49f6cf6b0a059fcf05099be8d1ee62; secretKey=b799df02cc38e8baa622b4ab9e659703eaf286c06426628a266cffb320393275;'}
for i in range(11930,100000,1):
	try:
		url="https://127.0.0.1:8834/plugins/plugin/"+str(i)
		sonuc=requests.get(url=url,headers=header,verify=False)
		cikti=sonuc.json()
		#print cikti
		print "ID:",cikti['id']
		for j in cikti['attributes']:
			if "plugin_name" in j['attribute_name']:
				print j["attribute_value"]
				log=str(j["attribute_value"])+"|"+str(cikti['id'])+"\n"
				dosya=open("nessusPlugin.csv","a")
				dosya.write(log)
				dosya.close()
	except:
		pass

