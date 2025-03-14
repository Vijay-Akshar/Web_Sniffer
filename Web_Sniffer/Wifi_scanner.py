'''
ARP - Address Resolution Protocol - Broadcasts a request to find out which devices are active on the network
Socket - Reverse DNS lookup
Requests - Making HTTP requests like GET or POST
Akshar Vijay, 3/5/2025
'''

from scapy.all import ARP, Ether, srp
import socket
import requests
import datetime

def get_host_name(ip): # Reverse DNS lookup to get the hostname for an IP
    try:
        return socket.gethostbyaddr(ip)[0]  # Returns the hostname if available
    except socket.herror:
        return "Host name not assigned"

def scan_network(ip_range):
    arp_request = ARP(pdst=ip_range)  # Creates an ARP request
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")  # Ethernet frame with broadcast MAC
    packet = ether_frame / arp_request 
    result = srp(packet, timeout=3, verbose=False)[0]  # Send and receive packets

    devices = []
    for sent, received in result:
        ip_address = received.psrc
        mac_address = received.hwsrc
        hostname = get_host_name(ip_address)  # Fetch the hostname

        devices.append({
            "IP": ip_address,
            "MAC": mac_address,
            "Hostname": hostname
        })

    return devices  

def log_devices(devices): #Logs every scan to 'devices.txt' for tracking
    with open("devices.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\nScan Timestamp: {timestamp}\n")
        file.write("-" * 80 + "\n")
        file.write(f"{'IP Address':<18}{'MAC Address':<20}{'Hostname'}\n")
        file.write("-" * 80 + "\n")

        for device in devices:
            file.write(f"{device['IP']:<18}{device['MAC']:<20}{device['Hostname']}\n")

        file.write("-" * 80 + "\n\n")

if __name__ == "__main__":
    network_range = "10.16.57.0/24"  # My network range (WiFi)
    devices = scan_network(network_range)
    # Print results in the same format as before
    print("\nConnected Devices:")
    print("-" * 80)
    print(f"{'IP Address':<18}{'MAC Address':<20}{'Hostname'}")
    print("-" * 80)

    for device in devices:
        print(f"{device['IP']:<18}{device['MAC']:<20}{device['Hostname']}")

    log_devices(devices)
    print("\nDevice scan results logged to 'devices.txt'.")

