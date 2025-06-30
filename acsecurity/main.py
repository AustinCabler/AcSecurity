import re
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.panel import Panel

console = Console()

def is_valid_username(username):
    return bool(re.match(r"^[a-zA-Z0-9_]{3,20}$", username))

def is_valid_role(role):
    return bool(re.match(r"^[a-zA-Z0-9_]+$", role))

def is_valid_ip(ip):
    return bool(re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip))

def print_menu():
    table = Table(title="AcSecurity Console", show_header=False, box=None)
    table.add_row("[cyan]1.[/cyan]", "Surveillance System Risk Assessment")
    table.add_row("[cyan]2.[/cyan]", "Access Control Management")
    table.add_row("[cyan]3.[/cyan]", "Network Security Monitoring")
    table.add_row("[cyan]4.[/cyan]", "Exit")
    console.print(table)

if __name__ == "__main__":
    console.print(Panel("[bold green]AcSecurity Console[/bold green]"))
    while True:
        print_menu()
        choice = Prompt.ask("[bold yellow]Select an option[/bold yellow]", choices=["1", "2", "3", "4"])

        if choice == '1':
            from acsecurity.core.surveillance import assess_risk, generate_risk_report, recommend_mitigation
            system_config = {
                'camera_quality': 'high',
                'coverage_area': 'wide'
            }
            risk_level = assess_risk(system_config)
            console.print(f"[bold magenta]Risk Level:[/bold magenta] {risk_level}")
            console.print(Panel(generate_risk_report(), title="Risk Report", style="blue"))
            console.print("[bold green]Mitigation Strategies:[/bold green]")
            for strategy in recommend_mitigation():
                console.print(f"- {strategy}")

        elif choice == '2':
            from acsecurity.core.access_control import authenticate_user, authorize_user, log_access_attempt
            username = Prompt.ask("Enter username")
            if not is_valid_username(username):
                console.print("[red]Invalid username format.[/red]")
                continue
            password = Prompt.ask("Enter password", password=True)
            if authenticate_user(username, password):
                console.print("[green]Authentication successful.[/green]")
                user_role = Prompt.ask("Enter your role")
                if not is_valid_role(user_role):
                    console.print("[red]Invalid role format.[/red]")
                    continue
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
            try:
                from acsecurity.core.network_security import scan_ports, monitor_traffic, detect_intrusion
            except ModuleNotFoundError:
                console.print("[red]Error: acsecurity.core.network_security module not found. Please check your project structure.[/red]")
                continue
            ip = Prompt.ask("Enter IP address to scan ports")
            if not is_valid_ip(ip):
                console.print("[red]Invalid IP address format.[/red]")
                continue
            open_ports = scan_ports(ip)
            console.print(f"[bold magenta]Open ports on {ip}:[/bold magenta] {open_ports}")

            interface = Prompt.ask("Enter network interface to monitor traffic")
            console.print(f"[cyan]Monitoring traffic on {interface}...[/cyan]")
            monitor_traffic(interface)

            detect_intrusion()

        elif choice == '4':
            console.print("[bold]Exiting AcSecurity Console.[/bold]")
            break

        else:
            console.print("[red]Invalid option. Please try again.[/red]")