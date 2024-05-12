import requests

cep = '20090002'

cep = cep.replace("-", "").replace(".", "".replace(" ", ""))

if len(cep) == 8:
  link = f'https://viacep.com.br/ws/01001000/json'

  request = requests.get(link)
  request_dic = request.json()

  uf = request_dic['uf']
  city = request_dic['localidade']
  neighborhood = request_dic['bairro']
  print(uf, city, neighborhood)
else:
  print('CEP inválido')