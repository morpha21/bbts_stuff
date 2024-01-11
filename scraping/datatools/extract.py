def novelty(div):
	"""returns the last line of a given string"""
	start = div.rfind('\n')
	if start != -1:
		return div[start+1:]
	return ""
