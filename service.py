import requests, json, os


class GetServices:
    def __init__(self, consul_url):
        # Consul API service url
        self.consul_service = (consul_url + '/service/')
        # Consul API services url
        self.consul_services = (consul_url + '/services')
        self.print_services()

    def print_services(self):
        # Print services and IPs
        for service in self.get_all_services():
            print("Service Name: " + str(service).upper() + "\nService IPs: "
                  + str(self.get_service_ip(service)) + "\n")

    def get_all_services(self):
        contents = requests.get(self.consul_services).text
        # Parse json to dictionary
        services = json.loads(contents)
        return services

    def get_service_ip(self, service_name):
        # Define addresses list
        addresses = []

        # Get service details from api
        service_details = (requests.get(self.consul_service + str(service_name)))

        # Parse data to a dictionary
        data = json.loads(service_details.text)

        # Append service addresses to addresses list
        for address in data:
            addresses.append(address['Address'])

        # Print addresses list
        return addresses
