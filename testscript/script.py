import urllib

opener = urllib.build_opener()

opener.addheaders = [('Accept', 'application/vnd.crossref.unixsd+xml')] r = opener.open('http://dx.doi.org/10.5555/515151') print r.info()['Link']
