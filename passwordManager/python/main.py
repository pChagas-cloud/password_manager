import cryptography

testpass = "myKey"
epass = ""
dpass = ""

def get_key_len(key):
    key_len = 0
    for i in key:
        key_len += 1
    return key_len

def get_key_data(key):
    data = []
    data.append(get_key_len(key))

    return data

def read_key():
    file = open('key', 'rb')
    key = file.readlines()
    file.close()
    key = key[0]
    return key;
   
print(get_key_data(testpass))
print(read_key())
