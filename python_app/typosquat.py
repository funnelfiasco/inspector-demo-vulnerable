#!/usr/bin/python3

import request
import sys

url = "https://api.github.com/events"
response = request.get(url)

# Accessing response data
print(f"Status Code: {response.status_code}")

sys.exit(0)
