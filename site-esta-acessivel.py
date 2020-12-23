import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.specializzata.com.br")
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento")
else:
    print("Tudo ok!")
    print(site.read())