"""
https://oauth.vk.com/authorize?client_id=8225378&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.131
"""

with open('settings.txt', 'r') as file:
    data = file.read().split('\n')
    TOKEN = data[0].split('=')[1].strip()
    SLEEP = data[1].split('=')[1].strip()
