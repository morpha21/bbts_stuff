import requests
from bs4 import BeautifulSoup
from datetime import datetime

from datatools.validata import validar_data
from datatools.extracao import novidade
from datatools.message import send


formato = "%d/%m/%Y"
ultima_novidade = ""
novelty_file = 'last_novelty'

with open(novelty_file, 'r') as f:
	ultima_novidade = f.read().strip()
	ultima_novidade = datetime.strptime(ultima_novidade, formato)


url = 'https://conhecimento.fgv.br/concursos/bbts23'
resp = requests.get(url)

mensagem = ""

if resp.status_code == 200:
	soup = BeautifulSoup(resp.text, 'html.parser')
else:
	mensagem = f'Falha ao obter dados de {url}'

div_class = "field__item"

divs = soup.find_all('div', {'class': div_class})


# pega as divs com data em seu conteudo
conteudo_divs = [
	div.text.strip()
	for div in divs
	if validar_data(div.text.strip()[:10], formato_data=formato)
	]



novidades = [
	( i[:10], novidade(i) )
	for i in conteudo_divs
	if datetime.strptime(i[:10], formato) >= ultima_novidade
	and len(novidade(i)) > 0
	]


if len(novidades) == 0:
	mensagem = "sem novidades..."
	send(mensagem)
	exit()

for i in novidades:
	mensagem = mensagem+i[0]+":\t"+i[1]+"\n\n"

send(mensagem)

hoje = datetime.now().strftime("%d/%m/%Y")

with open(novelty_file, 'w') as f:
	f.write(hoje)
