import customtkinter
import keyboard

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")


def login():
    print(varTest.get())

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

varTest = customtkinter.StringVar(root)
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username", textvariable=varTest)
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

if keyboard.read_hotkey() == ('ctrl + alt + w'):
        print('youhou')

pitLog = customtkinter.IntVar(root)


root.mainloop()
