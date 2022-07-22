import requests
from config import TOKEN



def get_group_info(group_id):
    """Get group info"""
    fields = 'description,members_count'
    req = requests.get(f'https://api.vk.com/method/groups.getById?v=5.131&group_id={group_id}&fields={fields}&access_token={TOKEN}')
    return req.json()['response'][0]

def get_group_members(group_id, count):
    """Get group members"""
    
    offset = 401
    fields = 'city,bdate,contacts'
    req = requests.get(f'https://api.vk.com/method/groups.getMembers?v=5.131&group_id={group_id}&offset={offset}&fields={fields}&access_token={TOKEN}')
    return req.json()

c = 0
for i in get_group_members('thai_island_submariner', '0')['response']['items']:
    print(i)
    c += 1

print(c)

id_group = 'thai_island_submariner'
try:
    info = get_group_info(id_group)
    count = info['members_count']

    print('ID:', info['id'])
    print('Name:', info['name'])
    print('Screen name:', info['screen_name'])
    print('Description:', info['description'])
    print('Members count:', info['members_count'])
except Exception as e:
    print('Error. Get group info')
    print(e)

