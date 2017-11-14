# caching
# HTTP headers: Cache-Control, Last-Modified (304: Not Modified), If-Modified-Since
#   ETag (If-No-Match)

# compression
# gzip and deflate
# HTTP headers: Accept-encoding, Content-encoding

# redirects
# 302 response - temporary redirect
# 301 response - permanent redirect

# python native http modules do not support caching, compression, redirects
# httplib2 supports caching, compression, redirects
import httplib2

h = httplib2.Http('.cache')

response, content = h.request('https://www.theregister.co.uk/emergent_tech/artificial_intelligence/headlines.atom',
  headers={'cache-control':'no-cache'}) # bypass all cache servers

print(response.status)
print(response.fromcache)