# Scripting Tool

This tool provides functionalities for encryption and network scanning. Below are the steps to install and use the tool.

## Installation

To install and use this tool, follow these steps:

1. Clone the GitHub repository:
   ```
   git clone https://github.com/Smadag47/Scripting-Tool
   ```

2. Navigate to the project directory:
   ```
   cd Scripting-Tool
   ```

3. Install the required modules:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Main Menu

When the program is executed, it will display a main menu. Use the arrow keys on your keyboard to navigate through the menu options. You can choose the encryption tool, the network scan report tool, or exit the program using `CTRL + C`.

### Encryption Tool

If you select the encryption tool from the main menu, you'll encounter four options:

#### 1. Create Key

This option generates a key used for encrypting and decrypting files. Keys are automatically generated when encrypting or decrypting files.

#### 2. Encrypt File

Select this option to encrypt a file. You'll be presented with a list of files in the current directory that can be encrypted. Choose the file you want to encrypt, and a confirmation message will appear after encryption.

#### 3. Decrypt File

Choose this option to decrypt a file. You'll see a list of files available for decryption. Select the file you wish to decrypt, and a confirmation message will appear after decryption.

#### 4. Back

Use this option to return to the main menu from the encryption tool menu.

### Network Scanner

Selecting this option from the main menu prompts you to enter the subnet you want to scan, including CIDR notation. After entering the subnet, the program will execute the scan and inform you of its progress.

Once the scan is complete, the program returns to the main menu. The results of the scan are saved to CSV files, with one CSV file generated per scanned host.
