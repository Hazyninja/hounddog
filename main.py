import socket
import struct
import threading


def scan(ip):
    # Attempts to connect to chosen port
    try:
        # Create TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))  # Attempts port connection
        if result == 0:
            print(f'IP: {ip} has port {port} open')
    except Exception as e:
        print(f'Error scanning {ip}: {e}')
    finally:
        sock.close()


def ip_range(start_range, end_range):
    # Converts IP addresses to int and generates IP list
    start = struct.unpack('>I', socket.inet_aton(start_range))[0]
    end = struct.unpack('>I', socket.inet_aton(end_range))[0]
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end+1)]


def run_scanner(start_ip, end_ip):
    # Creates threads and scans IP range
    ips = ip_range(start_ip, end_ip)
    threads = []
    for ip in ips:
        thread = threading.Thread(target=scan, args=(ip,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()  # Doesn't continue until all threads are complete


if __name__ == "__main__":
    port = int(input('Input port to be scanned: '))
    usr_start_ip = input('Input starting IP range: ')
    usr_end_ip = input('Input ending IP range: ')
    run_scanner(usr_start_ip, usr_end_ip)