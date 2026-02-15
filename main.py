from network_scanner import scan_network
from port_scanner import scan_ports
from vulnerability_checker import check_vulnerabilities
from report_generator import generate_report


def main():
    print("=== Advanced Network Security Assessment Tool ===")
    print("⚠ Scan only authorized networks\n")

    network = input("Enter network range (Example: 192.168.1.1/24): ")

    devices = scan_network(network)

    final_results = []

    for device in devices:
        print(f"\nScanning {device}...")
        open_ports = scan_ports(device)

        for port in open_ports:
            vulnerability = check_vulnerabilities(port)
            print(f"Open Port: {port} | Risk: {vulnerability}")
            final_results.append([device, port, vulnerability])

    generate_report(final_results)


if __name__ == "__main__":
    main()
