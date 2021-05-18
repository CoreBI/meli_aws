import urllib2
page =urllib2.urlopen("https://www.collinsdictionary.com/browse/english/words-starting-with-a")
print(page.read())

