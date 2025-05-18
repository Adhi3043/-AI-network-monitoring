import nmap
import time
import json
import os
from datetime import datetime

REPORTS_DIR = "network-monitoring-project/reports/"
SCAN_INTERVAL = 60  # Scan interval in seconds

def save_scan_report(data, filename):
    """ Save scan report to a JSON file. """
    filepath = os.path.join(REPORTS_DIR, filename)
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Scan report saved to: {filepath}")

def load_previous_scan(filename):
    """ Load the previous scan data from a JSON file. """
    filepath = os.path.join(REPORTS_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            return json.load(file)
    return None

def scan_network():
    """ Scan the network and return scan data. """
    print("Starting Network Scan...")
    nm = nmap.PortScanner()
    target_range = '10.0.2.1-254'
    print(f"Scanning network: {target_range}")
    nm.scan(hosts=target_range, arguments='-p 1-1024 -sS')
    scan_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "target_range": target_range,
        "hosts": []
    }

    for host in nm.all_hosts():
        host_data = {
            "ip": host,
            "state": nm[host].state(),
            "protocols": {}
        }
        for proto in nm[host].all_protocols():
            protocol_data = []
            for port in nm[host][proto]:
                port_data = {
                    "port": port,
                    "state": nm[host][proto][port]["state"]
                }
                protocol_data.append(port_data)
            host_data["protocols"][proto] = protocol_data

        scan_data["hosts"].append(host_data)

    return scan_data

def compare_scans(previous_scan, current_scan):
    """ Compare scans and detect changes. """
    changes = []
    prev_hosts = {host["ip"]: host for host in previous_scan["hosts"]}
    curr_hosts = {host["ip"]: host for host in current_scan["hosts"]}

    # Check for new hosts and port changes
    for ip, curr_host in curr_hosts.items():
        prev_host = prev_hosts.get(ip)
        if not prev_host:
            changes.append(f"New host detected: {ip}")
        else:
            for proto, ports in curr_host["protocols"].items():
                for port_data in ports:
                    port = port_data["port"]
                    state = port_data["state"]
                    prev_ports = {p["port"]: p["state"] for p in prev_host["protocols"].get(proto, [])}
                    
                    # Check for new open ports
                    if port not in prev_ports and state == "open":
                        changes.append(f"New open port {port} detected on {ip}")
                    
                    # Check for closed ports
                    if port in prev_ports and state != prev_ports[port]:
                        changes.append(f"Port {port} on {ip} changed from {prev_ports[port]} to {state}")

    return changes

def main():
    previous_scan_file = "last_scan.json"
    while True:
        current_scan = scan_network()

        # Save the current scan
        save_scan_report(current_scan, "current_scan.json")

        # Load the previous scan
        previous_scan = load_previous_scan(previous_scan_file)

        # Compare scans and log changes
        if previous_scan:
            changes = compare_scans(previous_scan, current_scan)
            if changes:
                print("\nALERT: Network changes detected!")
                for change in changes:
                    print(f" - {change}")
        
        # Update the previous scan file
        save_scan_report(current_scan, previous_scan_file)

        # Wait for the next scan interval
        print(f"\nWaiting for the next scan in {SCAN_INTERVAL} seconds...\n")
        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    main()

