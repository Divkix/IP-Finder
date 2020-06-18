import requests

url = "https://httpbin.org/ip"

response = requests.get(url)
json_data = response.json()

ip = json_data['origin']

if "," in ip:
    print(f"Your IP Addresses are:")
    ip1, ip2 = ip.split(",")[0], ip.split(",")[1]
    print(f"{ip1}\n{ip2}")
else:
    print(f"Your IP Address is: {ip}")