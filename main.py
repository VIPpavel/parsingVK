import requests
 ###162458672
 ### группа: opt2020
from tokenVK import token

#name_user = input("Введите название группы: ")
#url = f"https://api.vk.com/method/users.get?user_id={name_user}&fields=status,city,connections&access_token=7c14770d7c14770d7c14770d257c6cda8d77c147c14770d1cece0d3e314031ab161ba64&v=5.52"
#req = requests.get(url)
#print(req.text)


def main():
    #name_group = input("Введите название группы: ")
    url1 = f"https://api.vk.com/method/groups.getMembers?group_id=opt2020&offset=1070&access_token=7c14770d7c14770d7c14770d257c6cda8d77c147c14770d1cece0d3e314031ab161ba64&v=5.52"
    req = requests.get(url1)
    print(req.text)
    print(url1)
    mass = req.text
    a = '['
    b = ']'
    c = mass.index(a)
    d = mass.index(b)
    mainId = mass[c+1:d]
    print(mainId)
    digits = []
    digits = mainId.split(',')
    print(digits)
    f = open('file.txt', 'wt', encoding='utf-8')
    for i in digits:
        url = f"https://api.vk.com/method/users.get?user_id={i}&fields=connections&access_token=7c14770d7c14770d7c14770d257c6cda8d77c147c14770d1cece0d3e314031ab161ba64&v=5.52"
        req = requests.get(url)
        f.write(req.text)
    f.close()
main()