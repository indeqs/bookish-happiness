#!/usr/bin/env python3

import hashlib, os

def hash_digest(secret_key, data):
    m = hashlib.md5()
    m.update(secret_key.encode())
    m.update(data.encode())
    return m.hexdigest()

secret_key = os.environ["KEY"]  # set environment variable KEY


print("\n")
print("\t\t\t*********** WELCOME FRIEND ***********")
print("\t\t\t*********** THERE IS ONLY 1 HINT HERE ***********")
print("\t\t\t*********** EXTEND IT...EXTEND IT....MAY THE gods BE WITH YOU!!! ***********")
print("\n")
print("\t\t\t*********** LENGTH OF THE KEY IS SOMEWHERE BETWEEN 10-15 BY THE WAY ***********")  # change prompt based on on length of secret_key
print("\n")
print("\n")

user_input = str(input("Enter data you want to hash and we'll hash it for you using our secure algorithm with a very secret key: "))

user_supplied_hash = input(f"Enter hash digest for your input '{user_input}': ")
print("\n")
user_input = user_input.strip().lower()
message = hash_digest(secret_key, user_input)
print(f"\t\t\t*********** Our secure hash for your input, '{user_input}' was {message} ***********")

if user_supplied_hash == message:
    os.system("cat ./flag.txt")
else:
    print("How stupid can you be bro!")
    print(f"Your input was '{user_input}' and the hash you gave us was: '{user_supplied_hash}'")
    print("\r\n")
