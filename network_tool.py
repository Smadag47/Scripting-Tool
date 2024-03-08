class Network_tool:
    """
    A class containing all the methods needed for a port scanner.

    Methods:
        scan1 - Scan number 1.    
        scan2 - Scan number 2.
    """

    def __init__(self):
        """Constructor for the Port_scan class"""

        print("1. Scan 1")
        print("2. Scan 2")
        print("3. Scan 3")
        print("4. Scan 4")

        print("5. Return to main menu")
        print("6. Exit program\n")

        while True:
            user_choice = input("Select your choice > ")

            match user_choice:
                case "1":
                    self.scan1()
                case "2":
                    self.scan2()
                case "3":
                    self.scan3()
                case "4":
                    self.scan4()
                case "5":
                    break
                case "6":
                    print("\n GOODBYE!!! \n")
                    exit()
                case _:
                    print("Invalid input")

    def scan1(self):
        print("Scan 1")

    def scan2(self):
        print("Scan 2")

    def scan3(self):
        print("Scan 3")

    def scan4(self):
        print("Scan 4")


def main():
    Network_tool()


if __name__ == "__main__":
    main()