di = {
    "sid": 3,
    "jack": 1,
    "ram": 5,
}

for a in di.items():
    print(a)

for key, value in di.items():
    print(key + " " + str(value))
    print()


# https://pythontips.com/2016/04/24/python-sorted-collections/


# Sort dict by key
def sort_dict_by_key(dictionary):
    sorted_di = sorted(dictionary.items(), key=lambda t: t[0], reverse=True)
    return sorted_di


# Sort dict by values
def sort_dict_by_values(dictionary):
    sorted_di = sorted(dictionary.items(), key=lambda t: t[1], reverse=True)
    return sorted_di


print(sort_dict_by_key(di))
print(sort_dict_by_values(di))
