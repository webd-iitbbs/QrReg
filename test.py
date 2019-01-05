import requests

url = "https://qrcode-monkey.p.mashape.com/qr/custom"
data = {
		'data':'https://www.qrcode-monkey.com',
		'config':{
				'body':'circle',
				'logo':'#facebook'
				},
		'size':300,
		'download':False,
		'file':'svg'
	    }

r = requests.post(url = url, data = data)

print (r)