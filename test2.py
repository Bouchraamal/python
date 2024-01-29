import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3

# Créer une base de données SQLite pour stocker les informations d'identification
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Créer une table 'user' pour stocker les informations d'identification
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Ajouter un utilisateur à la table (exemple, veuillez remplacer par vos propres données)
cursor.execute('INSERT INTO user (username, password) VALUES (?, ?)', ('safaa', '123'))
conn.commit()

class LoginInterface(ctk.CTkFrame):
    def __init__(self, parent, show_main_callback):
        super().__init__(parent)

        # Chargez l'image d'arrière-plan
        img = Image.open('Login.png')
        self.photo = ImageTk.PhotoImage(img)

        # Créez et placez l'étiquette de l'image d'arrière-plan
        background_label = tk.Label(self, image=self.photo)
        background_label.place(x=0, y=0)
        background_label.pack()

        # Créez les labels et les champs de saisie pour le nom d'utilisateur et le mot de passe
       



        self.username_entry = ctk.CTkEntry(self, font=("Arial", 14), width=180)
        self.username_entry.place(x=520, y=300)

        self.password_entry = ctk.CTkEntry(self, font=("Arial", 14), width=180, show="*")
        self.password_entry.place(x=520, y=390)

        # Créez le bouton "Se connecter" avec la fonctionnalité associée
        login_button = ctk.CTkButton(self, text="Se connecter", command=self.authenticate_user, bg_color="#FFFFFF", fg_color="#E9766D", corner_radius=10)
        login_button.place(x=600, y=460)

    def authenticate_user(self):
        # Récupérez les informations saisies par l'utilisateur
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        # Vérifiez les informations d'identification dans la base de données
        cursor.execute('SELECT * FROM user WHERE username=? AND password=?', (entered_username, entered_password))
        user_data = cursor.fetchone()

        if user_data:
            print("Authentification réussie!")
            # Affichez une nouvelle interface ou effectuez d'autres actions après une authentification réussie
            # Ici, nous allons simplement imprimer un message pour l'exemple
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")

class ReadMoreContent(ctk.CTkFrame):
    def __init__(self, parent, show_main_callback):
        super().__init__(parent)
        # Chargez l'image
        img = Image.open('about_app.png')
        self.photo = ImageTk.PhotoImage(img)

        # Créez et placez l'étiquette de l'image
        image_label = tk.Label(self, image=self.photo)
        image_label.place(x=0, y=0)
        image_label.pack()

        # Créez le bouton "Home" pour revenir à l'interface principale
        home_button = ctk.CTkButton(self, text="Home", command=show_main_callback, bg_color="#E4F4FF", fg_color="#E9766D", corner_radius=10)
        home_button.place(x=900, y=720)

class LoginContent(ctk.CTkFrame):
    def __init__(self, parent, show_main_callback):
        super().__init__(parent)

        # Intégrez l'interface de connexion dans cette partie du code
        login_interface = LoginInterface(self, show_main_callback)
        login_interface.pack()

        # Créez le bouton "Home" pour revenir à l'interface principale
        home_button = ctk.CTkButton(self, text="Home", command=show_main_callback, bg_color="#FFFFFF", fg_color="#E9766D", corner_radius=10)
        home_button.place(x=600, y=500)

# Interface principale home
class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('GroceryFlow')
        self.geometry("1920x1080")

        # Chargez l'image
        img = Image.open('inter4.png')
        self.photo = ImageTk.PhotoImage(img)

        # Créez et placez l'étiquette de l'image
        self.image_label = tk.Label(self, image=self.photo)
        self.image_label.place(x=0, y=0)
        self.image_label.pack()

        # Créez le bouton "Read More" et placez-le dans le coin supérieur gauche
        read_more_button = ctk.CTkButton(self, text="Read More", command=self.show_read_more, bg_color="#FFFFFF", fg_color="#E9766D", corner_radius=10)
        read_more_button.place(x=20, y=40)

        # Créez le bouton "Log in" et placez-le dans le coin supérieur droit
        login_button = ctk.CTkButton(self, text="Log in", command=self.show_login, bg_color="#FFFFFF", fg_color="#E9766D", corner_radius=10)
        login_button.place(x=20, y=70)

    def show_read_more(self):
        # Effacez le contenu actuel
        self.image_label.pack_forget()

        # Ajoutez le contenu de ReadMoreContent à la fenêtre principale
        self.read_more_content = ReadMoreContent(self, self.show_main)
        self.read_more_content.pack()

    def show_login(self):
        # Effacez le contenu actuel
        self.image_label.pack_forget()

        # Ajoutez le contenu de LoginContent à la fenêtre principale
        self.login_content = LoginContent(self, self.show_main)
        self.login_content.pack()

    def show_main(self):
        # Effacez le contenu actuel
        if hasattr(self, 'read_more_content'):
            self.read_more_content.pack_forget()
        if hasattr(self, 'login_content'):
            self.login_content.pack_forget()

        # Ajoutez le contenu initial à la fenêtre principale
        self.image_label.pack()

if __name__ == "__main__":
    Window = MainApplication()
    Window.mainloop()

# Fermez la connexion à la base de données lorsqu'il n'est plus nécessaire
conn.close()