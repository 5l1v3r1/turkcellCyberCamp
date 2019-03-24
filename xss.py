import requests
url="http://192.168.79.141/xss/example1.php?name=hacker"
cikti=requests.get(url)
#print cikti.content
indis=url.find("=")
#print indis
#print url[:indis+1]
dosya=open("xssPayload.txt","r")
icerik=dosya.read()
dosya.close()
for i in icerik.split("\n"):
	#print i
	istek=str(url[:indis+1])+str(i)
	sonuc=requests.get(istek)
	if str(i) in sonuc.content:
		print "XSS olabilir:",str(i)
