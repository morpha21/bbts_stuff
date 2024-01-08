def novidade(div):
	"""retorna a última linha de texto de uma string"""
	inicio = div.rfind('\n')
	if inicio != -1:
		return div[inicio+1:]
	return ""
