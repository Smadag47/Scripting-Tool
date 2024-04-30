import socket


class Web_scrape:
    """
    A class containing all the methods needed for a web scraper.

    Methods:
        host_discovery - Scan number 1.    
        port_scan - Scan number 2.
    """

    def __init__(self):
        """Constructor for the Web_scrape class"""

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
                    self.host_discovery()
                case "2":
                    self.port_scan()
                case "3":
                    self.generate_report()
                case "4":
                    self.scan4()
                case "5":
                    print("bye bye")
                    break
                case "6":
                    print("\n GOODBYE!!! \n")
                    exit()
                case _:
                    print("Invalid input")

    def host_discovery(self):
        print("Scan 1")

    def get_subnet_addresses(self):
        ip_prefix = "192.168.1."

        for suffix in range(1, 256):    
            print(f"{ip_prefix}{suffix}")

    def return_banner(self, ip_addresses, port):


        for address in ip_addresses:
            try:
                socket.setdefaulttimeout(2)
                s = socket.socket()
                s.connect((address, port))
                banner = s.recv(1024)

                return banner
            
            except Exception as e:
                print(f"Exception: {e}")
                
                return None

    def generate_report(self):
        print("Scan 3")

    def scan4(self):
        print("Scan 4")


def main():
    ip_address = Web_scrape.get_subnet_addresses()

    return_banner()


if __name__ == "__main__":
    main()

    