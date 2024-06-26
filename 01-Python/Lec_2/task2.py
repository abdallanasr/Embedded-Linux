import requests
import webbrowser

ip_response = requests.get("https://api.ipify.org/?format=json")
ip_address = ip_response.json()["ip"]

location_response = requests.get(f"https://ipinfo.io/{ip_address}/geo")
location_data = location_response.json()

print(f"I'm currently in {location_data['city']}, {location_data['country']}.")
