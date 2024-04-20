import subprocess
import importlib


def install_package():
    packages = ["cryptography", "curses", "inquirer", "pyfiglet"]

    x = input("would you like to install required modules? (Y/n)")

    if x == "y":
        for package in packages:
            try:
                importlib.import_module(package)
                print(f"{package} is already installed.")
            except ImportError:
                print(f"{package} is not installed. Installing...")
                subprocess.run(["sudo", "apt", "install", f"python3-{package}"])

    else:
        print("Program could not be ran")
        exit()


if __name__ == "__main__":
    install_package()

