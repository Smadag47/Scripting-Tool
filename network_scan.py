import nmap
import csv


class Network_Scanner:
    """A class for performing network scanning operations.

    Attributes:
        nm (nmap.PortScanner): An instance of the nmap PortScanner class.

    Methods:
        host_discovery(subnet): Perform a host discovery by carrying out a ping scan on the given subnet.
        service_scan(hosts): Perform a service version scan on a list of hosts.
        generate_report(results): Generate a CSV report for the network scan results.
    """

    # Initialise the nmap PortScanner class
    nm = nmap.PortScanner()

    def host_discovery(self, subnet):
        """Perform a host discovery by carrying out a ping scan on the given subnet.

        Args:
            subnet (str): The subnet to scan.

        Returns:
            list: A list of active hosts on the network.
        """
        # Carry out a ping scan on the given subnet and save to a list
        self.nm.scan(hosts=subnet, arguments="-sn")
        active_hosts = self.nm.all_hosts()

        # Return list of active hosts on the network
        return active_hosts

    def service_scan(self, hosts):
        """Perform a service version scan on a list of hosts.

        Args:
            hosts (list): A list of hosts to scan.

        Returns:
            dict: A dictionary containing the scan results for each host.
        """
        scan_results = {}

        # Iterate through all hosts and do a service version scan
        for host in hosts:
            self.nm.scan(hosts=host, arguments="-sV")

            # Store the scan results in a dictionary
            scan_results[host] = self.nm[host]

        # Return the dictionary of the scan results
        return scan_results

    def generate_report(self, results):
        """Generate a CSV report for the network scan results.

        Args:
            results (dict): A dictionary containing the scan results for each host.
        """
        # Iterate through all scanned hosts
        for host, host_info in results.items():

            # Check if there is TCP port information to iterate through
            if "tcp" in host_info:
                tcp_ports = host_info["tcp"]

                # Create a CSV file for each host scanned
                file_name = f"{host}_scan_results.csv"
                with open(file_name, "w", newline="") as csv_file:
                    headers = ["Port", "Service", "Product", "Version"]
                    writer = csv.DictWriter(csv_file, fieldnames=headers)
                    writer.writeheader()

                    # Iterate through all open ports
                    for port, port_info in tcp_ports.items():

                        # Get scan results
                        port_number = port
                        service = port_info.get("name", "Unknown")
                        product = port_info.get("product", "Unknown")
                        version = port_info.get("version", "Unknown")

                        # Write results to csv file
                        writer.writerow(
                            {
                                "Port": port_number,
                                "Service": service,
                                "Product": product,
                                "Version": version,
                            }
                        )
