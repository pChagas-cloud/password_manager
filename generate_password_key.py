import os 
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class pgk:
    
    def generate_key():

        print("tip: remember your fucking password")
        password_provided = input("type your password: ")
        password = password_provided.encode() #convert to bytes

        salt = b'\xcc#!;\xce\xdf]\xcd\x8c\\A#\xaf\xfb\x8e\xdf'

        kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
                )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        save = input("Do you want to save your password key ? [Y/n] ")
            
        if save.lower() == "y" or save.lower() == "yes" or save == "":
            filename = input("Name the file: ")
            file = open(filename, 'wb')
            file.write(key)
            file.close()
            print(f"The key {key} was saved")
            return key;
        else:
            return key;
    
    def generate_hash():

        print("tip: remember your fucking password")
        password_provided = input("type your main password: ")
        password = password_provided.encode() #convert to bytes

        salt = b'\xcc#!;\xce\xdf]\xcd\x8c\\A#\xaf\xfb\x8e\xdf'

        kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
                )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
