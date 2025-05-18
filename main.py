#!/home/aditya/network-monitoring-project/env310/bin/python

import nmap

output_file = "network-monitoring-project/data/hosts.txt"

print("Starting Nmap Scan...")
nm = nmap.PortScanner()

try:
    print("Scanning network: 192.168.1.0/24")
    nm.scan('192.168.1.0/24', arguments='-sn')
    print("Scan Completed.")

    # Extract active hosts
    hosts = nm.all_hosts()

    # Save to file
    with open(output_file, "w") as file:
        for host in hosts:
            file.write(f"{host}\n")

    print(f"Active hosts saved to {output_file}")

except Exception as e:
    print(f"Error during scan: {e}")
