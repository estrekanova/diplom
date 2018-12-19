from urllib.parse import urlencode
import requests
from vk_user import UserVK
from pprint import pprint

if __name__ == '__main__':
    # APP_ID = 6779997
    # AUTH_URL = 'https://oauth.vk.com/authorize?'
    #
    # auth_data = {
    #     'client_id': APP_ID,
    #     'display': 'page',
    #     'redirect_uri': 'https://oauth.vk.com/blank.html',
    #     'response_type': 'token',
    #     'scope': 'groups,friends',
    #     'v': '5.92'
    # }
    #
    # print(AUTH_URL + urlencode(auth_data))

    token = 'b936e4a44ef83b175af9757d03265d6060601248807c9798e9935249ae46687adbe6f63b1bb1454abd07b'
    user1 = UserVK(token)
    user_groups = user1.get_groups()
    pprint(user_groups)
    # # pprint(user1.get_group_members('34215577'))
    #
    for group in user_groups:
        pprint(user1.get_group_members(group))

    pprint(user1.get_unique_groups(user_groups))


    # params = {
    #     'access_token': token,
    #     'user_id': '17463688',
    #     'v': '5.92'
    # }
    # response = requests.get('https://api.vk.com/method/groups.get', params)
    # pprint(response.json())
    #
    params = {
            'access_token': token,
            # 'group_id': '144867281',  # '34215577',
            'filter': 'groups, publics, events',  # 'friends',
            # 'user_id': '171691064',
            'v': '5.92',
        }
    response = requests.get('https://api.vk.com/method/groups.get', params)
    pprint(response.json())
