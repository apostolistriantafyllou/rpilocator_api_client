from win10toast_click import ToastNotifier
from ast import literal_eval
import requests, time, webbrowser

#default port is 3000
apiurl = "example.com:port"

def onclick(url):
	webbrowser.open(url, new=0, autoraise=True)

while True:
	r = requests.get('http://' + apiurl + '/pi4-stockcheck/[4,8]')
	if r.text != 'null':
		pilist = literal_eval(r.text)
		for res in pilist:
			notification = ToastNotifier()
			notification.show_toast(
				title = "Raspberry Pi 4 8gb in stock!!!! price: " + res[1],
				msg = "url: " + res[0],
				threaded=True,
				duration=60,
				callback_on_click = lambda: onclick(res[0]),
				icon_path = './raspi.ico'
			)
	time.sleep(60)
