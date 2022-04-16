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
        #print(key)
        file = open('password_generated_key', 'wb')
        file.write(key)
        file.close()
    
