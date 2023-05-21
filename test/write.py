# Import requests and os
import requests
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Set the parameters for the Cloudflare API
dns_record_id = os.getenv("CLOUDFLARE_RECORD")
dns_record_name = os.getenv("CLOUDFLARE_DND")
api_token = os.getenv("CLOUDFLARE_TOKEN")
zone_id = os.getenv("CLOUDFLARE_ZONE")

# Get the current public IP
response = requests.get('https://api.ipify.org')
public_ip = response.text

# # Set the parameters for the Cloudflare API request
url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record_id}'
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}
data = {
    'type': 'A',
    'name': dns_record_name,
    'content': public_ip
}

# # Send the request to the Cloudflare API
response = requests.put(url, headers=headers, json=data)

# Check the response status code
if response.status_code == 200:
    print('DNS record updated successfully')
else:
    print(f'Failed to update DNS record: {response.text}')
