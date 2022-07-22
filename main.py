import requests
from config import TOKEN
import time
import math
from progress import progressBar


def get_group_info(group_id):
    """Get group info"""
    fields = 'description,members_count'
    req = requests.get(
        f'https://api.vk.com/method/groups.getById?v=5.131&group_id={group_id}&fields={fields}&access_token={TOKEN}')
    print(req.json())
    return req.json()['response'][0]


def get_group_members(group_id, count):
    """Get group members"""

    length = math.ceil(count / 400)
    data = []
    offset = 0
    num = 0
    
    # print progress bar
    progressBar(num, length, prefix = 'Progress:', suffix = 'Complete', length = 50)

    while offset <= count:
        fields = 'city,bdate,contacts'
        req = requests.get(
            f'https://api.vk.com/method/groups.getMembers?v=5.131&group_id={group_id}&offset={offset}&fields={fields}&access_token={TOKEN}')
        offset += 400
        num += 1
        for i in req.json()['response']['items']:
            if i not in data:
                data.append(i)
        time.sleep(5)
        
        # + progress bar
        progressBar(num, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
        
    return data


id_group = 'thai_island_submariner'

# GET BASIC INFO ABOUT GROUP
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
    
# GET MEMBERS
try:
    members_data = get_group_members(id_group, count)
    print(members_data)
    
except Exception as e:
    print('Error. Get members')
    print(e)