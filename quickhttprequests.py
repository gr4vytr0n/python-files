from http.client import HTTPConnection
import urllib.request

url = 'https://www.theregister.co.uk/emergent_tech/artificial_intelligence/headlines.atom'
response = urllib.request.urlopen(url)
print(response.headers.as_string())
