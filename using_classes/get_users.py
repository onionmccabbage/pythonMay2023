from my_class_c import User
import requests

# here is a method to get a user
def getUser(n=1):
    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{n}')
    u = resp.json()
    return u

if __name__ == '__main__':
    l = getUser(1)
    leanne = User(l['name'], l['email'])
    print(leanne)
    # we can grab all the users and make instances
    users = []
    for u in range(1, 11):
        usr = getUser(u)
        usr_c = User(usr['name'], usr['email'])
        users.append(usr_c)

    for u in users:
        print(u)

    # we can see the value of our static property
    print(User.userCount)


