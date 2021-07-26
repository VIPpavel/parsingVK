import requests
 ###162458672
 ### группа: opt2020
from tokenVK import token

#name_user = input("Введите название группы: ")
#url = f"https://api.vk.com/method/users.get?user_id={name_user}&fields=status,city,connections&access_token=7c14770d7c14770d7c14770d257c6cda8d77c147c14770d1cece0d3e314031ab161ba64&v=5.52"
#req = requests.get(url)
#print(req.text)


def main():
    name_group = input("Введите название группы: ")
    url1 = f"https://api.vk.com/method/groups.getMembers?group_id={name_group}&offset=999&access_token=7c14770d7c14770d7c14770d257c6cda8d77c147c14770d1cece0d3e314031ab161ba64&v=5.52"
    req = requests.get(url1)
    print(req.text)
    print(url1)
    mass = []
    mass = req.text
    a = '['
    for i in mass:
        if i == a:
            print(i)
    f = open('file.txt', 'wt')
    f.write(req.text)
    f.close()
main()