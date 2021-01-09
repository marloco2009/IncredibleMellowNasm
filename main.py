

"""line2 = []
for line in urllib.request.urlopen("https://github.com/JEOS19/fabricantes_pymatrix/blob/main/fabricantes_c%C3%B3digos_nombres.txt"):
  line2.append(line)
  print(line2)
from urllib.request import urlopen
data = urlopen("https://github.com/JEOS19/fabricantes_pymatrix/blob/main/fabricantes_c%C3%B3digos_nombres.txt")
print(data)"""
"""import urllib.request
import urllib
txt = urllib.request.urlopen("https://es.scribd.com/document/490176746/fabricantes-codigos-nombres").read() 
print(txt)"""
"""import urllib.request  # the lib that handles the url stuff

for line in urllib.request.urlopen("http://lib.stat.cmu.edu/datasets/boston"):
    print(line.decode('utf-8'))"""
"""import requests
response = requests.get("https://github.com/JEOS19/fabricantes_pymatrix/blob/main/fabricantes_c%C3%B3digos_nombres.txt")
data = response.text
for i, line in enumerate(data.split('\n')):
    print(f'{i}   {line}')"""


"""import urllib3

http = urllib3.PoolManager()
response = http.request('GET', "https://github.com/JEOS19/fabricantes_pymatrix/blob/main/fabricantes_c%C3%B3digos_nombres.txt")
data = response.data.decode('utf-8')"""

"""import requests

response = requests.get("https://github.com/JEOS19/fabricantes_pymatrix/blob/main/fabricantes_c%C3%B3digos_nombres.txt")
data = response.text
print(data)
import requests

response = requests.get('https://github.com/JEOS19/fabricantes_pymatrix/blob/main/fabricantes_c%C3%B3digos_nombres.txt')
data = response.text
for i, line in enumerate(data.split('\n')):
    if i>1024:
        print(f'{i}   {line}' )"""
"""import requests
url = 'https://github.com/marloco2009/fabricantes/blob/main/fabricantes_c%C3%B3digos_nombres.txt'
page = requests.get(url)
print (page.text)"""


#¿ESTO ES LO IMPORTANTE CIERTO?
#hay algo raro, los comprobantes que escupe cada codigo es diferente, unas comienzan con huawei otras con zte
#prueba cada cod y te das cuenta que esta rarisimo
"""import requests
response = requests.get('https://github.com/marloco2009/fabricantes/blob/main/fabricantes_c%C3%B3digos_nombres.txt')
data = response.text

for i, line in enumerate(data.split('\n')):
    print(f'{i}   {line}')
"""
#este de aca con huawei y no se porque



import requests
response = requests.get('https://drive.google.com/file/d/13G67DwRUQb_rVsbdJHiLTa8ApjwC9uEN/view')
data = response.text
#for linea in data:
 # print(linea)
  
print(data)
#este de aqui empieza con zte
    
#mira, creo que deberiamos crear una pagina en python, porque todas las paginas web estan en html
#y esto lo lee como html 
#pero deberiamos hacer un repositorio para poner el txt oa lo mejor creamos un archivo csv, donde los datos de la pg se vayan agregandi o escribiendo en el csv, y de ahi podriamos trabajar con un readline,no se, vamos al zoom, dale, podrias madrugar?
#vale, deja termino esto xD
#mi mama me ayuda, so
#esto es lo que deberia leer 
"""código,nombre
709F2D,zte corporation
E4B021,Samsung Electronics Co.
D0F88C,Motorola (Wuhan) Mobility Technologies Communication Co.
D4C1C8,zte corporation
88D274,zte corporation"""
