import requests

url = "https://httpbin.org/ip"

response = requests.get(url)
json_data = response.json()

ip = json_data['origin']

if "," in ip:
    print("Your IP Addresses are:")
    iplist = ip.split(",")
    print(",".join(iplist))
else:
    print(f"Your IP Address is: {ip}")