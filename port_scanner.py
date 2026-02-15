import socket
import threading

COMMON_PORTS = [21, 22, 23, 80, 443, 445, 3389]

def scan_port(ip, port, results):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            results.append(port)
        sock.close()
    except:
        pass


def scan_ports(ip):
    open_ports = []
    threads = []

    for port in COMMON_PORTS:
        t = threading.Thread(target=scan_port, args=(ip, port, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return open_ports
