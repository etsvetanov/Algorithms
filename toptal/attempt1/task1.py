# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


s = '''photo.jpg, Warsaw, 2013-09-05 14:08:15
john.png, London, 2015-06-20 15:13:22
myFriends.png, Warsaw, 2013-09-05 14:07:13
Eiffel.jpg, Paris, 2015-07-23 08:03:02
pisatower.jpg, Paris, 2015-07-22 23:59:59
BOB.jpg, London, 2015-08-05 00:02:03
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2013-09-06 15:40:22
a.png, Warsaw, 2016-02-13 13:33:50
b.jpg, Warsaw, 2016-01-02 15:12:22
c.jpg, Warsaw, 2016-01-02 14:34:30
d.jpg, Warsaw, 2016-01-02 15:15:01
e.png, Warsaw, 2016-01-02 09:49:09
f.png, Warsaw, 2016-01-02 10:55:32
g.jpg, Warsaw, 2016-02-29 22:13:11'''

from datetime import datetime
from collections import defaultdict

def solution(S: str) -> str:
    # write your code in Python 3.6
    f = '%Y-%m-%d %H:%M:%S'
    parsed_photos = []
    photo_by_key = {}

    for p in S.splitlines():
        name, city, date = p.split(',')
        photo_name, ext = name.split('.')
        data = {
            'photo_name': photo_name,
            'ext': ext,
            'city': city.strip(),
            'date': datetime.strptime(date.strip(), f),
            'n': None,
            'new_name': None
        }
        parsed_photos.append(data)
        photo_by_key[(city.strip(), date.strip())] = data
    #
    # for x in parsed_photos:
    #     print(x)

    photo_data_by_city = defaultdict(list)
    for p in parsed_photos:
        city = p['city']
        photo_data_by_city[city].append(p)

    for k, v in photo_data_by_city.items():
        # print(f'{k}: {v}')
        # for x in v:
        #     print(x)
        v.sort(key=lambda x: x['date'])

        max_digits = len(str(len(v)))

        for i, p in enumerate(v):
            n = i + 1
            p['n'] = str(n).zfill(max_digits)
            print(p['n'])
            p['new_name'] = f'{p["city"]}{p["n"]}.{p["ext"]}'


    res = []
    [photo_data_by_city.items()]


    # [[name, city.strip(), datetime.strptime(date.strip(), f)] for name, city, date in p.split(',') for p in S.splitlines()]

print(solution(s))



# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
# from datetime import datetime
#
# def solution(A, D):
#     # write your code in Python 3.6
#     f = '%Y-%m-%d'
#     parsed_dates = [datetime.strptime(d, f) for d in D]
#
#     transactions = zip(A, parsed_dates)
#
#     payment_amounts_by_month = [0] * 13 # ignore 0 idx
#     payments_by_month = [0] * 13
#
#     balance = 0
#
#     for amount, date in transactions:
#         balance += amount
#
#         if amount < 0:  # payment
#             month = date.month
#             payment_amounts_by_month[month] += abs(amount)  # just count the abs amount
#             payments_by_month[month] += 1
#
#     months_without_fee = len([t for t in zip(payment_amounts_by_month, payments_by_month) if t[0] >= 100 and t[1] >= 3])
#
#     fees = (12 - months_without_fee) * 5
#
#     balance -= fees
#
#     return balance
#
#
# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
# import re
#
#
# def solution(S):
#     # write your code in Python 3.6
#     max_words = 0
#
#     for sent in re.split('[\?\.\!]', S):
#         words = [w for w in sent.split() if w]
#         max_words = max(max_words, len(words))
#
#     return max_words