from .models import Pessoa

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