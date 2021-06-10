'''
26. Write a Python program to display the contains of different attributes
like different attributes like status_code, headers, url, history, encoding,
reason, cookies, elapsed, request and content of a specified resource.

'''

import requests
response = requests.get('https://python.org')
print("Status Code: ",response.status_code)
print("Headers: ",response.headers)
print("Url: ",response.url)
print("History: ",response.history)
print("Encoding: ",response.encoding)
print("Reason: ",response.reason)
print("Cookies: ",response.cookies)
print("Elapsed: ",response.elapsed)
print("Request: ",response.request)
print("Content: ",response._content)