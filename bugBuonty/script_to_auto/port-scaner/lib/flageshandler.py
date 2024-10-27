#coded by 0xdy
import sys

def handletargs(arg) :
    for aj in arg :
        if not "=" in aj :
            return False, aj
    return True,"nun"

def return_all_args(arg) :
    arg = arg[1:]
    handler, err = handletargs(arg)
    if err != 'nun' :
        print("Error in arg : ",err)
        exit(1)
    dek_ag = {}
    for av in arg:
        key = av.split("=")[0]
        vul = av.split("=")[1]
        dek_ag[key] = vul
    return dek_ag

def commands(arg) :
    args = return_all_args(arg)
    arr_com = ["--T-p", "--U-p", "-t", "--target", "--open-targets", "-h", "--help", "-o", "---output", "-U", - ]
    list_of_keys = list(args.keys())
    for key in list_of_keys:
        for com in arr_com :
            if key == com :
                return True
    return False

def main(arg):
    args_all = return_all_args(arg)
    if not commands(arg) :
        print("Emmmmm u are use flage not alowd -__-")
        exit(1)
    return args_all
