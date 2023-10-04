import customtkinter
import tkinter
from tkinter import *

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

# Fenêtre principale
frame = customtkinter.CTkFrame(master=root)

# Variables générales
support = customtkinter.StringVar(root)
support2 = customtkinter.StringVar(root)
support3 = customtkinter.StringVar(root)
support4 = customtkinter.StringVar(root)
supportBouseNep = customtkinter.StringVar(root)
commentaire = customtkinter.StringVar(root)
commentaire2 = customtkinter.StringVar(root)
commentaireBouse = customtkinter.StringVar(root)
commentaireBouseNep = customtkinter.StringVar(root)
check_var = customtkinter.StringVar(root)
check_varRY1 = customtkinter.StringVar(root)
check_var_bouse = customtkinter.StringVar(root)
combobox_var = customtkinter.StringVar(root)
combobox_var_bouse = customtkinter.StringVar(root)
comboboxPlacement_var = customtkinter.StringVar(root)
comboboxQualite_var = customtkinter.StringVar(root)
qualite = customtkinter.StringVar(root)

# Variables pour la liste
entry = customtkinter.StringVar()
listbox = Listbox

# Variables pour le support
pitLog = customtkinter.IntVar(root)
pitLog2 = customtkinter.IntVar(root)
pitLog3 = customtkinter.IntVar(root)
pitLogBouse = customtkinter.IntVar(root)
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

    buttonBouse = customtkinter.CTkButton(master=frame, text="Projet Bouse", command=MenuBouse, fg_color='#c86c29',hover_color='#804418')
    buttonBouse.pack(pady=12, padx=10)

    keyboard.clear_all_hotkeys()

#Menu Bouse
def MenuBouse():
    #Nettoyage de la frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="AutoSty - Projet Bouse")
    label.pack(pady=20, padx=10)

    buttonRY1 = customtkinter.CTkButton(master=frame, text="Réparable", command=BouseRep, fg_color='#c86c29',hover_color='#683714')
    buttonRY1.pack(pady=12, padx=10)

    buttonOB1 = customtkinter.CTkButton(master=frame, text="Non réparable", command=BouseNep, fg_color='#c86c29',hover_color='#683714')
    buttonOB1.pack(pady=12, padx=10)

    buttonDevis = customtkinter.CTkButton(master=frame, text="Réparé", command=BouseR, fg_color='#c86c29',hover_color='#683714')
    buttonDevis.pack(pady=12, padx=10)

    buttonRY1 = customtkinter.CTkButton(master=frame, text="Retour menu", command=Menu)
    buttonRY1.pack(pady=12, padx=10)

    keyboard.clear_all_hotkeys()

# Selection du raccourcis clavier selon la page
def on_hotkey():
    if current_function:
        current_function()

# ------------------------- POSITION DE SOURIS DE LEO -----------------------------------------

# Position souris du début
def StartPos():
    time.sleep(2)
    pyautogui.click(1000,385, duration=0.1, button="right")
    pyautogui.moveTo(1147,803, duration=0.1)
    time.sleep(1.5)
    pyautogui.click(1437,803, duration=0.1)
    time.sleep(1.5)
    pyautogui.click(784,507, duration=0.1)

# Position souris à la fin
def endPos():
    pyautogui.click(250,235, duration=0.1)
    time.sleep(2)
    pyautogui.click(1900,200, duration=0.1)
    pyautogui.click(135,490, duration=0.3)
    pyautogui.click(135,490, duration=0)

# Position souris pour la liste
def ListPos():
    pyautogui.click(135,490, duration=0.3)
    pyautogui.click(135,490, duration=0)

#Position de souris pour le projet Bouse - changement code famille
def BousePos():
    pyautogui.click(1000,385, duration=0.1, button="right")
    pyautogui.moveTo(1130,485, duration=0.1)
    time.sleep(1.5)
    pyautogui.click(1420,600, duration=0.1)
    time.sleep(1.5)
    pyautogui.click(283,675, duration=0.3)
    pyautogui.click(283,675, duration=0)

# ------------------------- POSITION DE SOURIS DE LEO -----------------------------------------

# Ajout du poste dans la liste
def add_text():
    text = entry.get()
    if text:
        listbox.insert(tkinter.END, text)
        entry.delete(0, tkinter.END)
# Ajout du poste dans la liste avec touche entrer
def add_textEvent(e):
    text = entry.get()
    if text:
        listbox.insert(tkinter.END, text)
        entry.delete(0, tkinter.END)

# Lancement des script avec la liste
def scriptListe():
    for index in range(listbox.size()):
        item = listbox.get(index)
        time.sleep(1)
        ListPos()
        keyboard.write(item)
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(0.3)
        pyautogui.hotkey('enter')
        time.sleep(2.5)
        if current_function == script750:
            script750()
        elif current_function == script751:
            script751()
        elif current_function == scriptDevis:
            scriptDevis()

    # Fenetre de complétion d'insertion de la liste
    FinishWindow = customtkinter.CTkToplevel(root)
    FinishWindow.grab_set()
    FinishWindow.title("Autosty - terminé")
    FinishWindow.geometry("300x300")
    label2 = customtkinter.CTkLabel(FinishWindow, text="Insertion terminée")
    label2.pack(pady=10, padx=10)
    button = customtkinter.CTkButton(FinishWindow, text="Fermer", command=FinishWindow.destroy, fg_color='green',hover_color='darkgreen')
    button.pack(pady=5, padx=5)

# Script 750
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

# Script RY1
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
    elif check_varRY1.get() =="on" and current_function == script750:
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
        EndPos()

# Script 751
def script751():
    global current_function
    current_function = script751

    StartPos()
    if comboboxQualite_var.get() == "751":
        pyautogui.typewrite("751")
    elif comboboxQualite_var.get() == "755":
        pyautogui.typewrite("755")
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

# Script OB1
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
        EndPos()

# Script Devis
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
    time.sleep(1)

    EndPos()

# Script 111
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

# Script Reparation
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
            pyautogui.typewrite("P07")
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

    EndPos()

# Script Bouse réparable
def scriptBouseRep():
    global current_function
    current_function = scriptBouseRep

    StartPos()
    pyautogui.typewrite("751")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("Poste NOK")
    pyautogui.hotkey("tab")
    textBouse = commentaireBouse.get()
    keyboard.write(textBouse)
    for i in range(6):
        pyautogui.hotkey("tab")

    pyautogui.typewrite("NOK")
    for i in range(6):
        pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')
    time.sleep(1)

    EndPos()

# Script Bouse Non réparable
def scriptBouseNep():
    global current_function
    current_function = scriptBouseNep
    StartPos()
    pyautogui.typewrite("OB1")
    pyautogui.hotkey("tab")
    keyboard.write("Obsolète")
    pyautogui.hotkey("tab")
    text = commentaireBouseNep.get()
    keyboard.write(text)
    pyautogui.hotkey("tab")
    pyautogui.typewrite("DEEE")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("DEEE")           
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
    if (pitLogBouse.get() == 1):
            pyautogui.hotkey("down")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.typewrite(supportBouseNep.get())
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')
    time.sleep(2)
    EndPos()

# Script Bouse Réparé (Projet PE)
def scriptBouseR():
    global current_function
    current_function = scriptBouseR

    if qualite.get() == "LVPO4N" or qualite.get() == "LVPO4Q" or qualite.get() == "LVPO4W":
        time.sleep(2)
        BousePos()
        time.sleep(1.5)
        
        if qualite.get() == "LVPO4N":
            pyautogui.typewrite("LVPO8B")
        elif qualite.get() == "LVPO4Q":
            pyautogui.typewrite("LVPO8C")
        elif qualite.get() == "LVPO4W":
            pyautogui.typewrite("LVPO8D")
        pyautogui.hotkey("tab")
        pyautogui.hotkey("tab")
        pyautogui.hotkey("tab")
        pyautogui.hotkey("tab")
        pyautogui.typewrite("ART")
        pyautogui.hotkey("tab")
        pyautogui.typewrite("AM")
        for i in range(6):
            pyautogui.hotkey("tab")
        pyautogui.hotkey('enter')

    StartPos()
    pyautogui.typewrite("111")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("Poste OK")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("RUN")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("RUN")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("OK")
    for i in range(6):
        pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')

    StartPos()
    match combobox_var_bouse.get():
        case "RAM":
            pyautogui.typewrite("P02")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("RAM OK")
        case "Ventilateur":
            pyautogui.typewrite("P04")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Ventilateur OK")
        case "Cover":
            pyautogui.typewrite("P06")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Cover OK")
        case "SSD":
            pyautogui.typewrite("P08")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("SSD OK")
        case "Clavier":
            pyautogui.typewrite("P10")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Clavier OK")
        case "Ecran":
            pyautogui.typewrite("P12")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Ecran OK")
        case "Lecteur de carte":
            pyautogui.typewrite("P14")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Lecteur de carte OK")
        case "Touchpad":
            pyautogui.typewrite("P16")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Touchpad OK")
        case "Batterie":
            pyautogui.typewrite("P18")
            pyautogui.hotkey("tab")
            pyautogui.typewrite("Batterie OK")
        case "Speaker":
            pyautogui.typewrite("P20")
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
    pyautogui.hotkey("down")
    pyautogui.hotkey("tab")
    if check_var_bouse.get() =="on":
        pyautogui.hotkey("space")
    pyautogui.hotkey("tab")
    pyautogui.typewrite(support4.get())
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')
    time.sleep(1.5)

    EndPos()

# Frame RY1
def RY1():
    # Nettoyage de la frame
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

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Etiquette", variable=check_varRY1, onvalue="on", offvalue="off")
    checkbox.pack(pady=12, padx=10)

    buttonListe = customtkinter.CTkButton(master=frame, text="Insertion groupée", command=openlistWindow)
    buttonListe.pack(pady=12, padx=10)

    buttonOK = customtkinter.CTkButton(master=frame, text="Lancer le script", command=script750, fg_color='#d11128',hover_color='#6a0915')
    buttonOK.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = script750
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)

# Frame OB1
def OB1():
    # Nettoyage de la frame
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

    comboboxQualite = customtkinter.CTkComboBox(master=frame, values=["751", "755"],
                                                variable=comboboxQualite_var)
    comboboxQualite_var.set("751")
    comboboxQualite.pack(pady=12, padx=10)

    pit = customtkinter.CTkRadioButton(master=frame, text="en PIT", variable=pitLog2, value=0)
    pit.pack(pady=12, padx=10)

    log = customtkinter.CTkRadioButton(master=frame, text="en LOG", variable=pitLog2, value=1)
    log.pack(pady=12, padx=10)

    buttonListe = customtkinter.CTkButton(master=frame, text="Insertion groupée", command=openlistWindow)
    buttonListe.pack(pady=12, padx=10)

    buttonNOK = customtkinter.CTkButton(master=frame, text="Lancer le script", command=script751, fg_color='#d11128',hover_color='#6a0915')
    buttonNOK.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = script751
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)

# Frame Devis
def Devis():
    # Nettoyage de la frame
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

    buttonListe = customtkinter.CTkButton(master=frame, text="Insertion groupée", command=openlistWindow)
    buttonListe.pack(pady=12, padx=10)

    buttonDevis = customtkinter.CTkButton(master=frame, text="Lancer le script", command=scriptDevis, fg_color='#d11128',hover_color='#6a0915')
    buttonDevis.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = scriptDevis
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)

# Frame Reparation
def Reparation():
    # Nettoyage de la frame
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

    buttonDevis = customtkinter.CTkButton(master=frame, text="Lancer le script", command=scriptReparation, fg_color='#d11128',hover_color='#6a0915')
    buttonDevis.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = scriptReparation
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)

# Frame Bouse Réparable
def BouseRep():
    # Nettoyage de la frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.pack(pady=20, padx=60, fill="both", expand=True)
    clavier = 3

    label2 = customtkinter.CTkLabel(master=frame, text="AutoSty - Bouse Réparable")
    label2.pack(pady=20, padx=10)

    buttonRY1 = customtkinter.CTkButton(master=frame, text="Retour menu", command=MenuBouse, fg_color='#c86c29',hover_color='#683714')
    buttonRY1.pack(pady=12, padx=10)

    label2 = customtkinter.CTkLabel(master=frame, text="Commentaire")
    label2.pack(pady=2, padx=2)
    entry1 = customtkinter.CTkEntry(master=frame, textvariable=commentaireBouse)
    entry1.pack(pady=12, padx=10)

    buttonDevis = customtkinter.CTkButton(master=frame, text="Lancer le script", command=scriptBouseRep, fg_color='#d11128',hover_color='#6a0915')
    buttonDevis.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = BouseRep
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)

# Frame Bouse Non réparable
def BouseNep():
    # Nettoyage de la frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.pack(pady=20, padx=60, fill="both", expand=True)
    clavier = 2

    label2 = customtkinter.CTkLabel(master=frame, text="AutoSty - Bouse Non réparable")
    label2.pack(pady=20, padx=10)

    buttonRY1 = customtkinter.CTkButton(master=frame, text="Retour menu", command=MenuBouse, fg_color='#c86c29',hover_color='#683714')
    buttonRY1.pack(pady=12, padx=10)

    label2 = customtkinter.CTkLabel(master=frame, text="Commentaire")
    label2.pack(pady=2, padx=2)
    entry1 = customtkinter.CTkEntry(master=frame, textvariable=commentaireBouseNep)
    entry1.pack(pady=12, padx=10)

    label2 = customtkinter.CTkLabel(master=frame, text="Numéro de support")
    label2.pack(pady=2, padx=2)
    entry1 = customtkinter.CTkEntry(master=frame, textvariable=supportBouseNep)
    entry1.pack(pady=12, padx=10)

    pit = customtkinter.CTkRadioButton(master=frame, text="en LOG", variable=pitLogBouse, value=0)
    pit.pack(pady=12, padx=10)

    log = customtkinter.CTkRadioButton(master=frame, text="en PIT", variable=pitLogBouse, value=1)
    log.pack(pady=12, padx=10)

    buttonNOK = customtkinter.CTkButton(master=frame, text="Lancer le script", command=scriptBouseNep, fg_color='#d11128',hover_color='#6a0915')
    buttonNOK.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = scriptBouseNep
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)

# Frame Bouse Réparé
def BouseR():
    # Nettoyage de la frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.pack(pady=20, padx=60, fill="both", expand=True)
    clavier = 3

    label2 = customtkinter.CTkLabel(master=frame, text="AutoSty - Réparé")
    label2.pack(pady=20, padx=10)

    buttonRY1 = customtkinter.CTkButton(master=frame, text="Retour menu", command=MenuBouse, fg_color='#c86c29',hover_color='#683714')
    buttonRY1.pack(pady=12, padx=10)

    combobox = customtkinter.CTkComboBox(master=frame, values=["Choisir panne", "RAM", "Ventilateur", "Cover", "SSD", "Clavier", "Ecran", "Lecteur de carte", "Touchpad", "Batterie", "Speaker"],
                                        variable=combobox_var_bouse)
    combobox_var_bouse.set("Choisir panne")
    combobox.pack(pady=12, padx=10)

    label3 = customtkinter.CTkLabel(master=frame, text="Numéro de qualité")
    label3.pack(pady=2, padx=2)
    entry2 = customtkinter.CTkEntry(master=frame, textvariable=qualite)
    entry2.pack(pady=12, padx=10)

    label2 = customtkinter.CTkLabel(master=frame, text="Numéro de support")
    label2.pack(pady=2, padx=2)
    entry1 = customtkinter.CTkEntry(master=frame, textvariable=support4)
    entry1.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Etiquette", variable=check_var_bouse, onvalue="on", offvalue="off")
    checkbox.pack(pady=12, padx=10)

    buttonDevis = customtkinter.CTkButton(master=frame, text="Lancer le script", command=scriptBouseR, fg_color='#d11128',hover_color='#6a0915')
    buttonDevis.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = scriptBouseR
    keyboard.add_hotkey("ctrl + alt + w", on_hotkey)

# Nouvelle fenêtre pour la liste
def openlistWindow():
    global entry, listbox
     
    # Toplevel Créer une nouvelle fenêtre et grab_set la laisse en premier plan
    listWindow = customtkinter.CTkToplevel(root)
    listWindow.grab_set()

    # Nom de la fenêtre
    listWindow.title("AutoSty - Liste de postes")

    # Taille de la fenêtre
    listWindow.geometry("400x500")

    # Titre
    if current_function == script750:
        lab = "Liste de postes - RY1"
    elif current_function == script751:
        lab = "Liste de postes - OB1"
    elif current_function == scriptDevis:
        lab = "Liste de postes - Devis"
    label2 = customtkinter.CTkLabel(listWindow, text=lab)
    label2.pack(pady=10, padx=10)

    # Créer le widget Entry pour saisir le texte
    entry = customtkinter.CTkEntry(listWindow)
    entry.pack(pady=1, padx=1)

    # Créer le widget Button pour ajouter le texte à la liste
    button = customtkinter.CTkButton(listWindow, text="Ajouter", command=add_text)
    button.pack(pady=5, padx=5)

    # Appuyer sur entrer pour ajouter le texte à la liste
    listWindow.bind('<Return>',add_textEvent)

    # Créer le widget Listbox pour afficher la liste de texte
    listbox = Listbox(listWindow, bg="#212121", fg="white")
    listbox.pack(pady=1, padx=1)

    buttonListe = customtkinter.CTkButton(listWindow, text="Lancer le script", command=scriptListe, fg_color='#d11128',hover_color='#6a0915')
    buttonListe.pack(pady=10, padx=10)

    labelPrev = customtkinter.CTkLabel(listWindow, text="(Ne pas oublier Reflex dans le champ de vision)")
    labelPrev.pack(pady=1, padx=1)
    

# Frame principale
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

buttonBouse = customtkinter.CTkButton(master=frame, text="Projet Bouse", command=MenuBouse, fg_color='#c86c29',hover_color='#683714')
buttonBouse.pack(pady=12, padx=10)

root.mainloop()
