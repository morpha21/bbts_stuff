from datetime import datetime

def date(data, format="%d/%m/%Y"):
	"""checks if a given string conforms to a date format"""
	try:
		datetime.strptime(data, format)
		return True
	except ValueError:
		return False
