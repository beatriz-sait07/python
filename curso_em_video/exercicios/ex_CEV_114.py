import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('deu erro!')
else:
    print('entrou!')
    
#print(site.read) //acessa o site