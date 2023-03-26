# Import requests and os
import requests
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Set the parameters for the Cloudflare API
api_token = os.getenv("CLOUDFLARE_TOKEN")
domain = os.getenv("CLOUDFLARE_DOMAIN")


# Set the URL for the Cloudflare API request
url = f'https://api.cloudflare.com/client/v4/zones?name={domain}'

# Set the headers for the Cloudflare API request
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

# Send the request to the Cloudflare API
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Get the Zone ID from the response
    zone_id = response.json()['result'][0]['id']
    print(f'Zone ID for {domain}: {zone_id}')
else:
    print(f'Failed to retrieve Zone ID: {response.text}')
