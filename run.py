import requests
import json
from Service import Service

# Consul API url
consulurl = 'http://demo.consul.io/v1/catalog/services'

# Parse json to dictionary
contents = requests.get(consulurl).text
services = json.loads(contents)

# Print services and IPs
for service in services:
    print("Service Name: " + str(service).upper() + "\nService IPs: " + str(Service.getServiceIP(service)) + "\n")



