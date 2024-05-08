import requests 
import pprint


link = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/11|12|15|21|22|23|24|25|27|29|33|35|41|51|52"

requisicao = requests.get(link)
informacoes = requisicao.json()

nomesEstados = []

for estado in informacoes:
    nomesEstados.append(estado['nome']) 

#Imprimir estados
pprint.pprint(nomesEstados)

