def scan_ports(ip):
    import socket

    open_ports = []
    for port in range(1, 1025):  # Scanning ports from 1 to 1024
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set a timeout for the connection attempt
            result = sock.connect_ex((ip, port))
            if result == 0:  # Port is open
                open_ports.append(port)
    return open_ports

def monitor_traffic(interface):
    from scapy.all import sniff

    def packet_callback(packet):
        print(packet.summary())

    # Sniffing packets on the specified network interface
    sniff(iface=interface, prn=packet_callback, store=0)
    
    
def detect_intrusion():
    import os

    # This function could be expanded to include more sophisticated intrusion detection logic
    suspicious_files = ['/etc/passwd', '/etc/shadow']
    for file in suspicious_files:
        if os.path.exists(file):
            print(f"Suspicious file detected: {file}")
        else:
            print(f"No suspicious file found: {file}")