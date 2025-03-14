# WebSniffer - Network Device and Port Scanner

A Python-based network reconnaissance tool that scans devices on a local network and identifies open ports on a target IP. It helps security professionals and network administrators assess vulnerabilities by identifying connected devices and their open ports.

### Features
- Network Scanning: Uses ARP requests to discover active devices.
- Port Scanning: Identifies open ports on specified IPs.
- Reverse DNS Lookup: Retrieves hostnames for identified IP addresses.
- Scan Logging: Saves discovered devices in a structured log file.

---

## How It Works
### 1. WiFi Scanner (`Wifi_scanner.py`)
The WiFi scanner discovers active devices on the network by sending ARP requests. It:
- Sends broadcast requests to all devices in the subnet.
- Collects responses containing IP, MAC address, and hostname.
- Saves the results to `devices.txt`.

### 2. Port Scanner (`Port_scanner.py`)
The port scanner checks for common open ports on a given IP. It:
- Scans ports 22, 23, 25, 53, 80, 135, 139, 443, 445, 3306, 3389.
- Uses socket timeout to avoid long waits.
- Returns a list of open ports or a message if no ports are found.

---

## Installation & Setup
### 1. Install Required Dependencies
Ensure Python is installed. Install required libraries:
```sh
pip install scapy requests
```

### 2. Run the Network Scanner
Scan for devices on the network:
```sh
python Wifi_scanner.py
```
- Expected Output:
```
Connected Devices:
------------------------------------------------------------
IP Address        MAC Address         Hostname
------------------------------------------------------------
10.159.243.35     62:63:95:76:9e:9d   iphone.dhcp.asu.edu
10.159.243.63     14:ac:60:dc:38:a7   Akshar.dhcp.asu.edu
------------------------------------------------------------
Device scan results logged to 'devices.txt'.
```

### 3. Run the Port Scanner
To check open ports on a device:
```sh
python Port_scanner.py
```
- Expected Output:
```
Enter an IP address to scan (or type 'n' or '0' to exit): 10.159.243.63

Open ports on 10.159.243.63: [22, 80, 443]
```

---

## Getting Started
### 1. Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required dependencies (`scapy`, `requests`)

### 2. Clone the Repository
```sh
git clone <repo-link>
cd WebSniffer
```

### 3. Run the Scanners
#### WiFi Scanner
```sh
python Wifi_scanner.py
```
#### Port Scanner
```sh
python Port_scanner.py
```

---

## Contributing
Pull requests and suggestions are welcome to improve functionality and efficiency.

---

## License
This project is open-source and available under the MIT License.

(For research purposes only)