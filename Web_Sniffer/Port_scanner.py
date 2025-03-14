import socket

def scan_ports(ip):
    """Scan common ports to determine open services on a device."""
    common_ports = [22, 23, 25, 53, 80, 135, 139, 443, 445, 3306, 3389]  # List of common ports
    open_ports = []

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second to avoid long wait times
        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            open_ports.append(port)

    return open_ports if open_ports else "No open ports found"

# Main loop to keep asking for IP addresses
while True:
    ip_address = input("\nEnter an IP address to scan (or type 'n' or '0' to exit): ").strip()

    if ip_address.lower() == "n" or ip_address == "0":
        print("Exiting program.")
        break

    try:
        open_ports = scan_ports(ip_address)
        print(f"\nOpen ports on {ip_address}: {open_ports}")
    except Exception as e:
        print(f"Error scanning {ip_address}: {e}")
