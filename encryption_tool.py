import os
from cryptography.fernet import Fernet


class Encryption_tool:
    """ A class containing all the methods needed for a port scanner.

    Methods:
        __init__ -   

        create_new_key - 

        read_key
    """

    def __init__(self):
        """Constructor for the Port_scan class"""


        # Display the menu for the encryption tool
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Generate a new key")
        print("4. Return to main menu")
        print("0. Exit program\n")
        
        # Get the key
        key = self.read_key()

        # Ask the user for a choice and run the selected option
        while True:
            user_choice = input("Select your choice > ")

            match user_choice:
                case "1":
                    file = str(input("Enter a file to encrypt: "))
                    self.encrypt_file(file, key)

                case "2":
                    file = str(input("Enter a file to decrypt: "))
                    try:
                        self.decrypt_file(file, key)
                    except:
                        print("Invalid Key")

                case "3":
                    self.create_new_key()

                case "4":
                    break

                case "0":
                    print("\n GOODBYE!!! \n")
                    exit()

                case _:
                    print("Invalid input")

    def create_new_key(self):
        '''  '''
        # Check if the file already exists
        if os.path.exists("key.txt"):
            print("key already exists")
        else:
            # Generate an encryption key
            key_start = Fernet.generate_key()

            # Create a file to store the encryption key
            with open("key.txt", "wb") as key_file:
                key_file.write(key_start)

    def read_key(self):
        '''   '''
        # Check if a key file already exists
        if not os.path.exists("key.txt"):
            print("No key found, generating new key")
            self.create_new_key()

        # Read the encryption key from the file
        with open("key.txt", "rb") as key_file:
            key = key_file.read()

        return key

    def encrypt_file(self, file, key):
        '''   '''
        # Try to open the file to be encrypted
        try:
            with open(file, "rb") as file:
                file_contents = file.read()

            # Encrypt the contents of the file
            cipher_text = Fernet(key).encrypt(file_contents)

            # Save the encrypted contents to a new file
            with open(f"encrypted-{file.name}", "wb") as encrypted_file:
                encrypted_file.write(cipher_text)

            print(f"{file.name} has been encrypted")

        except FileNotFoundError:
            print("File could not be found")

    def decrypt_file(self, file, key):
        '''   '''
        try:
            # Open the file to be decrypted
            with open(file, "rb") as encrypted_file:
                file_contents = encrypted_file.read()

            # Decrypt the contents of the file
            decrypted = Fernet(key).decrypt(file_contents)

            # Remove the 'encrypted' prefix
            file_name = file[10:]

            # Save the encrypted contents to a new file
            with open(f"decrypted-{file_name}", "wb") as plaintext_file:
                plaintext_file.write(decrypted)

            print(f"{file_name} has been decrypted")

        except FileNotFoundError:
            print("File could not be found")


def main():
    '''   '''
    Encryption_tool()


if __name__ == "__main__":
    main()