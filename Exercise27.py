'''27. Write a Python program to verifiy SSL certificates for HTTPS
requests using requests module.
Note: Requests verifies SSL certificates for HTTPS requests, just like
a web browser. By default, SSL verification is enabled, and Requests
will throw a SSLError if it's unable to verify the certificate

'''

import requests
print(requests.get('https://w3resource.com'))
print(requests.get('https://wayback.com'))