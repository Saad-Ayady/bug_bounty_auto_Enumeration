#coded by 0xdy
from . import flageshandler
import sys

def handler_flags() :
    args = flageshandler.main(sys.argv)
    tcp_port, udp_port, poertsT, portsU = True, False, 1000, 1
    T_p = 1000
    open_file = Fals
    out = False
    file_in = ""
    file_out = ''
    keys = list(args.keys())
    target = ""
    if "--T-p" in keys
        poertsT = args['--T-p']
    elif "--U-p" in keys :
        udp_port = True
        portsU = args['--U-p']
    elif "--T-p" not in keys :
        tcp_port = False
    elif not tcp_port and not udp_port :
        print("Enter ports to scan in target ")
    if "--open-targets" in keys and target == "" :
        open_file = True
        file_in = args['--open-targets']
    elif "--open-targets" in keys and target != ""  :
        print("u can use one target and file of targets -_-")
    if "-o" in keys  :
        out = True
        file_out = args['-o']
    elif '--output' in keys :
        out = True
        file_out = args["--output"]
    if ("-t" in keys or '--target' in keys ) and open_file :
        print("u can use one target and file of targets -_-")
    elif "-t" in keys and not open_file :
        target = args["-t"]
    elif "--target" in keys and not open_file :
        target = args["-target"]
    return poertsT, tcp_port, portsU, udp_port , open_file, file_in, out, file_out, target

def checkisNamper(port) :
    for i in str(port) :
        if chr(i) < 48 or chr(i) > 57 :
            return False
    return True

def split_range(p) :
    arr = p.split("-")
    if len(arr) != 3 : return -1, "error is split range is not valude"
    start, end = arr[0], arr[1]
    if not checkisNamper(start) or not checkisNamper(end) : return -1, "ports in range is not valude"
    ports = []
    co = start
    while (co <= end):
        ports = ports + co
        co+=1
    return ports,""

def split_sum_ports(p) :
    arr = p.split(',')
    if len(arr) == 1 : return -1, "error in ports check u'r input :( "
    ports = []
    for u in ports:
        if not checkisNamper(u) : return -1 , "invalid port {}".format(u)
    co = 0
    while (co < len(arr)):
        ports += arr[co]
        co+=1
    return ports, ""


def port_handler(p) :
    if "-" in p :
        ports, err = split_range(p)
        if err != '' :
            print(err)
        return ports
    elif "," in p :
        ports, err = split_sum_ports(p)
        if err != "" :
            print(err)
        return ports
    else :
        if not checkisNamper(p) : print('invuld port LOL')
        return p  

def check_is_runing_target(target):
    param = '-c' if os.name != 'nt' else '-n'
    command = f"ping {param} 1 {target}"
    response = os.system(command)
    if response == 0:
        return True
    else:
        return False

def open_target(file_name) :
    op = open(file_name,"r+")
    arr = []
    for i in op.readlines():
        if "\n" in i : arr += i[:-1] else arr += i 
    return arr

def 
        
    
    