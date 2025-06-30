if __name__ == "__main__":
    print("AcSecurity Console")
    # Simple menu logic here
    while True:
        print("\n1. Surveillance System Risk Assessment")
        print("2. Access Control Management")
        print("3. Network Security Monitoring")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            from acsecurity.core.surveillance import assess_risk, generate_risk_report, recommend_mitigation
            system_config = {
                'camera_quality': 'high',
                'coverage_area': 'wide'
            }
            risk_level = assess_risk(system_config)
            print(f"Risk Level: {risk_level}")
            print(generate_risk_report())
            print("Mitigation Strategies:")
            for strategy in recommend_mitigation():
                print(f"- {strategy}")
        
        elif choice == '2':
            from acsecurity.core.access_control import authenticate_user, authorize_user, log_access_attempt
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate_user(username, password):
                print("Authentication successful.")
                user_role = input("Enter your role: ")
                required_role = "admin"
                if authorize_user(user_role, required_role):
                    print("Access granted.")
                    log_access_attempt(username, "Resource", True)
                else:
                    print("Access denied.")
                    log_access_attempt(username, "Resource", False)
            else:
                print("Authentication failed.")
        
        elif choice == '3':
            try:
                from acsecurity.core.network_security import scan_ports, monitor_traffic, detect_intrusion
            except ModuleNotFoundError:
                print("Error: acsecurity.core.network_security module not found. Please check your project structure.")
                continue
            ip = input("Enter IP address to scan ports: ")
            open_ports = scan_ports(ip)
            print(f"Open ports on {ip}: {open_ports}")
            
            interface = input("Enter network interface to monitor traffic: ")
            print(f"Monitoring traffic on {interface}...")
            # Uncomment the next line to start monitoring (requires scapy)
            monitor_traffic(interface)
            
            detect_intrusion()
        
        elif choice == '4':
            print("Exiting AcSecurity Console.")
            break
        
        else:
            print("Invalid option. Please try again.")