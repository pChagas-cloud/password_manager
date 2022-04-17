from cryptography.fernet import Fernet

class encrypt:

    def __init__(self, random_key_file, password_key_file):
        file = open(random_key_file, 'rb')
        random_key = file.readlines()
        random_key = random_key[0]
        file.close()
        file = open(password_key_file, 'rb')
        password_key = file.readlines()
        password_key = password_key[0]
        file.close
        self.random_key = random_key
        self.password_key = password_key

    def test(self):
        print(self.random_key)
        print(self.password_key)

    def encrypt_text(self, plain_text):
        rkey = self.random_key
        pkey = self.password_key
        encoded_text = plain_text.encode()
        print("Do you want to encrypt using a password or random key ?")
        print("[1] - random key")
        print("[2] - password key")
        choice = input("Type your index: ")
        if choice == "1" or choice == "random key":
            print("Ok, just remember to copy the following key:")
            print(rkey)
            print("you will need it to decrypt your passwords")
            input("")
            f = Fernet(rkey)
        elif choice == "2" or choice == "password key":
            f = Fernet(pkey)
        encrypted_text = f.encrypt(encoded_text)
        print(encrypted_text)
        return encrypted_text

    def encrypt_password(self, plain_text):
        rkey = self.random_key
        pkey = self.password_key
        encoded_text = plain_text.encode()
        f = Fernet(rkey)
        encrypted_text = f.encrypt(encoded_text)
        return encrypted_text

    def encrypt_with_password(self, plain_text, key):
        encoded_text = plain_text.encode()
        f = Fernet(key)
        encrypted_text = f.encrypt(encoded_text)
        return encrypted_text

    def decrypt_with_password(self, encrypted_text, key):
        f = Fernet(key)
        dtxt = f.decrypt(encrypted_text)
        return dtxt

   
