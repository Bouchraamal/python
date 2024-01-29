import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3
import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt




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

class ReadMoreContent(ctk.CTkFrame):
    def __init__(self, parent, show_main_callback):
        super().__init__(parent)
        # Chargez l'image
        img = Image.open('R2.png')
        self.photo = ImageTk.PhotoImage(img)

        # Créez et placez l'étiquette de l'image
        image_label = tk.Label(self, image=self.photo)
        image_label.place(x=0, y=0)
        image_label.pack()

        # Créez le bouton "Home" pour revenir à l'interface principale
        home_button = ctk.CTkButton(self, text="Home", command=show_main_callback, bg_color="#E4F4FF", fg_color="#E9766D", corner_radius=10)
        home_button.place(x=1100, y=600)

class LoginContent(ctk.CTkFrame):
    def __init__(self, parent, show_main_callback):
        super().__init__(parent)

        # Intégrez l'interface de connexion dans cette partie du code
        login_interface = LoginInterface(self, show_main_callback)
        login_interface.pack()


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

        self.username_entry = ctk.CTkEntry(self, font=("Arial", 14), width=150, fg_color="#D2DBCB")
        self.username_entry.place(x=570, y=320)

        self.password_entry = ctk.CTkEntry(self, font=("Arial", 14), width=150, show="*", fg_color="#D2DBCB")
        self.password_entry.place(x=570, y=380)

        # Créez le bouton "Se connecter" avec la fonctionnalité associée
        login_button = ctk.CTkButton(self, text="Se connecter", font=("Gras", 17),command=self.authenticate_user, bg_color="#D2DBCB", fg_color="#D2DBCB", corner_radius=10)
        login_button.place(x=570, y=460)
         # Créez le bouton "Home" pour revenir à l'interface principale
        home_button = ctk.CTkButton(self, text="Home", font=("Gras", 17),command=show_main_callback, bg_color="#D2DBCB", fg_color="#D2DBCB", corner_radius=10)
        home_button.place(x=570, y=500)

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
            self.show_authenticated_interface()
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")

    def show_authenticated_interface(self):
    # Hide the current login interface
        self.pack_forget()

        # Create and display the new authenticated interface
        authenticated_interface = AuthenticatedInterface(self.master)
        authenticated_interface.pack()




# page de diagramme 
donnees_produits = {"pomme": 50, "jus d'orange": 30, "potato": 70, "kitkat": 40}
donnees_listes = {"Liste 1": 500, "Liste 2": 600, "Liste 3": 700, "Liste 4": 800}
class  DiagrammeInterface(customtkinter.CTkFrame):
    def __init__(self, parent,show_main_callback):
        super().__init__(parent)
        self.main_frame = ctk.CTkFrame(self, width=1920, height=1080)
        self.main_frame.configure(bg_color="red")
        self.main_frame.pack()

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
            ax.bar(categories, quantites)
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
            ax.bar(listes, montants)
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

        left_frame = ctk.CTkFrame(master=self.main_frame, fg_color="#2D5A80")
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


        
        main_frame = tk.Frame(self.main_frame)
        main_frame.configure(bg="#FFFFFF")
        main_frame.pack(side="right", fill="both")
        main_frame.pack_propagate(False)
        main_frame.configure(height=1400, width=1600)






class CategoriesInterface(customtkinter.CTkFrame):
    def __init__(self, parent,show_authenticated_interface):
        super().__init__(parent)

        
        initial_image_path = 'cate_page.png'  # Chemin de votre image initiale
        initial_image = Image.open(initial_image_path)
        initial_image = initial_image.resize((width, height))  # Ajustez la taille si nécessaire
        initial_tk_image = ImageTk.PhotoImage(initial_image)

        # Créer et afficher une étiquette pour l'image initiale
        initial_image_label = tk.Label(self.main_frame, image=initial_tk_image)
        initial_image_label.image = initial_tk_image  # Garder une référence à l'image pour éviter la collecte de déchets
        initial_image_label.pack()

        self.main_frame = ctk.CTkFrame(self, width=1920, height=1080)
        self.main_frame.configure(bg_color="red")
        self.main_frame.pack()

        # Définir la taille de l'image initiale
        width = 500
        height = 500

        def vegetables_page():
            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/tomate.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=70)
            vegetables_frame.pack(pady=20)

            #--------------------------------------------------
            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/green_peper.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((150, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=70)
            vegetables_frame.pack(pady=20)
            #---------------------------------------------------------

            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/carrot.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=70)
            vegetables_frame.pack(pady=20)
            #--------------------------------------------------

            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/red_peper.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=70)
            vegetables_frame.pack(pady=20)
            #------------------------------------------------- 

            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/cauliflower.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=350)
            vegetables_frame.pack(pady=20)
            #---------------------------------------------------
            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/pumpkin.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=350)
            vegetables_frame.pack(pady=20)
            #---------------------------------------------------

            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/onion.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=350)
            vegetables_frame.pack(pady=20)
            #------------------------------------------------

            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/broccoli.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=350)
            vegetables_frame.pack(pady=20)
            #-----------------------------------------------------*
            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/potato.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=630)
            vegetables_frame.pack(pady=20)
            #----------------------------------------------------

            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/garlic.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=630)
            vegetables_frame.pack(pady=20)
            #------------------------------------------------------
            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/eggplant.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=630)
            vegetables_frame.pack(pady=20)
            #----------------------------------------------------------

            vegetables_frame = tk.Frame(main_frame)
            image_path = 'vegetables/cucumber.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=630)
            vegetables_frame.pack(pady=20)

        def fruits_page():
            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/mango.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=70)
            fruits_frame.pack(pady=20)

            #--------------------------------------------------
            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/watermelon.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((150, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=70)
            fruits_frame.pack(pady=20)
            #---------------------------------------------------------

            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/lemon.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=70)
            fruits_frame.pack(pady=20)
            #--------------------------------------------------

            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/strawberry.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=70)
            fruits_frame.pack(pady=20)
            #------------------------------------------------- 

            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/kiwi.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=350)
            fruits_frame.pack(pady=20)
            #---------------------------------------------------
            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/orange.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=350)
            fruits_frame.pack(pady=20)
            #---------------------------------------------------

            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/apple.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=350)
            fruits_frame.pack(pady=20)
            #------------------------------------------------

            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/ananas.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=350)
            fruits_frame.pack(pady=20)
            #-----------------------------------------------------*
            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/blueberry.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=630)
            fruits_frame.pack(pady=20)
            #----------------------------------------------------

            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/banane.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=630)
            fruits_frame.pack(pady=20)
            #------------------------------------------------------
            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/pear.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=630)
            fruits_frame.pack(pady=20)
            #----------------------------------------------------------

            fruits_frame = tk.Frame(main_frame)
            image_path = 'fruits/avocado.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=630)
            fruits_frame.pack(pady=20)
        def boisson_page():
            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/andros.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=70)
            boisson_frame.pack(pady=20)
            
            #--------------------------------------------------
            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/bioitalia.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((150, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=70)
            boisson_frame.pack(pady=20)
            #---------------------------------------------------------

            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/lemonade.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=70)
            boisson_frame.pack(pady=20)
            #--------------------------------------------------

            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/Power_Horse.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((150, 150))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=70)
            boisson_frame.pack(pady=20)
            #------------------------------------------------- 

            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/lipton.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=350)
            boisson_frame.pack(pady=20)
            #---------------------------------------------------
            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/monster.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=350)
            boisson_frame.pack(pady=20)
            #---------------------------------------------------

            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/preeme.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=350)
            boisson_frame.pack(pady=20)
            #------------------------------------------------

            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/redbull.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=350)
            boisson_frame.pack(pady=20)
            #-----------------------------------------------------*
            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/sprite.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((140, 140))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=630)
            boisson_frame.pack(pady=30)
            #----------------------------------------------------

            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/valencia.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((140, 140))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=630)
            boisson_frame.pack(pady=20)
            #------------------------------------------------------
            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/tropicana.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=630)
            boisson_frame.pack(pady=20)
            #----------------------------------------------------------

            boisson_frame = tk.Frame(main_frame)
            image_path = 'boisson/vimto.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=630)
            boisson_frame.pack(pady=20)

        def Snacks_page():
            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/lay_s.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=70)
            snacks_frame.pack(pady=20)

            #--------------------------------------------------
            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/doritos.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((150, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=70)
            snacks_frame.pack(pady=20)
            #---------------------------------------------------------

            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/pringels.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=70)
            snacks_frame.pack(pady=20)
            #--------------------------------------------------

            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/kitkat.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=70)
            snacks_frame.pack(pady=20)
            #------------------------------------------------- 

            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/nestel_Crunch.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=350)
            snacks_frame.pack(pady=20)
            #---------------------------------------------------
            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/snickers.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=350)
            snacks_frame.pack(pady=20)
            #---------------------------------------------------

            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/ritz.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=350)
            snacks_frame.pack(pady=20)
            #------------------------------------------------

            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/milka.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=350)
            snacks_frame.pack(pady=20)
            #-----------------------------------------------------*
            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/diary_milk.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=80, y=630)
            snacks_frame.pack(pady=20)
            #----------------------------------------------------

            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/skittles.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=500, y=630)
            snacks_frame.pack(pady=20)
            #------------------------------------------------------
            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/nerds.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=900, y=630)
            snacks_frame.pack(pady=20)
            #----------------------------------------------------------

            snacks_frame = tk.Frame(main_frame)
            image_path = 'snacks/m&m.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            resized_image = image.resize((130, 130))  # Resize the image
            tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.place(x=1300, y=630)
            snacks_frame.pack(pady=20)


        def show_liste():
            liste_frame = tk.Frame(main_frame)
            image_path = 'L.png'  # Replace 'raib.png' with your image path
            image = Image.open(image_path)
            tk_image = ImageTk.PhotoImage(image)  # Convert the resized image to a Tkinter-compatible format

            image_label = tk.Label(main_frame, image=tk_image, bg="#E4F4FF")  # Display the resized image
            image_label.image = tk_image  # Keep a reference to the image
            image_label.pack()
            liste_frame.pack()

            budget_entry = ctk.CTkEntry(self, font=("Arial", 14), width=150,height=30, fg_color="#D2DBCB")
            budget_entry.place(x=1030, y=570)

            paiment_entry = ctk.CTkEntry(self, font=("Arial", 14), width=150, height=30 ,show="*", fg_color="#D2DBCB")
            paiment_entry.place(x=1030, y=680)

            # Créez le bouton "Se connecter" avec la fonctionnalité associée
            payer_button = ctk.CTkButton(self, text="payer", font=("Gras", 17), bg_color="#D2DBCB", fg_color="#D2DBCB", corner_radius=10)
            payer_button.place(x=1030, y=750)
            # Créez le bouton "Home" pour revenir à l'interface principale
        

            

        def hide_indicators():
            vegetables_indicate.config(bg='#458DA2')
            fruits_indicate.config(bg='#458DA2')
            boisson_indicate.config(bg='#458DA2')
            snacks_indicate.config(bg='#458DA2')

        def delete_pages():
            for frame in main_frame.winfo_children():
                frame.destroy()
        def indicate(lb, page):
            hide_indicators()
            lb.config(bg='#E4F4FF')
            delete_pages()

            page()

        def show_authenticated_interface(self):
    

            # Create and display the new authenticated interface
            authenticated_interface = AuthenticatedInterface(self)
            authenticated_interface.pack()




    

        # frame qui emporte les button des categories
        left_frame= customtkinter.CTkFrame(master=self.main_frame,fg_color="#2D5A80")
        left_frame.configure(width=255,height=700)
        left_frame.pack(side="left",fill="both")



        # Créez le bouton "vegetable" et placez-le dans le coin supérieur droit
        vegetables_button = customtkinter.CTkButton(left_frame, text="Vegetables", fg_color="#2D5A80", corner_radius=10, width=250,height=60,font= ("Arial", 20, "bold"),command=lambda:  indicate(vegetables_indicate,vegetables_page))
        vegetables_button.place(x=0, y=70)
        vegetables_indicate=tk.Label(left_frame,text='',bg='#458DA2')
        vegetables_indicate.place(x=3,y=115,width=5 ,height=70 )


        # Créez le bouton "vegetable" et placez-le dans le coin supérieur droit
        fruits_button = customtkinter.CTkButton(left_frame, text="Fruits", fg_color="#2D5A80", corner_radius=10, width=250,height=60,font= ("Arial", 20, "bold"),command=lambda:  indicate(fruits_indicate,fruits_page))
        fruits_button.place(x=0, y=170)
        fruits_indicate=tk.Label(left_frame,text='',bg='#458DA2')
        fruits_indicate.place(x=3,y=115,width=5 ,height=70 )

        # Créez le bouton "vegetable" et placez-le dans le coin supérieur droit
        boisson_button = customtkinter.CTkButton(left_frame, text="Boisson", fg_color="#2D5A80", corner_radius=10, width=250,height=60,font= ("Arial", 20, "bold"),command=lambda:  indicate(boisson_indicate,boisson_page))
        boisson_button.place(x=0, y=270)
        boisson_indicate=tk.Label(left_frame,text='',bg='#458DA2')
        boisson_indicate.place(x=3,y=250,width=5 ,height=50 )

        # Créez le bouton "vegetable" et placez-le dans le coin supérieur droit
        snacks_button = customtkinter.CTkButton(left_frame, text="Snacks", fg_color="#2D5A80", corner_radius=10, width=250,height=60,font= ("Arial", 20, "bold"),command=lambda:  indicate(snacks_indicate,Snacks_page))
        snacks_button.place(x=0, y=370)
        snacks_indicate=tk.Label(left_frame,text='',bg='#458DA2')
        snacks_indicate.place(x=3,y=250,width=5 ,height=50 )
        # Créez le bouton "vegetable" et placez-le dans le coin supérieur droit
        Liste_button = customtkinter.CTkButton(left_frame, text="My Liste", fg_color="#2D5A80", corner_radius=10, width=250,height=60,font= ("Arial", 20, "bold"), command=lambda: show_liste())
        Liste_button.place(x=0, y=470)
        
    
        self.show_authenticated_interface = show_authenticated_interface
        # Créez le bouton "vegetable" et placez-le dans le coin supérieur droit
        Service_button = customtkinter.CTkButton(left_frame, text="Services", fg_color="#2D5A80", corner_radius=10, width=250,height=60,font= ("Arial", 20, "bold") , command=self.show_authenticated_interface)
        Service_button.place(x=0, y=570)


        main_frame = tk.Frame(self.main_frame)
        main_frame.configure(bg="#FFFFFF")  # Set the background color to white
        main_frame.pack(side="right", fill="both")  # Change "left" to "right"
        main_frame.pack_propagate(False)
        main_frame.configure(height=1400, width=1600)

        
            
            

        
    #     self.show_main_callback = show_main_callback
    #     self.create_widgets()

    # def create_widgets(self):
    #     # Ajoutez le code pour créer les éléments de votre interface ici
    #     # Par exemple, un bouton dans la nouvelle interface
        # back_button = customtkinter.CTkButton(
        #     self, text="Back to Home", command=self.show_authenticated_interface, 
        #     bg_color="#FFFFFF", fg_color="#E9766D", corner_radius=10
        # )
        # back_button.place(x=20, y=20)

        # Ajoutez d'autres éléments comme des étiquettes, des boutons, etc.

class AuthenticatedInterface(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        header_image = self.load_and_resize_image('login.png', (1400, 350))
        
        # Créez la frame principale
        self.main_frame = ctk.CTkFrame(self, width=1920, height=1080)
        self.main_frame.configure(fg_color="#FFFFFF")
        self.main_frame.pack()
       
        header_label = ctk.CTkLabel(
        master=self.main_frame,
        image=header_image,
        text="",
        compound=ctk.TOP
        )
        header_label.place(relx=0.5, rely=0.04, anchor=ctk.N)

       
        
        # Load your icon images
        icon_categories = self.load_and_resize_image('basket.png', (100, 100))
        icon_my_list = self.load_and_resize_image('liste.png', (100, 100))
        icon_history = self.load_and_resize_image('historiques.png', (100, 100))
        icon_statistique = self.load_and_resize_image('statistiques.png', (100, 100))

        # Specify the width and height of the button
        button_width = 270
        button_height = 300

        # Specify the font size and style
        button_font = ("Arial", 20, "bold")

        # 1st button
        button_categories = ctk.CTkButton(
            master=self.main_frame,
            text="Categories",
            image=icon_categories,
            compound=ctk.TOP,
            width=button_width,
            height=button_height,
            font=button_font,
            fg_color="#C8D4BF",
            command=self.show_categories_interface
        )
        button_categories.place(relx=0.14, rely=0.67, anchor=ctk.CENTER)

        # 2nd button
        button_my_list = ctk.CTkButton(
            master=self.main_frame,
            text="My List",
            image=icon_my_list,
            compound=ctk.TOP,
            width=button_width,
            height=button_height,
            font=button_font,
            fg_color="#A8C199",
            command=self.show_my_list_interface
        )
        button_my_list.place(relx=0.38, rely=0.67, anchor=ctk.CENTER)

        # 3rd button
        button_history_list = ctk.CTkButton(
            master=self.main_frame,
            text="Historique des listes",
            image=icon_history,
            compound=ctk.TOP,
            width=button_width,
            height=button_height,
            font=button_font,
            fg_color="#96AD87",
            command=self.show_history_interface
        )
        button_history_list.place(relx=0.62, rely=0.67, anchor=ctk.CENTER)

        # 4th button
        button_history_list_2 = ctk.CTkButton(
            master=self.main_frame,
            text="Statistique de courses",
            image=icon_statistique,
            compound=ctk.TOP,
            width=button_width,
            height=button_height,
            font=button_font,
            fg_color="#7A8F6D",
            command=self.show_statistics_interface
        )
        button_history_list_2.place(relx=0.86, rely=0.67, anchor=ctk.CENTER)

    def load_and_resize_image(self, image_path, size):
        img = Image.open(image_path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)

    def show_categories_interface(self):
        self.main_frame.pack_forget()
        self.categories_interface = CategoriesInterface(self, self.show_main2)
        self.categories_interface.pack()

    def show_my_list_interface(self):
        print("My List Interface")

    def show_history_interface(self):
        print("History Interface")

    def show_statistics_interface(self):
        self.main_frame.pack_forget()
        self.diagramme_interface = DiagrammeInterface(self, self.show_main2)
        self.diagramme_interface.pack()

    def show_main2(self):
        if hasattr(self, 'categories_interface'):
            self.categories_interface.pack_forget()
        if hasattr(self, 'diagramme_interface'):
            self.diagramme_interface.pack_forget()

        # Add the initial content to the main window
        self.main_frame.pack()


# class CategoriesInterface(ctk.CTkToplevel):
#     def _init_(self, parent):
#         super()._init_(parent)
#         self.title('Categories Interface')
#         self.create_widgets()

#     def create_widgets(self):
#         button_in_categories_interface = ctk.CTkButton(
#             master=self,
#             text="Button in Categories Interface",
#             command=self.button_in_categories_interface_clicked
#         )
#         button_in_categories_interface.pack()

#     def button_in_categories_interface_clicked(self):
#         print("Button in Categories Interface Clicked")


# ... (similar classes for other interfaces)

    # Define other methods for the authenticated interface as needed


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()