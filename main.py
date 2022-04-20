import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

new_alphabet = ['f', 'c', 'p', 'e', 'v', 'q', 'k', 'z', 'g', 'm', 't', 'r', 'a', 'y', 'o', 'n', 'u', 'j', 'd', 'l', 'w',
                'h', 'b', 'x', 's', 'i','f', 'c', 'p', 'e', 'v', 'q', 'k', 'z', 'g', 'm', 't', 'r', 'a', 'y', 'o', 'n',
                'u', 'j', 'd', 'l', 'w', 'h', 'b', 'x', 's', 'i']

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

upload_l = tk.Label(window, text='autorzy aplikacji: Bartłomiej Pniowski, Nikita Olchowski',
                    width=50, font=m_font, pady=100)
upload_l.grid(row=15, column=1)

shift = Spinbox(window, from_=1, to=100)
shift.grid(row=7, column=1)


v_list = ["Cypher", "ROT 13", "Arbitry"]
lista = ttk.Combobox(window, values=v_list)
lista.set("Wybierz szyfr")
lista['state'] = 'readonly'
lista.grid(row=3, column=1)


def upload_file():
    """Funckja otwiera okienko wyboru pliku o rozszerzeniu .txt z tekstem do kodowania/dekodowania
    następnie formatuje go i zapisuje do zmiennej globalnej file_cont"""
    file = filedialog.askopenfilename(filetypes=[("Plik tekstowy", '.txt')])
    fob = open(file, 'r')
    global file_cont
    file_cont = fob.read().lower()


def encode():
    """Funkcja pobiera informację o rodzaju wybranego szyfru i wywołująca odpowiednią funkcje kodującą"""
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
    elif lista.get() == "Arbitry":
        way = 0
        encode_text = Arbitry(way)
        save_cont = encode_text
        print(encode_text)


def decode():
    """Funkcja pobiera informację o rodzaju wybranego szyfru i wywołująca odpowiednią funkcje dekodującą"""
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
    elif lista.get() == "Arbitry":
        way = 1
        encode_text = Arbitry(way)
        save_cont = encode_text
        print(encode_text)


def save_file():
    """Funkcja pobiera tekst ze zmiennej save_cont, w której zapisany jest tekst po wyborze szyfru
    i opcji kodowania/dekodowania i zapisuje ją jako wybrany plik w formacie .txt"""
    fob = filedialog.asksaveasfile(filetypes=[("Plik tekstowy", '*.txt')], defaultextension='.txt', mode='w')
    fob.write(str(save_cont))
    fob.close()


def cypher(way, shift):
    """Funkcja szyfru Cezara. Pobiera argumenty 'way'- kierunek przesuwania liter alfabetu,
    'shift'- liczba oznaczająca o ile przesuwana jest litera po alfabecie. Funkcja zwraca 'cipher_text' czyli zakodowany
    lub zdekodowany tekst"""
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
    """Funkcja szyfru ROT13. Pobiera argumenty 'way'- kierunek przesuwania liter alfabetu.
    Funkcja zwraca 'cipher_text' czyli zakodowany lub zdekodowany tekst"""
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


def Arbitry(way):
    """Funkcja szyfru ROT13. Pobiera argumenty 'way'- kierunek przesuwania liter alfabetu.
    Funkcja zwraca 'cipher_text' czyli zakodowany lub zdekodowany zgodnie z przypisanym nowym porządkiem
    alfabetu tekst"""
    global file_cont
    cipher_text = ""
    for letter in file_cont:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_alphabet_position = new_alphabet.index(letter)
            if way == 0:
                new_position = position
                cipher_text += new_alphabet[new_position]
            elif way == 1:
                new_position = new_alphabet_position
                cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text

window.mainloop()


