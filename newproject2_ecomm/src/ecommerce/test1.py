# 1) Nested List
''' result = []


def single_list(nestedlist):
    for value in nestedlist:
        if isinstance(value, list):
            single_list(value)
        else:
            result.append(value)


nestedlist = [[1, 2], [3], [[[4, 5, 6]]]]
single_list(nestedlist)
print(result) '''

# ----------------------------------------------------
# 2) Nested Dictionary
result_list = []


def true_value(nesteddict):
    for key, val in nesteddict.items():
        # print("key is ", key, 'value is ', val)
        if isinstance(val, dict):
            # print("inside isinstance :", val)
            true_value(val)
        else:
            print(":")
        return result_list.append(key)
    # if val.values():
    #     print("one more inside :", val.values())
    # true_value(val)
    #     elif val.values() == True:
    #         print("true values are", val.keys)
    #     else:
    #         res = result_list.append(val)
    # return res


nested_dict = {
    'user': {'add': False, 'delete': True},
    'product': {'add': True, 'delete': False}
}

# def true_value(nesteddict):
#     for key, val in nesteddict.items():
#         print(key, val)
#         if val:
#             answer = '{}{}'.format(key,val)
#             q =result_list.append(answer)
#
#     return q
#
# nesteddict = {'add': False, 'delete': True,'formmatt':True}
# true_value(nesteddict)
# print(result_list)
temp_list = []


def parser(data, k=None):
    for key, value in data.items():
        if isinstance(value, dict):
            parser(value, key)
        elif value is True:
            parsed_key = '{}_{}'.format(k, key)
            temp_list.append(parsed_key)


# for key, value in nested_dict.items():
#     for key1, value1 in value.items():
#         if value1 is True:
#             parsed_key = '{}_{}'.format(key, key1)
#             temp_list.append(parsed_key)
# parser(data=nested_dict)
# print(temp_list)


search_dict = {
    'user1': {'address': ['banashankari', 'test'], 'number': 123456},
    'user2': {'address': ['marathalli', 'test'], 'number': 456787},
    'user3': {'address': ['mara', 'tera'], 'number': 456787},
    'user4': {'address': ['para', 'mara'], 'number': 456787}

}


# solution by nishant
# def search_params(data, param, value):
#     result_list2 = []
#     for k, v in data.items():
#         if data[k][param] is value:
#             result_list2.append(k)
#     return result_list2
# print(search_params(search_dict, 'number', 123456))

# vivek

def search_params(data, param, value):
    result_list3 = []
    for key, val in search_dict.items():
        # print("for:    ", data[key][param])
        for list_parse in data[key][param]:
            # print("for1:        ", list_parse)
            if list_parse == value:
                # print("list_parse:", list_parse, "value:", value)
                result_list3.append(key)
    return result_list3


print(search_params(search_dict, 'address', value='para'))
