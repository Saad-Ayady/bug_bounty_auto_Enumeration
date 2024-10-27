#coded by 0xdy

def printor(port, text) :
    len_of_port = len(str(port))
    spaces = ""
    if len_of_port == 1 :
        spaces = "     "
    elif len_of_port == 2 :
        spaces = "    "
    elif len_of_port == 3 :
        spaces = "   "
    elif len_of_port == 4 :
        spaces = "  "
    else:
        spaces = " "
    print(f" _{len_of_port*'_'}{len(spaces)*'_'}_ _{len(text)*'_'}_")
    print(f"| {port}{spaces} | {text} |")
    print(f" -{len_of_port*'-'}{len(spaces)*'-'}- -{len(text)*'-'}-")
