import json

data = {
    'username': 'vivek',
    'password': 'test',
    'address': [{
        'zip_code': '560070',
        'area': 'banashankari',
        'near_by': ['marathalli', 'silk_board', 'tin_factory'],
        'country': {
            'state': 'karnataka',
            'city': 'bangalore',
            'code': 'IN',
            'near_by_country': ['China', 'Srilanka']
        }
    },
        {
            'zip_code': '560031',
            'area': 'bana',
            'near_by': ['mara', 'silky', 'tiny'],
            'country': {
                'state': 'karna',
                'city': 'banga',
                'code': 'PA',
                'near_by_country': ['China1', 'Srilanka1']
            }
        },
        {
            'zip_code': '560031',
            'area': 'banagiri nagar',
            'near_by': ['uttarahalli', 'CT bed', 'AGS lyt'],
            'country': {
                'state': 'karna',
                'city': 'banga',
                'code': 'PA',
                'near_by_country': ['China1', 'Srilanka1']
            }
        },
        {
            'zip_code': '560070',
            'area': 'banashankari stage III',
            'near_by': ['srinivas nagar', 'hanumanth nagar', 'srinagar'],
            'country': {
                'state': 'karna',
                'city': 'banga',
                'code': 'PA',
                'near_by_country': ['China1', 'Srilanka1']
            }
        }
    ]
}

# area = data.get('address').get('area')
# country_dict = data['address']['country']
# city = country_dict['city']
# state = country_dict['state']
# code = country_dict['code']
# print('{} {} {} {}'.format(area, city, state, code))
# {'near_by': ['mara', 'silky', 'tiny'], 'code': 'PA', 'state': 'karna', 'area': 'bana', 'city': 'banga', 'country': {'city': 'banga', 'code': 'PA', 'state': 'karna'}, 'zip_code': '560031'}

# output
address1 = {
    'username': 'vivek',
    'password': 'test',
    'zip_code': '560017',
    'area': 'banashankari',
    'near_by': ['marathalli', 'silk_board', 'tin_factory'],
    'state': 'karnataka',
    'city': 'bangalore',
    'code': 'IN',
    'near_by_country': ['China', 'Srilanka']
}
address2 = {}


# for key, value in data.items():
#     if key == 'username':
#         address2['username'] = value
#     if key == 'password':
#         address2['password'] = value
#     if key == 'address':
#         # for list_value in value:
#         for list_value in range(len(value)):
#             print("list value is :", list_value, "|||Value is ", value[list_value])
#             # for key1, value1 in list_value.items():
#             for key1, value1 in value[list_value].items():
#                 print("key1 is :", key1, "|||||| value1 is ", value1)
#                 if key1 == 'zip_code':
#                     address2['zipcode'] = value1
#                 elif key1 == 'area':
#                     address2['area'] = value1
#                 elif key1 == 'near_by':
#                     address2['near_by'] = value1
#                 # one more dict country here
#                 elif key1 == 'country':
#                     for key2, value2 in value1.items():
#                         # print("country dic values are :",key2,"||| value is :",value2)
#                         if key2 == 'state':
#                             address2['state'] = value2
#                         elif key2 == 'city':
#                             address2['city'] = value2
#                         elif key2 == 'code':
#                             address2['code'] = value2
#                         elif key2 == 'near_by_country':
#                             address2['near_by_country'] = value2
#     print("complete address is ", address2)
# print(json.dumps(address2,indent= 4))

# solution by nishant
# temp_address = {}
# temp_dict = {}
# for k, v in data.items():
#     if k == 'username' or k == 'password':
#         temp_dict[k] = v
#     elif k == 'address':
#         for i in range(len(v)):
#             key = 'address{}'.format(i+1)
#             temp_dict[key] = {}
#             for k3, v3 in v[i].items():
#                 if k3 == 'country':
#                     for k4, v4 in v3.items():
#                         temp_address[k4] = v4
#                     temp_dict[key].update(temp_address)
# print(temp_dict)


## Reverse creation of a nested dict
# test_dict = {}
# # test_dict.update({'username': 'vivek', 'password': '123456'})
# test_dict['username'] = 'vivek'
# test_dict['password'] = '123456'
# test_dict['address'] = [{'zip_code': '560004', 'area': 'BSK', 'near_by': ['marathalli', 'silk_board', 'tin_factory'],
#                          'country': {'state': 'karnataka',
#                                      'city': 'bangalore',
#                                      'code': 'IN',
#                                      'near_by_country': ['China', 'Srilanka']
#                                      }
#                          }
#                         ]
#
# print(test_dict)
def create_user_detail(username, password, city, state, near_by):
    return {
        'username': username,
        'password': password,
        'address': [{'state': state, 'city': city, 'near_by': near_by}]
    }


# print(create_user_detail('vivek', '123456', 'bang', 'kar', ['mara', 'no_mara']))

# ### searching for a string from a dict
# result = ''
# for ke, va in data.items():
#     if ke == 'address':
#         print(va)
#         for i in va:
#             print("i value is ", i)
#             # print("keys are " ,i.keys())
#             # print('banashankari' in va.values)
#             if 'banashankari' in i.values():
#                 print(i.get('va'))

temp_list = [4, 5, 6, 67, 68]

a = [x + 1 for x in temp_list if x % 2]
# print(a)
#
# print(list(map(lambda x: x + 1, temp_list)))

test_temp = {}


def parser_dict(data):
    for k, v in data.items():
        if isinstance(v, list):
            for val in v:
                if isinstance(val, dict):
                    parser_dict(val)
        elif isinstance(v, dict):
            parser_dict(v)
        else:
            test_temp[k] = v


parser_dict(data)
print(test_temp)
