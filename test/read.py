# Import requests and os
import requests
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Get the values of the required environment variables
api_token = os.getenv("CLOUDFLARE_TOKEN")
zone_id = os.getenv("CLOUDFLARE_ZONE")

# Set the domain name and record type
domain_name = 'home.amirhossein.info'
record_type = 'A'

# Define the URL for the Cloudflare API endpoint
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type={record_type}&name={domain_name}"

# Set the API request headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}

# Make the API request and get the response JSON
response = requests.get(url, headers=headers)
response_json = response.json()

# Extract the IP address from the response
ip_address = response_json['result'][0]['content']

# Print the IP address
print(f"The current IP address for {domain_name} is {ip_address}")
