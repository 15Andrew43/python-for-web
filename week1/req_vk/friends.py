from filecmp import cmp

import requests
import datetime

ACCESS_TOKEN = '04444ea604444ea604444ea631043039eb0044404444ea65bc8669f9fe3192fc5da3d58'
V = 5.124
current_year = datetime.datetime.today().year
# https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN&v=V


def calc_age(uid):
    get_users = 'users.get'
    PARAMETERS = f'user_ids={uid}'
    uid = requests.get(f'https://api.vk.com/method/{get_users}?{PARAMETERS}&access_token={ACCESS_TOKEN}&v={V}').json()['response'][0]['id']

    get_friends = 'friends.get'
    PARAMETERS = f'user_id={uid}&fields=bdate'
    dict = requests.get(f'https://api.vk.com/method/{get_friends}?{PARAMETERS}&access_token={ACCESS_TOKEN}&v={V}')

    dict = dict.json()
    dict = dict['response']['items']
    counted_ages = {}

    for info in dict:
        # print(info)
        b_date = info.get('bdate', '-1')
        if b_date == '-1':
            continue
        b_year = int(b_date.split('.')[-1])
        if b_year < 1900:
            continue

        age = current_year - b_year

        counted_ages.setdefault(age, 0)
        counted_ages[age] += 1
    def Cmp(x, y):
        if x[1] > y[1]:
            return 1
        elif x[1] < y[1]:
            return -1
        if x[0] < y[0]:
            return 1
        elif x[0] > y[0]:
            return -1
        return 0

    counted_ages = list(counted_ages.items())
    counted_ages.sort(key=lambda x: (1000-x[1], x[0]))
    return counted_ages



if __name__ == '__main__':
    res = calc_age('382803844')
    print(res)
