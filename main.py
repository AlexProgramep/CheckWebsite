from tkinter import messagebox, StringVar, VERTICAL, Button, Scrollbar, Menu, Tk, Text, END, Entry, Label
import socket
import requests

width = 400
height = 300

root = Tk()
root.title("CheckWeb")
root.geometry(f"{width}x{height}+700+250")
root.minsize(width, height)
root.maxsize(width, height)
main_menu = Menu()


def infoweb():
    try:
        target = message.get().strip()
        r = requests.head(" http://" + target)
        status_html = str(r.status_code)
        data = f"""IP: {socket.gethostbyname(target)}
Status: {status_html}"""
        text.delete('1.0', END)
        text.insert('1.0', data)
    except Exception as e:
        messagebox.showerror("Помилка", "Введіть правильний домен без протоколу (HTTP/HTTPS).")


def help():
    messagebox.showinfo("Інформація",
                        """Вписуємо домен сайту без протоколу (HTTP/HTTPS),а потiм перевіряємо статус та ip.""")


message = StringVar()

message_button = Button(text="Перевірити", padx="20", pady="15", background="#555", foreground="#fff", command=infoweb)
message_button.place(relx=.5, rely=.7, anchor="center")

text = Text(root, width=400, height=350, wrap="word")
text.place(relx=.5, rely=.2, anchor="center", width="350", height="80")
scrollb = Scrollbar(text, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

message_label = Label(text="Введіть домен без протоколу")
message_label.place(x=110, y=110)

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.5, anchor="center", width="200", height="25")

main_menu.add_cascade(label="Інформація", command=help)

root.config(menu=main_menu)
root.mainloop()
