import requests
import time


class UserVK:
    def __init__(self, token, user_id):
        self.access_token = token
        self.v = '5.92'
        self.user_id = user_id
        self.error = 0
        try:
            if not user_id.isnumeric():
                user = self.user_info()
                self.user_id =user['response'][0]['id']
            else:
                self.user_id = user_id
        except KeyError:
            self.error = user['error']['error_code']
            print(user['error']['error_msg'])

    def user_info(self):
        params = {
            'access_token': self.access_token,
            'v': self.v,
            'user_ids': self.user_id
        }
        try:
            print('.')
            time.sleep(0.4)
            response = requests.get('https://api.vk.com/method/users.get', params)
            return response.json()
        except ConnectionError as e:
            print(e)

    def get_friends(self):
        params = {
            'access_token': self.access_token,
            'v': self.v,
            'user_id': self.user_id
        }
        try:
            print('.')
            time.sleep(0.4)
            response = requests.get('https://api.vk.com/method/friends.get', params)
            return response.json()['response']['items']
        except ConnectionError as e:
            print(e)
            return []
        except KeyError:
            return []

    def get_groups(self):
        params = {
            'access_token': self.access_token,
            'v': self.v,
            'user_id': self.user_id,
            'extended': 1,
            'fields': 'members_count'
        }
        print('.')
        try:
            time.sleep(0.4)
            response = requests.get('https://api.vk.com/method/groups.get', params)
            return response.json()['response']['items']
        except ConnectionError:
            print('Connection error')
            return []
        except KeyError:
            return []

    def get_unique_groups(self, groups_list, friends, max_friends=0):
        unique_list = list()
        friends_set = set(friends)

        for group in groups_list[:1000]:
            time.sleep(0.4)

            offset = 0
            group_id = group['id']
            members_count = group['members_count']

            print(group_id, members_count)
            params = {
                'access_token': self.access_token,
                'v': self.v,
                'group_id': group_id,
                'sort': 'id_asc',
                'count': '1000'
            }

            friends_in_group = 0

            while offset < members_count and friends_in_group <= max_friends:
                params['offset'] = offset

                print('.')
                try:
                    time.sleep(0.4)
                    response = requests.get('https://api.vk.com/method/groups.getMembers', params)
                    offset += 1000
                    response_set = set(response.json()['response']['items'])
                    res = friends_set.intersection(response_set)
                    friends_in_group += len(res)
                except KeyError as e:
                    print(response.json()['error']['error_msg'])
                except ConnectionError as e:
                    print(e)

            if friends_in_group <= max_friends:
                write_group = {
                    'id': group['id'],
                    'name': group['name'],
                    'members_count': group['members_count']
                }
                unique_list.append(write_group)
        return unique_list
