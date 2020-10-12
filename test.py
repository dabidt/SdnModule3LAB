import requests
import pprint


from requests.auth import HTTPBasicAuth

USER = "devnetuser"
PASS = "Cisco123!"


URL = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"

headers = {'Content-Type': 'application/json'}

response = requests.post(URL, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)

token = response.json()['Token']

URL2 = "https://sandboxdnac.cisco.com/dna/intent/api/v1/interface/ospf"


getHeader = {'Accept': 'application/json', 'X-auth-token': token}



getResponse = requests.get(URL2, headers=getHeader, verify=False)

devices = getResponse.json()['response'][0]


totalSold = devices['speed']
pizzaSales = devices['status']
deli = devices['lastUpdated']
print("Total Pizzas Sold: " + totalSold )
print("Pizza sales are: " + pizzaSales)
print("Latest pizza delivery " + deli)
