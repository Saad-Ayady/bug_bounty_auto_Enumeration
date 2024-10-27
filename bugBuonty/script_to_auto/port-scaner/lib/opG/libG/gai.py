from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x300")
root.title('0xdy')

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
    create_new_elements() 

def create_new_elements():
    message_label = Label(root, text="You have continued! Create new elements below:")
    message_label.pack(pady=20)
    titels("New Elements", "blue", "white", root)
    new_checkbox_var = BooleanVar()
    new_checkbox = Checkbutton(root, text="New Checkbox", variable=new_checkbox_var)
    new_checkbox.pack(pady=10)
    new_button = Button(root, text="Do Something", command=lambda: print("Doing something..."))
    new_button.pack(pady=10)


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
    input_area = Entry(root, width=20)
    input_area.place(x=220, y=300) 
    def print_input():
        input_text = input_area.get()
        print(input_text) 
        input_area.delete(0, END)

    input_area.bind('<Return>', lambda event: print_input())

def create_checkbox_buttons():
    checkbox_var = BooleanVar()
    checkbox = Checkbutton(root, text="Are you ready?", variable=checkbox_var, command=lambda: on_checkbox_toggle(continue_button, checkbox_var))
    checkbox.place(x=210, y=230)
    exit_button = Button(root, text="Exit", command=root.quit)
    exit_button.place(x=330, y=260)
    continue_button = Button(root, text="Continue", command=clear_window, state=DISABLED)
    continue_button.place(x=390, y=260) 
    def on_checkbox_toggle(button, var):
        if var.get():  
            button.config(state=NORMAL)  
        else:
            button.config(state=DISABLED) 

display_image('g.png')
titels("Developed by 0xdy group...", "black", "white", root)
create_scrollable_window("Françoise d’Aubigné est la fille de Constant d'Aubigné — lui-même fils du célèbre poète protestant et ami d'Henri IV, Agrippa d'Aubigné — et de sa seconde épouse Jeanne de Cardilhac. Constant d'Aubigné, après avoir abjuré sa foi protestante en 1618, assassine sa première épouse et son amant en 1619, puis dépense rapidement la dot de la deuxième, et est soupçonné d'intelligence avec les Anglais avec qui il est en relation d'affaires. Il est ainsi enfermé dans plusieurs prisons, dont celle de Bordeaux, le Château Trompette, et celle de Niort2. Françoise naît le 27 novembre 1635 rue du Pont dans la prison royale de Niort (baptisée à Niort, paroisse Notre-Dame), dans la geôle où son père est incarcéré pour dettes (Jeanne de Cardilhac, trop jeune et désargentée, partageant la cellule avec son mari)N 1, ce lieu de naissance étant incertain3.Lorsque son père sort de la prison de Niort, la jeune Françoise passe les premiers mois de sa petite enfance chez madame de Villette, sa tante huguenote, au château de Mursay, au nord de Niort. Elle passe les six années suivantes avec ses parents dans la colonie de Martinique : son père ayant obtenu la charge de gouverneur des Îles de Marie-Galante, il s'installe dans « l’île aux fleurs » où il a décidé de faire fortune4. Elle y garde un souvenir très fort, transmis à ses futurs époux, le poète burlesque Paul Scarron puis le roi de France Louis XIV, qui décide dès 1674 d'intensifier la culture de la canne à sucre en Martinique puis à Saint-Domingue.Le nom de son père est cité dans un premier voyage un an plus tôt, celui de 1635 avec Pierre Belain d'Esnambuc, fondateur de Saint-Pierre en Martinique en 1635. Le couple part en 1636 pour la colonie de Saint-Christophe, d'où il gagne la Martinique5. Françoise vit avec ses parents dans le village du Prêcheur, le premier où est arrivé d'Esnambuc, tout près de Saint-PierreN 2 à l'extrémité nord-ouest de la Martinique, exposé aux attaques incessantes des autochtones de l'île de la Dominique.Officiellement, son père est gouverneur de la toute petite île de Marie-Galante, toute proche. Mais ce titre ne lui est pas reconnu et il n'a pas les moyens de le valoriser. L'île est alors vierge et doit en principe gouverner la Martinique, elle-même couverte aux neuf dixièmes de forêts, où autochtones et boucaniers font la loi. La famille de Françoise survit en fait dans la pauvreté, alors que la colonie anglais de Barbade, non loin, accède bientôt à la richesse. Ce séjour de six ans lui vaudra le surnom de « belle Indienne ». Il s'achève à l'époque où les colons de la Martinique tentent sans succès d'introduire la culture de la canne à sucre, qui s'avère très rentable à la Barbade dès les années 1640, et entraîne l'éviction des planteurs de tabac. À son retour en France, en juillet 1647, Françoise apprend la mort de son père qui avait abandonné sa famille en 1645 pour chercher en métropole à faire reconnaître son titre de gouverneur. Jeanne de Cardilhac et ses trois enfants vivent misérablement dans une pièce unique, dans une maison proche du port de La Rochelle. La future Madame de Maintenon « n'oubliera jamais l'humiliation de la mendicité qu'elle a vécue à l'époque de ses douze ans, dans la faim, le froid, le désespoir de sa mère » qui « se perd dans le monde des hommes de loi parisiens, sans parvenir à recouvrer une partie de l'héritage » de son mari6. Elle est à nouveau prise en charge par sa tante de Niort, Mme de Villette, fervente protestante. Sa marraine, Madame de Neuillant, fervente catholique, obtient de la reine-mère Anne d'Autriche une lettre de cachet pour récupérer Françoise et lui permettre de pratiquer le catholicisme (en effet à sa naissance Madame d'Aubigné l'avait fait baptiser dans la religion catholique) et renier sa foi calviniste. Elle la place contre sa volonté au couvent des Ursulines de Niort, puis chez les Ursulines de la rue Saint-Jacques à Paris7 où, grâce à la douceur et l'affection d'une religieuse, sœur Céleste, la jeune fille renonce définitivement au calvinisme, condition indispensable pour pouvoir accompagner Mme de Neuillant dans les salons parisiens. C'est à l'une de ces réunions mondaines qu'elle rencontre le chevalier de Méré qui se prend d'affection pour celle qu'il nomme « la belle Indienne » et s'offre de l'instruire convenablement. ")
create_checkbox_buttons()

root.mainloop()
