import os
from cryptography.fernet import Fernet


class Encryption_tool:
    """ A class containing all the methods needed for a port scanner.

    Methods:
        scan1 - Scan number 1.    
        scan2 - Scan number 2.
    """

    def __init__(self):
        """Constructor for the Port_scan class"""

        # Display the menu for the encryption tool
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Return to main menu")
        print("4. Exit program\n")

        # Ask the user for a choice and run the selected option
        while True:
            user_choice = input("Select your choice > ")

            match user_choice:
                case "1":
                    file = str(input("Enter a file to encrypt: "))
                    self.encrypt_file(file)
                case "2":
                    self.decrypt_file()
                case "3":
                    break
                case "4":
                    print("\n GOODBYE!!! \n")
                    exit()
                case _:
                    print("Invalid input")


    def encrypt_file(self, file):
        # Generate an encryption key
        key_start = Fernet.generate_key()
    
        # Create a file to store the encryption key
        with open("key.txt", "wb") as key_file:
            key_file.write(key_start)
    
        # Read the encryption key from the file
        with open("key.txt", "rb") as key_file:
            key = key_file.read()

        # Open the file to be encrypted
        with open("plain_text.txt", "rb") as file:
            file_contents = file.read()

        # Encrypt the contents of the file
        cipher_text = Fernet(key).encrypt(file_contents)

        # Save the encrypted contents to a new file
        with open("encrypted_file.fernet", "wb") as encrypted_file:
            encrypted_file.write(cipher_text)

        print("COMPLETE")


    def decrypt_file(self):
        # Read the encryption key from the file
        with open("key.txt", "rb") as key_file:
            key = key_file.read()

        # Open the file to be decrypted
        with open("encrypted_file.fernet", "rb") as encrypted_file:
            file_contents = encrypted_file.read()

        # Decrypt the contents of the file
        decrypted = Fernet(key).decrypt(file_contents)

        # Save the encrypted contents to a new file
        with open("plain_text.txt", "wb") as plaintext_file:
            plaintext_file.write(decrypted)

        print("COMPLETE")


def main():
    Encryption_tool()


if __name__ == "__main__":
    main()


