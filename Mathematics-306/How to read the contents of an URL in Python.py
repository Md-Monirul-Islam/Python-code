from http.client import HTTPConnection
conn = HTTPConnection("Example.com")
conn.request('GET','/')
result = conn.getresponse()
# Retrives the entire contents.
contents = result.read()
print(contents)