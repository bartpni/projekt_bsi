import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

file_cont = ""
save_cont = ""
window = tk.Tk()

window.geometry("400x300")
window.title('Aplikacja szyfrujaca')

m_font = ('times', 10,)

upload_f = tk.Label(window, text='Dodaj plik z informacją w formacie .txt', width=50, font=m_font)
upload_f.grid(row=1, column=1)

b_upload = tk.Button(window, text='Dodaj plik', width=20, command=lambda: upload_file())
b_upload.grid(row=2, column=1)

b_encode = tk.Button(window, text='Zaszyfruj dane', width=20, command=lambda: encode())
b_encode.grid(row=4, column=1)

b_encode = tk.Button(window, text='Odszyfruj dane', width=20, command=lambda: decode())
b_encode.grid(row=5, column=1)

b_encode = tk.Button(window, text='Zapisz dane', width=20, command=lambda: save_file())
b_encode.grid(row=6, column=1)

shift = Spinbox(window, from_=1, to=100)
shift.grid(row=7, column=1)

vlist = ["Cypher", "ROT 13"]

lista = ttk.Combobox(window, values=vlist)
lista.set("Wybierz szyfr")
lista['state'] = 'readonly'
lista.grid(row=3, column=1)


def upload_file():
    file = filedialog.askopenfilename(filetypes=[("Plik tekstowy", '.txt')])
    fob = open(file, 'r')
    global file_cont
    file_cont = fob.read().lower()


def encode():
    global save_cont
    if lista.get() == "Cypher":
        number = int(shift.get())
        way = 0
        encode_text = cypher(way, number)
        save_cont = encode_text
        print(encode_text)
    elif lista.get() == "ROT 13":
        way = 0
        encode_text = ROT_13(way)
        save_cont = encode_text
        print(encode_text)


def decode():
    global shift
    global save_cont
    if lista.get() == "Cypher":
        number = int(shift.get())
        way = 1
        decode_text = cypher(way, number)
        save_cont = decode_text
        print(decode_text)
    elif lista.get() == "ROT 13":
        way = 1
        encode_text = ROT_13(way)
        save_cont = encode_text
        print(encode_text)


def save_file():
    fob = filedialog.asksaveasfile(filetypes=[("Plik tekstowy", '*.txt')], defaultextension='.txt', mode='w')
    fob.write(str(save_cont))
    fob.close()


def cypher(way, shift):
    global file_cont
    cipher_text = ""
    for letter in file_cont:
        if letter in alphabet:
            position = alphabet.index(letter)
            if way == 0:
                new_position = position + shift
            elif way == 1:
                new_position = position - shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text


def ROT_13(way):
    global file_cont
    cipher_text = ""
    for letter in file_cont:
        if letter in alphabet:
            position = alphabet.index(letter)
            if way == 0:
                new_position = position + 13
            elif way == 1:
                new_position = position - 13
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text


window.mainloop()
