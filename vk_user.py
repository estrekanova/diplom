import requests
import time


class UserVK:
    def __init__(self, token, user_id=''):
        self.user_id = user_id
        self.params = {
            'access_token': token,
            'v': '5.92'
        }

    def get_friends(self):
        response = requests.get('https://api.vk.com/method/friends.get', self.params)
        return response.json()['response']['items']

    def get_groups(self):
        params = self.params
        # params['user_id'] = str(self.user_id)
        params['filter'] = 'groups, publics, events'
        response = requests.get('https://api.vk.com/method/groups.get', self.params)
        return response.json()['response']['items']

    def get_group_members(self, group_id):
        time.sleep(0.3)
        params = self.params
        params['group_id'] = str(group_id)
        params['filter'] = 'friends'

        response = requests.get('https://api.vk.com/method/groups.getMembers', params)
        return response.json()['response']['count']

    def get_unique_groups(self, group_list):
        unique_list = list()
        for group in group_list:
            time.sleep(0.3)
            params = self.params
            params['group_id'] = str(group)
            params['filter'] = 'friends'

            response = requests.get('https://api.vk.com/method/groups.getMembers', params)
            if response.json()['response']['count']:
                unique_list.append(group)
        return unique_list
