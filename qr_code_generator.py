import pyqrcode
from tkinter import *
from PIL import Image
import webbrowser


def generate():
    #user_url = input("Please enter a valid URL: ")
    user_url = user_input.get()
    url = pyqrcode.create(user_url)
    url.svg("qr_code.svg", scale=10)
    #print(url.terminal(quiet_zone=1))
    print_image()


def print_image():
    #img = Image.open("qr_code.svg")
    #img.show()
    img = "qr_code.svg"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(img)


window = Tk()
window.title("QR Code Generator with Python")
window.geometry("465x300")
welcome_label = Label(window, text="Welcome to this QR-Code Generator", font=("Arial", 20))
welcome_label.grid(column=0, row=0)
label = Label(window, text="Please enter a valid URL: ")
label.grid(column=0, row=1)
user_input = Entry(window, width=50)
user_input.grid(column=0, row=2)
button = Button(window, text="Generate QR-Code", command=generate)
button.grid(column=0, row=3)
window.mainloop()