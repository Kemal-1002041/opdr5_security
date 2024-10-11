from cryptography.fernet import Fernet
import sys

def laad_key():
    try: 
        return open ("secret.key", "rb").read()
    except FileNotFoundError:
        print("Sleutel bestand niet gevonden, er word nieuwe sleutel gemaakt")
        sys.exit()
        return laad_key()

def encrypt_bericht():
    key = laad_key()
    f = Fernet(key)
    bericht = input("Voer het bericht in die je wilt versleutelen: ")
    encrypt_bericht = f.encrypt(bericht.encode())
    print(f"Versleuteld bericht: {encrypt_bericht.decode()}")
    main_menu()

def decrypt_bericht():
    sleutel = laad_key()
    f = Fernet(sleutel)
    encrypted_message = input("Voer het versleutelde bericht in om te ontsleutelen: ")
    try:
        decrypted_message = f.decrypt(encrypted_message.encode())
        print(f"Ontsleuteld bericht: {decrypted_message.decode()}")
    except Exception as e:
        print(f"Fout bij het ontsleutelen van het bericht: {e}")
    main_menu()

def main_menu():
    print("1. Versleutelen")
    print("2. Ontsleutelen")
    print("3. Exit")
    keuze = input("Wat wil je doen? ")
    if keuze == "1":
        encrypt_bericht()
    elif keuze == "2":
        decrypt_bericht()
    elif keuze == "3":
        sys.exit()
    else:
        print("Ongeldige keuze")
        main_menu()

if __name__ == "__main__":
    main_menu()