#!/usr/bin/python
import sys
from service import GetServices


# Consul API catalog url
consul_catalog = 'http://demo.consul.io/v1/catalog'


def main(user_url):
    # Check for user input
    if len(user_url) > 1:
        consul_url = user_url[1]
    else:
        # If not, use default url
        consul_url = consul_catalog
    GetServices(consul_url)


if __name__ == '__main__':
    sys.exit(main(sys.argv))

