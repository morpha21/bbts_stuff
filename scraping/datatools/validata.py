from datetime import datetime

def validar_data(data, formato_data="%d/%m/%Y"):
	"""confere se uma string é um formato de data válido"""
	try:
		datetime.strptime(data, formato_data)
		return True
	except ValueError:
		return False
