import requests


def get_json(source):
    result = requests.get(source)
    return result.json()


def print_result(dict):
    dict_len = dict['data'].__len__()
    i = 0
    while i < dict_len:
        print(dict['data'][i]['email'])
        i = i + 1


def main():
    print_result(get_json("https://reqres.in/api/users"))

main()