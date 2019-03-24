import datetime
import requests
dosya=open("birinci.txt","r")
icerik=dosya.read()
dosya.close()
eskiIPler=[]
for i in str(icerik).split("\n"):
	print i
	eskiIPler.append(str(i))
print eskiIPler
dosya=open("ikinci.txt","r")
icerik=dosya.read()
dosya.close()
for i in str(icerik).split("\n"):
	print str(i)
	print eskiIPler
	if str(i) in eskiIPler:
		print "Envanterde bulunan asset"
	else:
		print "Envanterde asset yok:",str(i)
		zaman=datetime.datetime.now()
		log=str(zaman)+"|Yeni asset:"+str(i)+"\n"
		dosya=open("yeniassetLog.txt","a")
		dosya.write(log)
		dosya.close()
		veri={'api_key':'4642e3d1','api_secret':'4HxSMkDdy2HnHak1','to':'905379126183','from':'NEXMO','text':'Yeni host bulundu'}
		url="https://rest.nexmo.com/sms/json"
		requests.post(url=url,data=veri,verify=False)
