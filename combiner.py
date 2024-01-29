import tkinter as tk
import customtkinter 
from PIL import Image, ImageTk



app = customtkinter.CTk()
app.geometry("1920x1080")
app.title("categories")
customtkinter.set_appearance_mode("system")
app.config(background='#E4F4FF')

app.resizable(width=True,height=True)


def create_image_label(frame, image_path, x, y, width=130, height=130):
    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    tk_image = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(frame, image=tk_image, bg="#E4F4FF")
    image_label.image = tk_image
    image_label.place(x=x, y=y)

def vegetables_page():
    create_image_label(main_frame, 'vegetables/tomate.png', 80, 70)
    create_image_label(main_frame, 'vegetables/green_peper.png', 500, 70, width=150)
    create_image_label(main_frame, 'vegetables/carrot.png', 900, 70)
    create_image_label(main_frame, 'vegetables/red_peper.png', 1300, 70)
    create_image_label(main_frame, 'vegetables/cauliflower.png', 80, 350)
    create_image_label(main_frame, 'vegetables/pumpkin.png', 500, 350)
    create_image_label(main_frame, 'vegetables/onion.png', 900, 350)
    create_image_label(main_frame, 'vegetables/broccoli.png', 1300, 350)
    create_image_label(main_frame, 'vegetables/potato.png', 80, 630)
    create_image_label(main_frame, 'vegetables/garlic.png', 500, 630)
    create_image_label(main_frame, 'vegetables/eggplant.png', 900, 630)
    create_image_label(main_frame, 'vegetables/cucumber.png', 1300, 630)

def fruits_page():
    create_image_label(main_frame, 'fruits/mango.png', 80, 70)
    create_image_label(main_frame, 'fruits/watermelon.png', 500, 70, width=150)
    create_image_label(main_frame, 'fruits/lemon.png', 900, 70)
    create_image_label(main_frame, 'fruits/strawberry.png', 1300, 70)
    create_image_label(main_frame, 'fruits/kiwi.png', 80, 350)
    create_image_label(main_frame, 'fruits/orange.png', 500, 350)
    create_image_label(main_frame, 'fruits/apple.png', 900, 350)
    create_image_label(main_frame, 'fruits/ananas.png', 1300, 350)
    create_image_label(main_frame, 'fruits/blueberry.png', 80, 630)
    create_image_label(main_frame, 'fruits/banane.png', 500, 630)
    create_image_label(main_frame, 'fruits/pear.png', 900, 630)
    create_image_label(main_frame, 'fruits/avocado.png', 1300, 630)

# Assuming main_frame is defined elsewhere in your code

def boisson_page():
    create_image_label(main_frame, 'boisson/andros.png', 80, 70, 130, 130)
    create_image_label(main_frame, 'boisson/bioitalia.png', 500, 70, 150, 130)
    create_image_label(main_frame, 'boisson/lemonade.png', 900, 70, 130, 130)
    create_image_label(main_frame, 'boisson/Power_Horse.png', 1300, 70, 150, 150)
    create_image_label(main_frame, 'boisson/lipton.png', 80, 350, 130, 130)
    create_image_label(main_frame, 'boisson/monster.png', 500, 350, 130, 130)
    create_image_label(main_frame, 'boisson/preeme.png', 900, 350, 130, 130)
    create_image_label(main_frame, 'boisson/redbull.png', 1300, 350, 130, 130)
    create_image_label(main_frame, 'boisson/sprite.png', 80, 630, 140, 140)
    create_image_label(main_frame, 'boisson/valencia.png', 500, 630, 140, 140)
    create_image_label(main_frame, 'boisson/tropicana.png', 900, 630, 130, 130)
    create_image_label(main_frame, 'boisson/vimto.png', 1300, 630, 130, 130)

def snacks_page():
    create_image_label(main_frame, 'snacks/lay_s.png', 80, 70, 130, 130)
    create_image_label(main_frame, 'snacks/doritos.png', 500, 70, 150, 130)
    create_image_label(main_frame, 'snacks/pringels.png', 900, 70, 130, 130)
    create_image_label(main_frame, 'snacks/kitkat.png', 1300, 70, 130, 130)
    create_image_label(main_frame, 'snacks/nestel_Crunch.png', 80, 350, 130, 130)
    create_image_label(main_frame, 'snacks/snickers.png', 500, 350, 130, 130)
    create_image_label(main_frame, 'snacks/ritz.png', 900, 350, 130, 130)
    create_image_label(main_frame, 'snacks/milka.png', 1300, 350, 130, 130)
    create_image_label(main_frame, 'snacks/diary_milk.png', 80, 630, 130, 130)
    create_image_label(main_frame, 'snacks/skittles.png', 500, 630, 130, 130)
    create_image_label(main_frame, 'snacks/nerds.png', 900, 630, 130, 130)
    create_image_label(main_frame, 'snacks/m&m.png', 1300, 630, 130, 130)

def hide_indicators():
    vegetables_indicate.config(bg='#458DA2')
    fruits_indicate.config(bg='#458DA2')
    boisson_indicate.config(bg='#458DA2')
    snacks_indicate.config(bg='#458DA2')

def delete_pages():
    for widget in main_frame.winfo_children():
        widget.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#E4F4FF')
    delete_pages()
    page()

left_frame = tk.Frame(app, bg="#2D5A80")
left_frame.configure(width=255, height=700)
left_frame.pack(side="left", fill="both")

vegetables_button = tk.Button(left_frame, text="Vegetables", bg="#2D5A80", fg="white", width=20, height=2, font=("Arial", 12, "bold"), command=lambda: indicate(vegetables_indicate, vegetables_page))
vegetables_button.place(x=0, y=70)
vegetables_indicate = tk.Label(left_frame, bg='#458DA2', width=5, height=4)
vegetables_indicate.place(x=3, y=115)

fruits_button = tk.Button(left_frame, text="Fruits", bg="#2D5A80", fg="white", width=20, height=2, font=("Arial", 12, "bold"), command=lambda: indicate(fruits_indicate, fruits_page))
fruits_button.place(x=0, y=170)
fruits_indicate = tk.Label(left_frame, bg='#458DA2', width=5, height=4)
fruits_indicate.place(x=3, y=220)

boisson_button = tk.Button(left_frame, text="Boisson", bg="#2D5A80", fg="white", width=20, height=2, font=("Arial", 12, "bold"), command=lambda: indicate(boisson_indicate, boisson_page))
boisson_button.place(x=0, y=270)
boisson_indicate = tk.Label(left_frame, bg='#458DA2', width=5, height=3)
boisson_indicate.place(x=3, y=320)

snacks_button = tk.Button(left_frame, text="Snacks", bg="#2D5A80", fg="white", width=20, height=2, font=("Arial", 12, "bold"), command=lambda: indicate(snacks_indicate, snacks_page))
snacks_button.place(x=0, y=370)
snacks_indicate = tk.Label(left_frame, bg='#458DA2', width=5, height=3)
snacks_indicate.place(x=3, y=420)

Liste_button = tk.Button(left_frame, text="My Liste", bg="#2D5A80", fg="white", width=20, height=2, font=("Arial", 12, "bold"))
Liste_button.place(x=0, y=470)

Service_button = tk.Button(left_frame, text="Services", bg="#2D5A80", fg="white", width=20, height=2, font=("Arial", 12, "bold"))
Service_button.place(x=0, y=570)

main_frame = tk.Frame(app, bg="#E4F4FF")
main_frame.pack(side="right", fill="both")
main_frame.pack_propagate(False)
main_frame.configure(height=1400, width=1600)

app.mainloop()