from operator import attrgetter

class User:
    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + ": "  +str(self.user_id)

users = [
    User('Bucky', 43),
    User('Rane', 23),
    User('TEjas', 3),
    User('Bucasadkady', 45),
    User('asda', 98)
]

for user in users:
    print(user)

print("_____________")
for user in sorted(users, key =attrgetter('name')):
    print(user)

print("_______")
for user in sorted(users, key =attrgetter('user_id')):
    print(user)