import requests
from config import TOKEN, SLEEP
import time
import math
from progress import progressBar
from datetime import datetime
from csv_write import write


def get_group_info(group_id):
    """Get group info"""
    fields = 'description,members_count'
    req = requests.get(
        f'https://api.vk.com/method/groups.getById?v=5.131&group_id={group_id}&fields={fields}&access_token={TOKEN}')
    
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
                
        time.sleep(int(SLEEP))
        
        # + progress bar
        progressBar(num, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
        
    return data

id_group = input('Enter group name/id: ')
work_status = True
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
    print('Check entered data and token\n')
    print('Error:')
    print(e)
    work_status = False

if work_status == True:
    # GET MEMBERS
    try:
        members_data = get_group_members(id_group, count)
        
        data = []
        for user in members_data:
            id_ = user['id']
            try:
                bdate = user['bdate']
                age = int((datetime.today() - datetime.strptime(bdate, '%d.%m.%Y')).days/365.2425)
            except:
                age = None
            
            try:
                fname = user['first_name']
            except:
                fname = None
            
            try:
                lname = user['last_name']
            except:
                lname = None
            
            try:
                phone = user['mobile_phone']
                if len(phone) == 0:
                    phone = None
            except:
                phone = None
            
            try:
                city = user['city']['title']
            except:
                city = None

            data.append([id_, fname, lname, phone, city, age])
            
        write(data, id_group)
        
        print(f'File "{id_group}" saved')
        
    except Exception as e:
        print('Error. Get members')
        print('Error:')
        print(e)