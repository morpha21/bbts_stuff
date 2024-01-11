import requests


def send(message):
	"""Sends a message to a telegram user through a telegram bot"""
	bot_token = ''
	chat_id = ''

	with open('.bot_token','r') as bot:
		bot_token = bot.read().strip()

	with open('.chat_id','r') as chat:
		chat_id = chat.read().strip()

	api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

	params = {
		'chat_id': chat_id,
		'text': message,
		}

	response = requests.post(api_url, json=params)

	if response.status_code == 200:
    		print('Message sent successfully!')
	else:
	    	print(f'Failed to send message. Status code: {response.status_code}, Response: {response.text}')
