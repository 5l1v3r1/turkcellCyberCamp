import requests
dosya=open("fuzzListe.txt","r")
icerik=dosya.read()
dosya.close()
for i in icerik.split("\n"):
	print i
	url="http://192.168.79.141/"+str(i)
	sonuc=requests.get(url)
	if "200" in str(sonuc.status_code):
		print "Sunucuda var:",str(i)
