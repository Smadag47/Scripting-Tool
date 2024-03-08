"""
Pentesting Tools

This program combines a port scanner and a web scraper, and allows
the user to selct the tool they want to use.

Author: Grant Adams
"""

import network_tool as nt
import web_scraper as ws


def heading(title, line_length):
    """Display a heading and automatically center the title

    Arguments:
        title (str): The title that will be displayed in header
        line_length (int): the desired length of the line
    """

    divider_lines = "*" * line_length
    padding = " " * ((line_length - len(title)) // 2)
    centered_title = padding + title + padding
    print(f"\n{divider_lines}\n{centered_title}\n{divider_lines}\n")


def main_menu():
    """Display the program main menu, and allow user to select a tool"""

    while True:

        heading("Welcome to the program", 60)
        print("1. Port Scanner")
        print("2. Web Scraper")
        print("3. Exit Program")
        user_choice = input("\nSelect your choice > ")

        match user_choice:
            case "1":
                heading("Port Scanner", 60)
                nt.Network_tool()
            case "2":
                heading("Web Scraper", 60)
                ws.Web_scrape()
            case "3":
                print("\nGOODBYE!!!\n")
                break
            case _:
                continue

    input("Press Enter to exit\n")


def main():
    """The main function of the program"""
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nGoodbye!!!\n")
        exit()


if __name__ == "__main__":
    main()
