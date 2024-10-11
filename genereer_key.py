from cryptography.fernet import Fernet
import sys

def genereer_sleutel():
    sleutel = Fernet.generate_key()  # Genereer een nieuwe sleutel
    with open("secret.key", "wb") as key_file:
        key_file.write(sleutel)  # Sla de sleutel op in 'secret.key'
    print("Nieuwe sleutel gegenereerd en opgeslagen in 'secret.key'.")

if __name__ == "__main__":
    genereer_sleutel()