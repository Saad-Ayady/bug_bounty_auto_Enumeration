import socket
import threading

def udp(host, ports=1000):
    print_lock = threading.Lock()

    def UDB_scan(ip, port, timeout=1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        try:
            sock.sendto(b'ping', (ip, port))
            sock.recvfrom(1024)
            return True
        except socket.timeout:
            return False
        except Exception as e:
            return False
        finally:
            sock.close()
    def thread_function(host, port):
            UDB_scan(host, port)
    threads = []
    for port in range(1, ports):
        thread = threading.Thread(target=thread_function, args=(host, port))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()   