from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import ttkbootstrap as tb

# Initialize the Bootstrap application
root = tb.Window(themename="cosmo")  # You can choose different themes like 'darkly', 'flatly', etc.

root.geometry("500x300+100+100")  # Set root window width to 500 and height to 300
root.title('0xdy')
icon_path = "logo.ico"  # Update this if necessary
try:
    img = Image.open(icon_path)
    img = img.resize((16, 16), Image.LANCZOS)  # Resize to a standard icon size
    photo = ImageTk.PhotoImage(img)
    root.iconphoto(False, photo)  # Set the window icon
except Exception as e:
    print(f"Error loading icon: {e}")

root.minsize(500, 300)  # width, height
root.maxsize(500, 300)  # width, height

# Initialize global variables
entry_value = ""
checkbox_vars = {}
child_checkboxes = {}

# Variable for entry
entry_var = StringVar()

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
    create_new_elements()

def clear_window2():
    for widget in root.winfo_children():
        widget.destroy()
    create_last_wind(entry_value)

def create_scrollable_frame(root):
    frame = Frame(root, width=200, height=110)
    frame.place(x=240, y=120)

    canvas = Canvas(frame, width=200, height=110)
    scroll_y = Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_y.pack(side="right", fill="y")

    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scroll_y.set)

    inner_frame = Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    create_checkboxes(inner_frame)
    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def create_checkboxes(frame):
    global checkbox_vars, child_checkboxes
    checkbox_vars = {}
    child_checkboxes = {}
    categories = {
        "Subdomains": ["Dorking", "ASP", "Brute Force"],
        "Ports": ["Open Ports", "Version", "Programs", "Vulnerability"],
        "Vulnerabilities": ["SQL Injection", "XSS", "LFI", "File Upload"]
    }

    row = 0

    for main_option, sub_options in categories.items():
        main_var = IntVar()
        checkbox_vars[main_option] = main_var
        cb = tb.Checkbutton(frame, text=main_option, variable=main_var, command=lambda opt=main_option: toggle_sub_options(opt))
        cb.grid(row=row, column=0, sticky="w")
        row += 1

        child_checkboxes[main_option] = []
        for sub_option in sub_options:
            sub_var = IntVar()
            checkbox_vars[sub_option] = sub_var
            cb_sub = tb.Checkbutton(frame, text=sub_option, variable=sub_var, state="disabled")
            cb_sub.grid(row=row, column=0, sticky="w", padx=5)  # Minimal 5px padding for subtle indentation
            child_checkboxes[main_option].append(cb_sub)
            row += 1

def toggle_sub_options(main_option):
    main_var = checkbox_vars[main_option]
    for cb_sub in child_checkboxes[main_option]:
        if main_var.get() == 1:
            cb_sub.config(state="normal")
        else:
            cb_sub.config(state="disabled")
            cb_sub.deselect()

def next_action():
    global entry_value
    entry_value = entry.get()  # Save entry value
    checkbox_states = {name: (var.get() == 1) for name, var in checkbox_vars.items()}
    clear_window2()

def create_inputs(win, text, x, y):
    label = Label(win, text=text)
    label.place(x=x, y=y)

def create_new_elements():
    display_image('g.png')
    titels("Developed by 0xdy group...", "black", "white", root)
    create_inputs(root, "Enter URl of tanget : ", 260, 50)
    global entry
    entry = tb.Entry(root, textvariable=entry_var, width=25)
    entry.place(x=250, y=80)

    # Create the Next button and disable it initially
    next_button = tb.Button(root, text="Next", command=next_action, state=DISABLED)
    next_button.place(x=420, y=260)

    # Monitor entry changes to enable/disable the Next button
    entry_var.trace("w", lambda *args: validate_entry(next_button))

    exit_button = tb.Button(root, text="Exit", command=root.quit)
    exit_button.place(x=350, y=260)

    create_scrollable_frame(root)

def validate_entry(button):
    if entry_var.get().strip():  # Check if entry is not empty
        button.config(state=NORMAL)
    else:
        button.config(state=DISABLED)

def create_last_wind(entry_value):
    display_image('g.png')
    titels("Developed by 0xdy group...", "black", "white", root)
    Label(root, text=f"Target Name: {entry_value}", font=('Arial', 12)).pack(padx=20, pady=30)

def titels(text, color, text_color, win):
    title_frame = Frame(win, bg=color, height=30)
    title_frame.pack(fill=X)

    bold_font = font.Font(family='Courier', size=12, weight='bold')
    title_label = Label(title_frame, text=text, bg=color, fg=text_color, font=bold_font)
    title_label.pack(side=LEFT, padx=10, pady=5)

def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((200, 270))  
    img_tk = ImageTk.PhotoImage(img)
    label = Label(root, image=img_tk)
    label.image = img_tk
    label.place(x=-1, y=32)  

def create_scrollable_window(text):
    frame = Frame(root, width=30, height=100)
    frame.place(x=210, y=40)  
    text_area = Text(frame, wrap='word', width=33, height=10) 
    text_area.insert(END, text) 
    text_area.config(state=DISABLED)
    text_area.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar = Scrollbar(frame, command=text_area.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_area['yscrollcommand'] = scrollbar.set
    input_area = tb.Entry(root, width=20)
    input_area.place(x=220, y=300) 
    def print_input():
        input_text = input_area.get()
        print(input_text) 
        input_area.delete(0, END)

    input_area.bind('<Return>', lambda event: print_input())

def create_checkbox_buttons():
    checkbox_var = BooleanVar()
    checkbox = tb.Checkbutton(root, text="Are you ready?", variable=checkbox_var, command=lambda: on_checkbox_toggle(continue_button, checkbox_var))
    checkbox.place(x=210, y=230)
    exit_button = tb.Button(root, text="Exit", command=root.quit)
    exit_button.place(x=330, y=260)
    continue_button = tb.Button(root, text="Continue", command=clear_window, state=DISABLED)
    continue_button.place(x=390, y=260) 
    def on_checkbox_toggle(button, var):
        if var.get():  
            button.config(state=NORMAL)  
        else:
            button.config(state=DISABLED) 

display_image('g.png')
titels("Developed by 0xdy group...", "black", "white", root)
create_scrollable_window("Françoise d’Aubigné...")
create_checkbox_buttons()

root.mainloop()
