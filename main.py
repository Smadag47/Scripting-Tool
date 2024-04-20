"""
Pentesting Tools

This program combines a port scanner and a web scraper, and allows
the user to selct the tool they want to use.

Author: Grant Adams
"""
# Try to import required modules and install them if they arent already
try:
    import inquirer
    from pyfiglet import Figlet
    from installer import install_package
    from encryption_tool import Encryption_tool
    # from web_scraper import Web_scrape
except ModuleNotFoundError:
    install_package()


def heading(title):
    """Display a heading using ASCII art

    Args:
        title (str): The title that will be displayed in header
    """
    f = Figlet(font='slant')
    print(f.renderText(title))


def main_menu():
    while True:
        heading("Welcome")

        # Display a menu to select a tool
        menu = inquirer.prompt([
            inquirer.List(
                'choice',
                message="Please select a tool",
                choices=[
                    "Encryption Tool", 
                    "Network Scan Report", 
                    "Exit"])
        ])
        user_choice = menu["choice"]

        # Run the tool based on user's choice
        match user_choice:
            case "Encryption Tool":
                encryption_menu()
            case "Network Scan Report":
                heading("Web Scraper")
                # Web_scrape()
            case "Exit":
                print("\nGOODBYE!!!\n")
                exit()
            case _:
                continue


def encryption_menu():
    encryption_tool = Encryption_tool()
    while True:

        heading("Encryption tool")

        encryption_tool_menu = inquirer.prompt([
            inquirer.List(
                'choice',
                message="Please select a function",
                choices=[
                    "Create Key",
                    "Encrypt File",
                    "Decrypt File", 
                    "Back"])
        ])
        user_choice = encryption_tool_menu["choice"]

        match user_choice:
            case "Create Key":
                encryption_tool.create_new_key()
            case "Encrypt File":
                encryption_tool.encrypt_file()
            case "Decrypt File":
                encryption_tool.decrypt_file()
            case "Back":
                main_menu()
            case _:
                exit()


def main():
    """The main function of the program"""
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nGoodbye!!!\n")
        exit()


if __name__ == "__main__":
    main()
