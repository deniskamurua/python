import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


with open("thekey.key", "rb") as key:
    secret_key = key.read()

secret_phrase = "kissmyass"
user_phrase = input("Enter secret phrase to decrypt")

if user_phrase == secret_phrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        content_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as f:
            f.write(content_decrypted)


