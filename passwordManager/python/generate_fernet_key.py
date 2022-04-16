from cryptography.fernet import Fernet

key = Fernet.generate_key()

key_string = key.decode()

file = open('random_key', 'wb')
file.write(key)
file.close()

print(f"The key was {key}")

write_backup = input("Do you want to overwrite the backup key file ? [Y/n] ")

if write_backup == "yes" or write_backup == "y" or write_backup == "" or write_backup == "Y":
    file = open('random_key_backup', 'wb')
    file.write(key)
    file.close()
    print("wrote it !")
