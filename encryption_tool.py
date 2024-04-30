# Try to import required modules and install them if they arent already
try:
    import os
    from installer import install_package
    from cryptography.fernet import Fernet
    import inquirer
except ModuleNotFoundError as e:
    install_package()


class Encryption_tool:
    """ A class containing all the methods needed for an encryption tool.

    Methods:
        __init__ - Initialises the encryption class and read the key

        select_file - Allows the user to select a file from a list

        create_new_key - Creates a new key if one doesn't already exist

        read_key - reads the encryption key

        encrypt_file - Encrypts the selected file using the encryption key

        decrypt_file - Decrypts the selected file using the encryption key

    """

    def __init__(self):
        """Initialises the encryption class and read the key"""
        # Get the key
        self.key = self.read_key()

    def select_file(self):
        '''Allows the user to select a file from a list'''
        # Get a list of files and directories in the current directory
        file_list = os.listdir()

        # Filter out directories and return only text documents except the
        # key
        files = [
            file for file in file_list
            if os.path.isfile(file)
            and not file.endswith(".py")
            and file != "key.txt"
        ]

        # Display a menu to select a file
        menu = inquirer.prompt([
            inquirer.List(
                'choice',
                message="Please select a file",
                choices=files)
        ])
        user_choice = menu["choice"]

        return user_choice

    def create_new_key(self):
        '''Creates a new key if one doesn't already exist'''
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
        '''Reads the encryption key'''
        # Check if a key file already exists
        if not os.path.exists("key.txt"):
            print("No key found, generating new key")
            self.create_new_key()

        # Read the encryption key from the file
        with open("key.txt", "rb") as key_file:
            key = key_file.read()

        return key

    def encrypt_file(self):
        '''Encrypts the selected file using the encryption key'''
        file = self.select_file()

        # Try to open the file to be encrypted
        try:
            with open(file, "rb") as file:
                file_contents = file.read()

            # Encrypt the contents of the file
            cipher_text = Fernet(self.key).encrypt(file_contents)

            # Save the encrypted contents to a new file
            with open(f"encrypted-{file.name}", "wb") as encrypted_file:
                encrypted_file.write(cipher_text)

            print(f"{file.name} has been encrypted")

        except FileNotFoundError:
            print("File could not be found")

    def decrypt_file(self):
        '''Decrypts the selected file using the encryption key'''
        file = self.select_file()

        try:
            # Open the file to be decrypted
            with open(file, "rb") as encrypted_file:
                file_contents = encrypted_file.read()

            # Decrypt the contents of the file
            decrypted = Fernet(self.key).decrypt(file_contents)

            # Remove the 'encrypted' prefix
            file_name = file[10:]

            # Save the encrypted contents to a new file
            with open(f"decrypted-{file_name}", "wb") as plaintext_file:
                plaintext_file.write(decrypted)

            print(f"{file_name} has been decrypted")

        except FileNotFoundError:
            print("File could not be found")
