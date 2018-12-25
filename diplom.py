# from urllib.parse import urlencode
import json
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
    #     'scope': 'friends',
    #     'v': '5.92'
    # }
    #
    # print(AUTH_URL + urlencode(auth_data))

    token = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
    try:
        user_id = input('Введите идентификатор (id) или короткое имя (screen_name) пользователя: ')
        assert user_id != '', 'user_id is empty'

        max_friends = input('Введите максимально допустимое число друзей в группе: ')
        assert max_friends.isnumeric(), 'Max friends count in group not is numeric'
        assert int(max_friends) >= 0, 'Max friends count in group is negative'

        user1 = UserVK(token, user_id)
        if user1.error == 0:
            get_groups_list = user1.get_groups()
            pprint(get_groups_list)
            friends = user1.get_friends()
            # groups_list = user1.get_unique_groups(get_groups_list, friends, int(max_friends))

            groups_list = user1.get_unique_groups_2(get_groups_list, friends, int(max_friends))

            with open('groups.json', 'w', encoding='utf-8') as result_file:
                json.dump(groups_list, result_file, ensure_ascii=False, indent=2)

    except AssertionError as e:
        print(e)
