import requests

cep = '01001000'

cep = cep.replace("-", "").replace(".", "".replace(" ", ""))

if len(cep) == 8:
  link = f'https://viacep.com.br/ws/{cep}/json'

  request = requests.get(link)
  request_dic = request.json()

  uf = request_dic['uf']
  city = request_dic['localidade']
  neighborhood = request_dic['bairro']
  print(uf, city, neighborhood)
else:
  print('CEP inválido')

uf = 'RJ'
city = 'Rio de Janeiro'
street = 'Rio Branco'

link = f'https://viacep.com.br/ws/{uf}/{city}/{street}/json/'

request = requests.get(link)
print(request)

request_dic = request.json()
print(request_dic)