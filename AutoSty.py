import customtkinter
import pyautogui
import keyboard
import time

#Apparence Fenêtre
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Création fenêtre
root = customtkinter.CTk()
root.title("AutoSty")
root.geometry("400x600")

frame = customtkinter.CTkFrame(master=root)

support = customtkinter.StringVar(root)
support2 = customtkinter.StringVar(root)
support3 = customtkinter.StringVar(root)
commentaire = customtkinter.StringVar(root)
commentaire2 = customtkinter.StringVar(root)
check_var = customtkinter.StringVar(root)
combobox_var = customtkinter.StringVar(root)
comboboxPlacement_var = customtkinter.StringVar(root)

pitLog = customtkinter.IntVar(root)
pitLog2 = customtkinter.IntVar(root)
pitLog3 = customtkinter.IntVar(root)
current_function = None

#Menu principal
def Menu():
    #Nettoyage de la frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="AutoSty - Menu")
    label.pack(pady=20, padx=10)

    buttonRY1 = customtkinter.CTkButton(master=frame, text="Poste OK", command=RY1)
    buttonRY1.pack(pady=12, padx=10)

    buttonOB1 = customtkinter.CTkButton(master=frame, text="BROKE", command=OB1)
    buttonOB1.pack(pady=12, padx=10)

    buttonDevis = customtkinter.CTkButton(master=frame, text="Devis", command=Devis)
    buttonDevis.pack(pady=12, padx=10)

    buttonReparation = customtkinter.CTkButton(master=frame, text="Réparation", command=Reparation)
    buttonReparation.pack(pady=12, padx=10)

    keyboard.clear_all_hotkeys()

#Selection du raccourcis clavier selon la page
def on_hotkey():
    if current_function:
        current_function()

#Position souris du début ALEX
def StartPos():
    time.sleep(2)
    pyautogui.click(860,415, duration=0.1, button="right")
    pyautogui.moveTo(1037,912, duration=0.1)
    time.sleep(1.5)
    pyautogui.click(1375,912, duration=0.1)
    time.sleep(2)
    pyautogui.click(928,554, duration=0.1)

#Position souris à la fin ALEX
def endPos():
    pyautogui.click(303,226, duration=0.1)
    time.sleep(2)
    pyautogui.click(1722,183, duration=0.1)
    pyautogui.click(145,533, duration=0.3)
    pyautogui.click(145,533, duration=0)
    pyautogui.hotkey('backspace')

#Script 750
def script750():
    global current_function
    current_function = script750

    StartPos()
    pyautogui.typewrite("750")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("Poste OK")
    for i in range(7):
        pyautogui.hotkey("tab")

    pyautogui.typewrite("OK")
    for i in range(6):
        pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')
    scriptRY1()

#Script RY1
def scriptRY1():

    StartPos()
    pyautogui.typewrite("RY1")
    pyautogui.hotkey("tab")
    keyboard.write("Opérationnel")
    for i in range(5):
        pyautogui.hotkey("tab")
    pyautogui.hotkey("space")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("Sortie SAV")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("space")
    time.sleep(0.4)
    pyautogui.hotkey("tab")
    if current_function == script750:
        if (pitLog.get() == 0):
            pyautogui.hotkey("down")
    elif current_function == scriptReparation:
        if (pitLog3.get() == 1):
            pyautogui.hotkey("down")
    pyautogui.hotkey("tab")
    if check_var.get() =="on" and current_function == scriptReparation:
        pyautogui.hotkey("space")
    pyautogui.hotkey("tab")
    if current_function == script750:
        pyautogui.typewrite(support.get())
    elif current_function == scriptReparation:
        pyautogui.typewrite(support3.get())
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')
    time.sleep(2)
    if current_function == script750:
        endPos()

#Script 751
def script751():
    global current_function
    current_function = script751

    StartPos()
    pyautogui.typewrite("751")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("Poste NOK")
    pyautogui.hotkey("tab")
    text = commentaire.get()
    keyboard.write(text)
    for i in range(6):
        pyautogui.hotkey("tab")

    pyautogui.typewrite("NOK")
    for i in range(6):
        pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')
    scriptOB1()

#Script OB1
def scriptOB1():

    StartPos()
    pyautogui.typewrite("OB1")
    pyautogui.hotkey("tab")
    keyboard.write("Obsolète")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("BROKE")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("BROKE")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("CAS")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("Sortie SAV")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("space")
    time.sleep(0.4)
    pyautogui.hotkey("tab")
    if current_function == script751:
        if (pitLog2.get() == 0):
            pyautogui.hotkey("down")
    elif current_function == scriptReparation:
        if (pitLog3.get() == 1):
            pyautogui.hotkey("down")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    if current_function == script751:
        pyautogui.typewrite(support2.get())
    elif current_function == scriptReparation:
        pyautogui.typewrite(support3.get())
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')
    time.sleep(2)
    if current_function == script751:
        endPos()

#Script Devis
def scriptDevis():
    global current_function
    current_function = scriptDevis

    StartPos()
    pyautogui.typewrite("751")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("Poste NOK")
    pyautogui.hotkey("tab")
    text2 = commentaire2.get()
    keyboard.write(text2)
    for i in range(6):
        pyautogui.hotkey("tab")

    pyautogui.typewrite("NOK")
    for i in range(6):
        pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')

    endPos()

#Script 111
def Script111():
    pyautogui.typewrite("111")
    pyautogui.hotkey("tab")
    if comboboxPlacement_var.get() == "RY1":
        pyautogui.typewrite("Poste OK")
    else:
        pyautogui.typewrite("Poste NOK")
    pyautogui.hotkey("tab")
    match combobox_var.get():
        case "RAM":
            keyboard.write("RAM remplacée")
        case "Ventilateur":
            keyboard.write("Ventilateur remplacé")
        case "Cover":
            keyboard.write("Cover remplacé")
        case "SSD":
            keyboard.write("SSD remplacé")
        case "Clavier":
            keyboard.write("Clavier remplacé")
        case "Ecran":
            keyboard.write("Ecran remplacé")
        case "Lecteur de carte":
            keyboard.write("Lecteur de carte remplacé")
        case "Touchpad":
            keyboard.write("Touchpad remplacé")
        case "Batterie":
            keyboard.write("Batterie remplacée")
        case "Speaker":
            keyboard.write("Speaker remplacé")
        case _:
            return 'Aucune panne selectionnée'

    for i in range(6):
        pyautogui.hotkey("tab")
    if comboboxPlacement_var.get() == "RY1":
        pyautogui.typewrite("OK")
    else:
        pyautogui.typewrite("NOK")
    for i in range(6):
        pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')

#Script Reparation
def scriptReparation():
    global current_function
    current_function = scriptReparation

    StartPos()
    match combobox_var.get():
        case "RAM":
            pyautogui.typewrite("P01")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("RAM OK")
        case "Ventilateur":
            pyautogui.typewrite("P03")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Ventilateur OK")
        case "Cover":
            pyautogui.typewrite("P05")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Cover OK")
        case "SSD":
            pyautogui.typewrite("PO7")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("SSD OK")
        case "Clavier":
            pyautogui.typewrite("P09")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Clavier OK")
        case "Ecran":
            pyautogui.typewrite("P11")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Ecran OK")
        case "Lecteur de carte":
            pyautogui.typewrite("P13")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Lecteur de carte OK")
        case "Touchpad":
            pyautogui.typewrite("P15")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Touchpad OK")
        case "Batterie":
            pyautogui.typewrite("P17")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Batterie OK")
        case "Speaker":
            pyautogui.typewrite("P19")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Speaker OK")
        case _:
            return 'Aucune panne selectionnée'

    for i in range(7):
        pyautogui.hotkey("tab")

    pyautogui.typewrite("OK")
    for i in range(6):
        pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')
    StartPos()
    Script111()

    if comboboxPlacement_var.get() == "OB1":
        scriptOB1()

    elif comboboxPlacement_var.get() == "RY1":
        scriptRY1()

    endPos()

#Frame RY1
def RY1():
    #Nettoyage de la frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.pack(pady=20, padx=60, fill="both", expand=True)
    clavier = 1

    label2 = customtkinter.CTkLabel(master=frame, text="AutoSty - RY1")
    label2.pack(pady=20, padx=10)

    buttonRY1 = customtkinter.CTkButton(master=frame, text="Retour menu", command=Menu)
    buttonRY1.pack(pady=12, padx=10)

    label2 = customtkinter.CTkLabel(master=frame, text="Numéro de support")
    label2.pack(pady=2, padx=10)
    entry1 = customtkinter.CTkEntry(master=frame, textvariable=support)
    entry1.pack(pady=12, padx=15)

    pit = customtkinter.CTkRadioButton(master=frame, text="en PIT", variable=pitLog, value=0)
    pit.pack(pady=12, padx=10)

    log = customtkinter.CTkRadioButton(master=frame, text="en LOG", variable=pitLog, value=1)
    log.pack(pady=12, padx=10)

    buttonOK = customtkinter.CTkButton(master=frame, text="Lancer le script", command=script750)
    buttonOK.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = script750
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)

#Frame OB1
def OB1():
    #Nettoyage de la frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.pack(pady=20, padx=60, fill="both", expand=True)
    clavier = 2

    label2 = customtkinter.CTkLabel(master=frame, text="AutoSty - OB1")
    label2.pack(pady=20, padx=10)

    buttonRY1 = customtkinter.CTkButton(master=frame, text="Retour menu", command=Menu)
    buttonRY1.pack(pady=12, padx=10)

    label2 = customtkinter.CTkLabel(master=frame, text="Commentaire")
    label2.pack(pady=2, padx=2)
    entry1 = customtkinter.CTkEntry(master=frame, textvariable=commentaire)
    entry1.pack(pady=12, padx=10)

    label2 = customtkinter.CTkLabel(master=frame, text="Numéro de support")
    label2.pack(pady=2, padx=2)
    entry1 = customtkinter.CTkEntry(master=frame, textvariable=support2)
    entry1.pack(pady=12, padx=10)

    pit = customtkinter.CTkRadioButton(master=frame, text="en PIT", variable=pitLog2, value=0)
    pit.pack(pady=12, padx=10)

    log = customtkinter.CTkRadioButton(master=frame, text="en LOG", variable=pitLog2, value=1)
    log.pack(pady=12, padx=10)

    buttonNOK = customtkinter.CTkButton(master=frame, text="Lancer le script", command=script751)
    buttonNOK.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = script751
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)

#Frame Devis
def Devis():
    #Nettoyage de la frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.pack(pady=20, padx=60, fill="both", expand=True)
    clavier = 3

    label2 = customtkinter.CTkLabel(master=frame, text="AutoSty - Devis")
    label2.pack(pady=20, padx=10)

    buttonRY1 = customtkinter.CTkButton(master=frame, text="Retour menu", command=Menu)
    buttonRY1.pack(pady=12, padx=10)

    label2 = customtkinter.CTkLabel(master=frame, text="Commentaire")
    label2.pack(pady=2, padx=2)
    entry1 = customtkinter.CTkEntry(master=frame, textvariable=commentaire2)
    entry1.pack(pady=12, padx=10)

    buttonDevis = customtkinter.CTkButton(master=frame, text="Lancer le script", command=scriptDevis)
    buttonDevis.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = scriptDevis
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)

#Frame Reparation
def Reparation():
    #Nettoyage de la frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.pack(pady=20, padx=60, fill="both", expand=True)
    clavier = 3

    label2 = customtkinter.CTkLabel(master=frame, text="AutoSty - Reparation")
    label2.pack(pady=20, padx=10)

    buttonRY1 = customtkinter.CTkButton(master=frame, text="Retour menu", command=Menu)
    buttonRY1.pack(pady=12, padx=10)

    combobox = customtkinter.CTkComboBox(master=frame, values=["Choisir panne", "RAM", "Ventilateur", "Cover", "SSD", "Clavier", "Ecran", "Lecteur de carte", "Touchpad", "Batterie", "Speaker"],
                                        variable=combobox_var)
    combobox_var.set("Choisir panne")
    combobox.pack(pady=12, padx=10)

    comboboxPlacement = customtkinter.CTkComboBox(master=frame, values=["RY1", "OB1", "111"],
                                                variable=comboboxPlacement_var)
    comboboxPlacement_var.set("RY1")
    comboboxPlacement.pack(pady=12, padx=10)

    label2 = customtkinter.CTkLabel(master=frame, text="Numéro de support")
    label2.pack(pady=2, padx=2)
    entry1 = customtkinter.CTkEntry(master=frame, textvariable=support3)
    entry1.pack(pady=12, padx=10)

    pit = customtkinter.CTkRadioButton(master=frame, text="en LOG", variable=pitLog3, value=0)
    pit.pack(pady=12, padx=10)

    log = customtkinter.CTkRadioButton(master=frame, text="en PIT", variable=pitLog3, value=1)
    log.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Etiquette", variable=check_var, onvalue="on", offvalue="off")
    checkbox.pack(pady=12, padx=10)

    buttonDevis = customtkinter.CTkButton(master=frame, text="Lancer le script", command=scriptReparation)
    buttonDevis.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = scriptReparation
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)
    

#Frame principale
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="AutoSty - Menu")
label.pack(pady=20, padx=10)

buttonRY1 = customtkinter.CTkButton(master=frame, text="Poste OK", command=RY1)
buttonRY1.pack(pady=12, padx=10)

buttonOB1 = customtkinter.CTkButton(master=frame, text="BROKE", command=OB1)
buttonOB1.pack(pady=12, padx=10)

buttonDevis = customtkinter.CTkButton(master=frame, text="Devis", command=Devis)
buttonDevis.pack(pady=12, padx=10)

buttonReparation = customtkinter.CTkButton(master=frame, text="Réparation", command=Reparation)
buttonReparation.pack(pady=12, padx=10)

root.mainloop()
