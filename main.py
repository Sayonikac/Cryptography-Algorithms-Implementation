from modules.hash import hash_file ,verify_integrity
from modules.encryption import aes_ed, rsa_ed
from modules.password import check_strength,hash_pw,verify_password

def menu():
    print("\nselect operation:")
    print("1.Hash File")
    print("2.Check file integrity")
    print("3.AES Encrypt/Decrypt")
    print("4.RSA Encrypt/Decrypt")
    print("5.Password Manager")
    print("0 Exit")

print("""
============================================================
SECURITY PROTOCOLS INITIALIZED - Cryptography v1.0
============================================================

Welcome, Operative. Your objectives for this session:
- Implement SHA-256 Hashing for data integrity
- Execute AES & RSA encryption for secure communication
- Validate authentication via secure password hashing

All encryption modules are LOADED. 
System status: SECURE.

Prepare to begin decryption...
============================================================
""")

while True:
    menu()
    choice= input("Enter choice(0.5):")
    if choice == "0":
        break
    elif choice =="1":
     file_path=input("Enter file path:")
     print("\nSHA HASH of file is:",hash_file(file_path))
    elif choice =="2":
       file_path1=input("Enter file path 1:")
       file_path2=input("Enter file path 2:")
       print(verify_integrity(file_path1,file_path2))
    elif choice =="3":
       message=input("Enter message:")
       key ,ciphertext ,plaintext  = aes_ed(message)
       print("AES Key:",key)
       print("AES ciphertext:",ciphertext)
       print("AES plaintext:",plaintext)
    elif choice =="4":
       message=input("Enter message:")
       ciphertext ,plaintext=rsa_ed(message)
       print("RSA message encrypted with a public key:",ciphertext)
       print("RSA message decrypted with a private key:",plaintext)
    elif choice =="5": 
        while True:
         password1 = input("Enter a password to check strngth:")
         print(check_strength(password1))
         if check_strength(password1).startswith("week"):
             print("please choose a stronger password")
         else:
             break
        hashed_password =hash_pw(password1)
        print("hashed password:",hashed_password)
        attempt = input("Re-enter the password to verify:")
        print(verify_password(attempt,hashed_password)) 
    else:
       print("Invalid choice")
print("Operative you are exiting your cryptography tool")       
        
