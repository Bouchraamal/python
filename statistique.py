import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


donnees_produits = {"pomme": 50, "jus d'orange": 30, "potato": 70, "kitkat": 40}
donnees_listes = {"Liste 1": 500, "Liste 2": 600, "Liste 3": 700, "Liste 4": 800}
                  
app = ctk.CTk()
app.geometry("1920x1080")
app.title("categories")
ctk.set_appearance_mode("system")
app.config(background='#E4F4FF')
app.resizable(width=True, height=True)

def afficher_diagramme_produits():
    # Displaying the image
    img = Image.open('desc11.png')
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(main_frame, image=photo)
    image_label.image = photo  # This line keeps a reference to the image to prevent it from being garbage collected
    image_label.place(x=0,y=0)

    # Plotting the bar chart
    categories = list(donnees_produits.keys())
    quantites = list(donnees_produits.values())
    
    fig, ax = plt.subplots()
    ax.bar(categories, quantites, color="#6b9033")
    ax.set_title("Produits les plus consommés")
    ax.set_xlabel("les produits")
    ax.set_ylabel("Quantité consommée")
    
    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()
    canvas.get_tk_widget().place(x=470,y=370)

def afficher_diagramme_listes():
    # Displaying the image
    img = Image.open('desc222.png')
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(main_frame, image=photo)
    image_label.image = photo  # Keeping a reference to the image
    image_label.place(x=0,y=0)
     
    # Plotting the bar chart
    listes = list(donnees_listes.keys())
    montants = list(donnees_listes.values())
    
    fig, ax = plt.subplots()
    ax.bar(listes, montants, color="#6b9033")
    ax.set_title("Montant dépensé par liste")
    ax.set_xlabel("Liste")
    ax.set_ylabel("Montant (en DH)")
    ax.tick_params(axis='x', rotation=45)
    
    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()
    canvas.get_tk_widget().place(x=470,y=370)



def delete_pages():
    for widget in main_frame.winfo_children():
        widget.destroy()

def indicate(page):
    delete_pages()
    page()

left_frame = ctk.CTkFrame(master=app, fg_color="#2D5A80")
left_frame.configure(width=255, height=700)
left_frame.pack(side="left", fill="both")

titre_label = ctk.CTkLabel(left_frame, text="Track Your Listes !", fg_color="#2D5A80", font=("Arial", 25, "bold"))
titre_label.place(x=10,y=70)

produits = ctk.CTkButton(left_frame, text="Digram Products", fg_color="#2D5A80", corner_radius=10, width=250, height=60, font=("Arial", 20, "bold"), command=lambda: indicate(afficher_diagramme_produits))
produits.place(x=0, y=220)

listes = ctk.CTkButton(left_frame, text="Digram Listes", fg_color="#2D5A80", corner_radius=10, width=250, height=60, font=("Arial", 20, "bold"), command=lambda: indicate(afficher_diagramme_listes))
listes.place(x=0, y=300)

home_button = ctk.CTkButton(left_frame, text="Back", fg_color="#2D5A80", corner_radius=10, width=250, height=60, font=("Arial", 20, "bold"))
home_button.place(x=0, y=670)

main_frame = tk.Frame(app)
main_frame.configure(bg="#FFFFFF")
main_frame.pack(side="right", fill="both")
main_frame.pack_propagate(False)
main_frame.configure(height=1400, width=1600)






app.mainloop()