# Import libs
import requests
import schedule
import time
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Get the values of the required environment variables
api_token = os.getenv("CLOUDFLARE_TOKEN")
zone_id = os.getenv("CLOUDFLARE_ZONE")

# Set the domain name and record type
dns_name = os.getenv("CLOUDFLARE_DND")
record_type = 'A'


def get_public_ip():
    response = requests.get('https://api.ipify.org').text
    return response.strip()


def update_dns():
    # Get public IP
    public_ip = get_public_ip()

    # Define the URL for the Cloudflare API endpoint
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type={record_type}&name={dns_name}"

    # Set the API request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_token}'
    }

    # Make the API request and get the response JSON
    response = requests.get(url, headers=headers)
    response_json = response.json()

    # Extract the current IP address from the DNS record
    current_ip_address = response_json['result'][0]['content']

    # Check if the IP address has changed
    if public_ip != current_ip_address:
        # If the IP address has changed, update the DNS record
        dns_record_id = response_json['result'][0]['id']
        update_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record_id}"
        data = {
            "type": "A",
            "name": dns_name,
            "content": public_ip,
            "ttl": 1,
            "proxied": False
        }
        update_response = requests.put(update_url, headers=headers, json=data)
        print(f"DNS record updated: {dns_name} now points to {public_ip}")
    else:
        # If the IP address hasn't changed, do nothing
        print("IP address has not changed.")


schedule.every(1).minutes.do(update_dns)

while True:
    schedule.run_pending()
    time.sleep(1)
