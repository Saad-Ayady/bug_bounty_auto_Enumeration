import socket
import threading
from . import printor
   
def tcp(host, ports=1000) :
    print_lock = threading.Lock()
    def TCP_scan(host, port, timeout=1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            with print_lock:
                printor.printor(port,"open")
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False
        except Exception as e:
            return False
        finally:
            sock.close()
    def thread_function(host, port):
        TCP_scan(host, port)

    threads = []
    for port in range(1, ports):
        thread = threading.Thread(target=thread_function, args=(host, port))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()