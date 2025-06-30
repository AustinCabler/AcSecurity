# This is a simple console application for AcSecurity that allows users to interact with core modules.
# It includes options for surveillance risk assessment, access control management, and network security monitoring.

## Use rich for better console output
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
console = Console()
import os
import sys
# Ensure the core modules are in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))
# Ensure the utils modules are in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
# Importing core modules
try:
    from acsecurity.core.surveillance import assess_risk, generate_risk_report, recommend_mitigation
    from acsecurity.core.access_control import authenticate_user, authorize_user, log_access_attempt
    from acsecurity.core.network_security import scan_ports, monitor_traffic, detect_intrusion
except ImportError as e:
    print(f"Error importing core modules: {e}")
    sys.exit(1)
# Importing utils modules
try:
    from acsecurity.utils.encryption import generate_key, load_key, encrypt_message, decrypt_message, encrypt_file, decrypt_file
except ImportError as e:
    print(f"Error importing utils modules: {e}")
    sys.exit(1)
# Main entry point for the console application
# This will provide a simple text-based interface for users to interact with the AcSecurity functionalities.
if __name__ == "__main__":
    console.print(Panel.fit("[bold blue]AcSecurity Console[/bold blue]", subtitle="Your Trusted Partner in Total Security"))
    while True:
        console.print("\n[bold]Main Menu[/bold]", style="cyan")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", style="dim")
        table.add_column("Description")
        table.add_row("1", "Surveillance System Risk Assessment")
        table.add_row("2", "Access Control Management")
        table.add_row("3", "Network Security Monitoring")
        table.add_row("4", "Exit")
        console.print(table)

        choice = Prompt.ask("[bold yellow]Select an option[/bold yellow]", choices=["1", "2", "3", "4"])

        if choice == '1':
            system_config = {
                'camera_quality': 'high',
                'coverage_area': 'wide'
            }
            risk_level = assess_risk(system_config)
            console.print(f"[bold green]Risk Level:[/bold green] {risk_level}")
            console.print(f"[bold blue]{generate_risk_report()}[/bold blue]")
            console.print("[bold magenta]Mitigation Strategies:[/bold magenta]")
            for strategy in recommend_mitigation():
                console.print(f"- {strategy}")

        elif choice == '2':
            username = Prompt.ask("Enter username")
            password = Prompt.ask("Enter password", password=True)
            if authenticate_user(username, password):
                console.print("[green]Authentication successful.[/green]")
                user_role = Prompt.ask("Enter your role")
                required_role = "admin"
                if authorize_user(user_role, required_role):
                    console.print("[bold green]Access granted.[/bold green]")
                    log_access_attempt(username, "Resource", True)
                else:
                    console.print("[red]Access denied.[/red]")
                    log_access_attempt(username, "Resource", False)
            else:
                console.print("[red]Authentication failed.[/red]")

        elif choice == '3':
            ip = Prompt.ask("Enter IP address to scan ports")
            open_ports = scan_ports(ip)
            console.print(f"[bold green]Open ports on {ip}:[/bold green] {open_ports}")

            interface = Prompt.ask("Enter network interface to monitor traffic")
            console.print(f"[yellow]Monitoring traffic on {interface}...[/yellow]")
            # Uncomment the next line to start monitoring (requires scapy)
            monitor_traffic(interface)

            detect_intrusion()

        elif choice == '4':
            console.print("[bold blue]Exiting AcSecurity Console.[/bold blue]")
            break

        else:
            console.print("[red]Invalid option. Please try again.[/red]")