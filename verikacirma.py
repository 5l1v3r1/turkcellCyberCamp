import requests
dosya=open("kritik.txt","r")
icerik=dosya.read()
dosya.close()
for i in icerik.split(" "):
	print i
	url="http://127.0.0.1/barikat-"+str(i)
	print url
	requests.get(url)
