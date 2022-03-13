import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('Ocorreu um erro ao abrir o site :(')
else:
    print('Site aberto com sucesso!!!')
