from .models import Pessoa
import requests
import matplotlib.pyplot as plt
import io
import base64


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
  
import matplotlib.pyplot as plt
import io
import base64
from .models import Pessoa

import matplotlib.pyplot as plt
import io
import base64
from .models import Pessoa

def generate_graph_data():
    # Fetch all Pessoa records from the database
    pessoas = Pessoa.objects.all()

    # Prepare the data for the graph
    data = {
        'labels': [p.name for p in pessoas],  # List of names
        'values': [float(p.quantity) for p in pessoas]  # List of quantity converted to float
    }

    # Set a minimum size for the plot (this works well with small numbers of records)
    min_width = 8  # Minimum width of the plot
    min_height = 6  # Minimum height of the plot

    # Dynamically calculate figure size based on the number of records
    num_records = len(data['labels'])
    width = max(min_width, num_records * 0.2)  # 0.2 scaling factor to fit more records
    height = max(min_height, 6 + num_records * 0.1)  # Increase height based on the number of records

    # Create the plot with dynamic size
    fig, ax = plt.subplots(figsize=(width, height))

    # Use the "copper" colormap for the bars
    # Normalize the data values to map them to the colormap range
    norm = plt.Normalize(min(data['values']), max(data['values']))
    cmap = plt.get_cmap('copper')
    
    # Create bars with the colormap
    ax.bar(data['labels'], data['values'], color=cmap(norm(data['values'])))

    # Set labels and title
    ax.set_xlabel('Person')
    ax.set_ylabel('Quantity')
    ax.set_title('Quantity vs Person')

    # Rotate x-axis labels to avoid overlapping
    plt.xticks(rotation=90)

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Encode the image to base64 for embedding in HTML
    graph_data = base64.b64encode(buf.getvalue()).decode('utf-8')

    return data, graph_data
