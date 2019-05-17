import requests
import json


class Service:
    def getServiceIP(servicename):
        # Define addresses list
        addresses = []

        # Get service details from api
        servicedetail = (requests.get('http://demo.consul.io/v1/catalog/service/' + str(servicename)))

        # Parse data to a dictionary
        data = json.loads(servicedetail.text)

        # Append service addresses to addresses list
        for address in data:
            addresses.append(address['Address'])
        # Print addresses list
        return addresses
