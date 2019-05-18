# MobileyeConsul
#### This script discovers which services a server exposes, and their Internal IPs.

## Prerequisites
* Make sure you have Python installed.
* Don't forget to install the included Python modules:
    ```
    pip install requests
    ```

## Getting Started
1. Clone this repository to your server or workstation:
    ```
    git clone https://github.com/amitde69/MobileyeConsul.git
    ```

1. Start the script by running: 
    ```
    ./get_services.py <SERVICE_URL>
    ```
    if you don't provide a SERVICE_URL, the default http://demo.consul.io/ URL will be used.
