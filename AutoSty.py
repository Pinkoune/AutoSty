import customtkinter
import pyautogui
import keyboard
import time

#Apparence Fenêtre
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Création fenêtre
root = customtkinter.CTk()
root.geometry("400x510")

frame = customtkinter.CTkFrame(master=root)
support = customtkinter.StringVar(root)
support2 = customtkinter.StringVar(root)
commentaire = customtkinter.StringVar(root)
commentaire2 = customtkinter.StringVar(root)
pitLog = customtkinter.IntVar(root)
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

    keyboard.clear_all_hotkeys()

#Selection du raccourcis clavier selon la page
def on_hotkey():
    if current_function:
        current_function()

#Script RY1
def scriptRY1():
    time.sleep(2)
    pyautogui.click(865,360, duration=0.1, button="right")
    pyautogui.moveTo(1017,770, duration=0.1)
    time.sleep(1)
    pyautogui.click(1305,770, duration=0.1)
    time.sleep(1.5)
    pyautogui.click(791,477, duration=0.1)

    pyautogui.typewrite("750")
    pyautogui.hotkey("tab")
    pyautogui.typewrite("Poste OK")
    for i in range(7):
        pyautogui.hotkey("tab")

    pyautogui.typewrite("OK")
    for i in range(6):
        pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')

    time.sleep(1)
    pyautogui.click(865,360, duration=0.1, button="right")
    pyautogui.moveTo(1017,770, duration=0.1)
    time.sleep(0.7)
    pyautogui.click(1305,770, duration=0.1)
    time.sleep(1.5)
    pyautogui.click(791,477, duration=0.1)

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
    pyautogui.hotkey("tab")
    pyautogui.typewrite(support.get())
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')
    time.sleep(1.5)

    pyautogui.click(249,203, duration=0.1)
    time.sleep(2)
    pyautogui.click(1902,170, duration=0.1)
    pyautogui.click(130,458, duration=0.3)
    pyautogui.click(130,458, duration=0)
    pyautogui.hotkey('backspace')

#Script OB1
def scriptOB1():
    global current_function
    current_function = scriptOB1
    time.sleep(2)
    pyautogui.click(865,360, duration=0.1, button="right")
    pyautogui.moveTo(1017,770, duration=0.1)
    time.sleep(0.7)
    pyautogui.click(1305,770, duration=0.1)
    time.sleep(1.5)
    pyautogui.click(791,477, duration=0.1)

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
    pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')

    time.sleep(1)
    pyautogui.click(865,360, duration=0.1, button="right")
    pyautogui.moveTo(1017,770, duration=0.1)
    time.sleep(0.7)
    pyautogui.click(1305,770, duration=0.1)
    time.sleep(1.5)
    pyautogui.click(791,477, duration=0.1)

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
    if (pitLog.get() == 1):
        pyautogui.hotkey("down")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.typewrite(support2.get())
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')
    time.sleep(1.5)

    pyautogui.click(249,203, duration=0.1)
    time.sleep(2)
    pyautogui.click(1902,170, duration=0.1)
    pyautogui.click(130,458, duration=0.3)
    pyautogui.click(130,458, duration=0)
    pyautogui.hotkey('backspace')

#Script Devis
def scriptDevis():
    global current_function
    current_function = scriptDevis
    time.sleep(2)
    pyautogui.click(865,360, duration=0.1, button="right")
    pyautogui.moveTo(1017,770, duration=0.1)
    time.sleep(0.7)
    pyautogui.click(1305,770, duration=0.1)
    time.sleep(1.5)
    pyautogui.click(791,477, duration=0.1)

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
    pyautogui.hotkey("tab")
    pyautogui.hotkey('enter')

    pyautogui.click(249,203, duration=0.1)
    time.sleep(2)
    pyautogui.click(1902,170, duration=0.1)
    pyautogui.click(130,458, duration=0.3)
    pyautogui.click(130,458, duration=0)
    pyautogui.hotkey('backspace')

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

    buttonOK = customtkinter.CTkButton(master=frame, text="Lancer le script", command=scriptRY1)
    buttonOK.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = scriptRY1
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

    pit = customtkinter.CTkRadioButton(master=frame, text="en LOG", variable=pitLog, value=0)
    pit.pack(pady=12, padx=10)

    log = customtkinter.CTkRadioButton(master=frame, text="en PIT", variable=pitLog, value=1)
    log.pack(pady=12, padx=10)

    buttonNOK = customtkinter.CTkButton(master=frame, text="Lancer le script", command=scriptOB1)
    buttonNOK.pack(pady=12, padx=10)

    labelHotkey = customtkinter.CTkLabel(master=frame, text="Ou utilisez Ctrl+Alt+W")
    labelHotkey.pack(pady=1, padx=1)

    global current_function
    current_function = scriptOB1
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

root.mainloop()
