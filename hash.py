import hashlib

#text="hello world"
#hash_object=hashlib.sha256(text.encode())
#hash_digest=hash_object.hexdigest()
#print("SHA HASH of",text,"is",hash_digest)

def hash_file(file_path):
    h  = hashlib.new("sha256")
    with open (file_path,"rb")as file:
        while True:
            chunk=file.read(1024)
            if chunk == b"":
                break
            h.update(chunk)
    return h.hexdigest()  

def verify_integrity(file1,file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    print("\nchecking integrity between",file1,"and",file2)
    if hash1 == hash2:
        return "File is intact. No modification have been made."
    return "File has been modified.Possibly unsafe"

if __name__=="__main__":
    print("SHA HASH of file is:",hash_file(r"C:\Cryptography\venv\sample_files\sample.txt"))
    print(verify_integrity(r"C:\Cryptography\venv\sample_files\WhatsApp Image 2026-01-20 at 19.12.25.jpeg",r"C:\Cryptography\venv\sample_files\WhatsApp Image 2026-01-20 at 19.06.31.jpeg"))
    print(verify_integrity(r"C:\Cryptography\venv\sample_files\WhatsApp Image 2026-01-20 at 19.06.19.jpeg",r"C:\Cryptography\venv\sample_files\WhatsApp Image 2026-01-20 at 19.06.31.jpeg"))
      
