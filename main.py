import cryptography
from generate_password_key import pgk
from generate_fernet_key import fgk
from encrypt import encrypt

testpass = "myKey"
epass = ""
dpass = ""

encpt = encrypt('random_key', 'password_generated_key')

class passmgr:

    def __init__(self, logins_file,passwords_file, tips_file):
        self.lfile = logins_file
        self.pfile = passwords_file
        self.tfile = tips_file

    def append_data(data, filename):
        f = open(filename, 'a')
        f.write(f"{data} \n")
        f.close()

    def encrypt_password(password):
        passHash = pgk.generate_hash()
        e_password = encpt.encrypt_with_password(password, passHash)
        return e_password
    
    def decrypt_password(password):
        passHash = pgk.generate_hash()
        d_password = encpt.decrypt_with_password(password, passHash)
        return d_password

    def add_data(self):
        login = input("Type the login: ")
        password = input("Type the password: ")
        tip = input("Where does this data belong: ")
        data = [login, password, tip]
        
        lfile = self.lfile
        pfile = self.pfile
        tfile = self.tfile
        passmgr.append_data(login, lfile)
        password = passmgr.encrypt_password(password)
        passmgr.append_data(password, pfile)
        passmgr.append_data(tip, tfile)

    def print_menu(self):
        greetings = "= This is my shitty password manager, it's usable at least ="
        print("="*len(greetings))
        print(greetings)
        print("="*len(greetings))
        passmgr.print_logins(self)

    def open_files(self):
        pfile = self.pfile
        lfile = self.lfile
        tfile = self.tfile
        passwords_file = open(pfile, 'rb')
        passwords = passwords_file.readlines()
        passwords_file.close()
        logins_file = open(lfile, 'r')
        logins = logins_file.readlines()
        logins_file.close()
        tips_file = open(tfile, 'r')
        tips = tips_file.readlines()
        tips_file.close()
        return [logins, passwords, tips]

    def print_logins(self):
        landp = passmgr.open_files(self)
        logins = landp[0]
        passwords = landp[1]
        tips = landp[2]

        for i in range(len(logins)):
            print(f"[{i}] - {tips[i].rstrip()} -> {logins[i].rstrip()} - {passwords[i].rstrip()}")
            #print(f"[{i}] - {tips[i].rstrip()} -> {logins[i].rstrip()}")

        index = input("Type the password index -> ")
        passmgr.request_password(self, passwords[int(index)].rstrip())

    def request_password(self, password):
        print(passmgr.decrypt_password(password))
    
    def test(self):
        x = input(">_ ")
        #print(x)
        ex = passmgr.encrypt_password(x)
        #print(ex)
        f = open('testfile', 'wb')
        f.write(ex)
        f.close()
        f = open('testfile', 'rb')
        ex_list = f.readlines()
        f.close()
        ex_read = ex_list[0]
        dx = passmgr.decrypt_password(ex_read)
        print(dx)

    def test2(self):
        landp = passmgr.open_files(self)
        passwords = landp[1]
        for i in passwords:
            print(i)
   

pmgr = passmgr("logins","passwords","tips")
#pmgr.add_data()
#pmgr.print_menu()
pmgr.test()
