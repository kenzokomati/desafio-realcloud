from .models import Pessoa
import requests


def totalsum_pessoa():
  quantity_list = Pessoa.objects.values_list('quantity', flat=True) 
  return sum(quantity_list)

def average_pessoa():
  averageMoney = 0
  quantity_list = Pessoa.objects.values_list('quantity', flat=True) 
  totalsum = sum(quantity_list)
  record_num = len(quantity_list)
  if record_num > 0:
    averageMoney = totalsum / record_num
  return averageMoney

def obter_valor_dolar():
  url = "https://open.er-api.com/v6/latest/USD"
  
  try:
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    valor_dolar = data['rates']['BRL']
    return valor_dolar
  except requests.exceptions.RequestException as e:
    print("Erro ao acessar a API:", e)
    return None