🛡️ Advanced Network Security Assessment Tool (Python)
📌 Project Overview

The Advanced Network Security Assessment Tool is a Python-based application designed for educational and ethical cybersecurity purposes. It automates the process of assessing the security of a network by:

Discovering active devices on a network

Scanning for open ports

Detecting running services

Identifying basic vulnerabilities

Generating detailed security reports

This tool emphasizes ethical use only and should be run on networks you own or are authorized to test.

🎯 Objectives

Learn and demonstrate network scanning techniques

Understand port scanning and service detection

Perform basic security auditing

Generate structured reports for network analysis

Develop a modular and maintainable Python project

🛠 Key Features

ARP-Based Network Discovery — Detect live devices in LAN

Multithreaded Port Scanning — Efficiently scan common ports

Service Detection & Banner Grabbing — Identify services running on open ports

Vulnerability Alerts — Highlight risky ports like FTP, Telnet, SMB, RDP

Report Generation — Save scan results to CSV for analysis

Modular Design — Easy to extend or integrate new features

📁 Project Structure
SecurityToolkit/
│
├── main.py                  # Entry point of the project
├── network_scanner.py       # Functions for device discovery
├── port_scanner.py          # Functions for scanning ports
├── vulnerability_checker.py # Functions for basic vulnerability checking
├── report_generator.py      # Functions to generate CSV reports
├── requirements.txt         # Required Python packages

▶ How to Run

Install dependencies:

pip install scapy


Run the main program:

python main.py


Enter your network range when prompted (e.g., 192.168.1.1/24)

The program scans devices, checks ports, identifies vulnerabilities, and saves results to security_report.csv.

⚠ Ethical Notice

Only run this tool on authorized networks.

Unauthorized scanning may be illegal and unethical.

Intended for educational and security learning purposes.

📈 Future Enhancements

Add GUI interface using Tkinter

Include OS detection and advanced banner grabbing

Integrate web-based dashboard (Flask/Django)

Implement real-time monitoring and alerting
