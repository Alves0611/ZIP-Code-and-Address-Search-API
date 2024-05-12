import requests

cep = '20090002'

link = f'https://viacep.com.br/ws/01001000/json'

request = requests.get(link)

uf = request_dic['uf']
city = request_dic['localidade']
neighborhood = request_dic['bairro']
print(uf, city, neighborhood)