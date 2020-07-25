import urllib
import urllib.request

web="http://www.pudim.com.br"

try:
    site=urllib.request.urlopen(web)
except:
    print("Deu erro!")
else:
    print("Tudo OK!")
     