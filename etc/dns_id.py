# Import requests and os
import requests
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Set the parameters for the Cloudflare API
zone_id = os.getenv("CLOUDFLARE_ZONE")
api_token = os.getenv("CLOUDFLARE_TOKEN")
dns_record_name = os.getenv("CLOUDFLARE_DND")

# Set the URL for the Cloudflare API request
url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type=A&name={dns_record_name}'

# Set the headers for the Cloudflare API request
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

# Send the request to the Cloudflare API
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Get the DNS record ID from the response
    dns_record_id = response.json()['result'][0]['id']
    print(f'DNS record ID for {dns_record_name}: {dns_record_id}')
else:
    print(f'Failed to retrieve DNS record ID: {response.text}')
