import requests
import webbrowser

response = requests.get("https://api.ipify.org/?format=json")

ip_address = response.json()['ip']

webbrowser.open(f"https://ipinfo.io/{ip_address}/geo")

