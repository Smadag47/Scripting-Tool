"""
Pentesting Tools

This program combines a port scanner and a web scraper, and allows
the user to selct the tool they want to use.

Author: Grant Adams
"""

# Try to import required modules
try:
    import inquirer
    from pyfiglet import Figlet
    from encryption_tool import Encryption_tool
    from network_scan import Network_Scanner
except ModuleNotFoundError:
    print("Please install the required modules, and try again")
    exit()


def heading(title):
    """Display a heading using ASCII art

    Args:
        title (str): The title that will be displayed in header
    """
    f = Figlet(font="slant")
    print(f.renderText(title))


def display_menu(*options):
    """Displays a menu with the given options and returns the user's choice.

    Args:
        *options: Variable number of options to be displayed in the menu.

    Returns:
        The user's choice as a string.
    """
    menu = inquirer.prompt(
        [inquirer.List("choice", message="Please select a tool",
                       choices=options)]
    )

    # Exit the program gracefully if no option is selected
    if menu is None:
        print("Goodbye!")
        exit()

    user_choice = menu["choice"]

    return user_choice


def main_menu():
    """ Displays the main menu and allows the user to select a tool."""
    while True:
        heading("Welcome")

        # Display a menu to select a tool
        user_choice = display_menu(
            "Encryption Tool",
            "Network Scan Report",
            "Exit"
        )

        # Run the tool based on user's choice
        match user_choice:
            case "Encryption Tool":
                encryption_menu()
            case "Network Scan Report":
                network_scan_menu()
            case "Exit":
                print("\nGOODBYE!!!\n")
                exit()
            case _:
                continue


def encryption_menu():
    """Displays the encryption tool menu and performs the selected action."""
    encryption_tool = Encryption_tool()
    while True:
        heading("Encryption tool")

        # Display a menu to select an option
        user_choice = display_menu(
            "Create Key",
            "Encrypt File",
            "Decrypt File",
            "Back")

        # Carry out the chosen function
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


def network_scan_menu():
    """Displays the network scan menu and performs the selected action."""
    scanner = Network_Scanner()
    heading("Network Scanner")
    subnet_id = input("Enter a subnet to scan: ")
    hosts = scanner.host_discovery(subnet_id)
    scan_results = scanner.service_scan(hosts)
    scanner.generate_report(scan_results)


def main():
    """The main function of the program"""
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nGoodbye!!!\n")
        exit()


if __name__ == "__main__":
    main()
