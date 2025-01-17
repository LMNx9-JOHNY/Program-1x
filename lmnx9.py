
import os
try:import pycryptodome
except ImportError:
    os.system("pip install pycryptodome")
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os,sys

def decrypt_and_run(input_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    exec(plaintext.decode('utf-8'))
    
try:
    key_hex = os.getenv("ENCRYPTION_KEY")
    if not key_hex:
        print("\n </> LMNx9 ERROR : Unauthorized Detected.")
        sys.exit()
    key = bytes.fromhex(key_hex)
    encrypted_file = "run.xml"
    decrypt_and_run(encrypted_file, key)
except:
    print("\n </> LMNx9 ERROR : Unauthorized Detected.")
    sys.exit()
