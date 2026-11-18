import random
import string

def password_create(length):
    el_string = string.ascii_letters + string.digits + string.punctuation

    password_list = []
    for i in range(length):
        rand_el = random.choice(el_string)
        password_list.append(rand_el)

    password = "".join(password_list)

    return password

user_length = int(input("Enter password length: "))

print(password_create(user_length))