#import webbrowser
testURL = 'http://auth.mercadolibre.com.ar/authorization?response_type=code&client_id=7590455332194333&redirect_uri=https://localhost:0000'
#import requests
#webbrowser.open(testURL) 
#requests.urlopen(testURL, )

# For example in your app, you can make some like this to get de auth
#import urllib

#params = urllib.urlencode({'response_type':'code', 'client_id':'7590455332194333', 'redirect_uri':'https://localhost:0000'})
#f = urllib.urlopen("https://auth.mercadolibre.com.ar/authorization?%s" % params)
#print f.geturl()

#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}

import requests
testURL = 'http://auth.mercadolibre.com.ar/authorization?response_type=code&client_id=7590455332194333&redirect_uri=https://localhost:0000'
r = requests.get(testURL, allow_redirects=True)
print(r.status_code)
print(r.url)
print(r.headers["location"])
#q = requests.post(testURL)

#print(q)
#r = requests.head(testURL)
#print(dir(u))  # useful in seeing what's there, see also help(u)
#['__doc__', '__init__', '__iter__', '__module__', '__repr__', 'close', 'code', 'fileno', 'fp', 'getcode', 'geturl', 'headers', 'info', 'msg', 'next', 'read', 'readline', 'readlines', 'url']
#u.geturl()
#print(u.url)
#print(u.text)
#TG-60903a95adfc2e000751ee47-246777298
#TG-60903ac24cdaae0007f95fcc-246777298
#2Fauthorization%3Fresponse_type%3Dcode%26client_id%3D7590455332194333%26redirect_uri%3Dhttps%253A%252F%252Flocalhost%253A3000&platform_id=ml&application_id=7590455332194333



#['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
