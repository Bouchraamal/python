import tkinter as tk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        
        # self.root.config(background='#3a8585')
        

        # Get the image dimensions
        img = tk.PhotoImage(file='SS.png')
        width = img.width()
        height = img.height()

        # Set window size to match image dimensions
        self.root.geometry(f"{width}x{height}")

        # Place the image on the window
        self.img_label = tk.Label(root, image=img)
        self.img_label.place(x=0, y=0, relwidth=1, relheight=1)
        

        self.frame = ctk.CTkFrame(root,width=400,height=400)
        self.frame.place(x=400, y=190)

        heading = ctk.CTkLabel(self.frame, text='Sign in', fg_color='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        self.user = ctk.CTkEntry(self.frame, fg_color='white', corner_radius=10, font=('Microsoft Yahei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', self.on_enter)
        self.user.bind('<FocusOut>', self.on_leave)

        self.password_entry = ctk.CTkEntry(self.frame, fg_color='white', corner_radius=10, font=('Microsoft Yahei UI Light', 11))
        self.password_entry.place(x=30, y=150)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind('<FocusIn>', self.on_enter_password)
        self.password_entry.bind('<FocusOut>', self.on_leave_password)

        ctk.CTkButton(self.frame, text='Sign in', fg_color='white', corner_radius=10, command=lambda: self.check_user_exists(self.user.get())).place(x=35, y=204)
        button2 = ctk.CTkButton(self.frame, text="Don't have an account?", fg_color="#b3aa5a",corner_radius=10, font=('Microsoft Yahei UI Light', 9),command=self.add_to_database)
        button2.place(x=105, y=270)

    def on_enter(self, e):
        self.user.delete(0, 'end')

    def on_leave(self, e):
        name = self.user.get()
        if name == '':
            self.user.insert(0, 'Username')

    def on_enter_password(self, e):
        self.password_entry.delete(0, 'end')

    def on_leave_password(self, e):
        name = self.password_entry.get()
        if name == '':
            self.password_entry.insert(0, 'Password')





    def check_user_exists(self, username):
            username = self.user.get()
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="test"
                )
                mycursor = mydb.cursor()

                # Exécutez la requête SQL pour vérifier si l'utilisateur existe déjà
                sql = "SELECT * FROM users WHERE username = %s"
                val = (username,)
                mycursor.execute(sql, val)

                user = mycursor.fetchone()  # Récupère la première ligne résultante

                mydb.close()

                if user:
                    self.root.withdraw()  # Cacher la fenêtre principale
                    screen = tk.Toplevel(root)
                    screen.geometry('1920x1080')
                    screen.title('my app')

                    def vegetables_page():
                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/tomate.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=80, y=40)
                        vegetables_frame.pack(pady=20)

                        #--------------------------------------------------
                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/green_peper.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((150, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=400, y=40)
                        vegetables_frame.pack(pady=20)
                        #---------------------------------------------------------

                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/carrot.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=700, y=40)
                        vegetables_frame.pack(pady=20)
                        #--------------------------------------------------

                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/red_peper.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=1000, y=40)
                        vegetables_frame.pack(pady=20)
                        #------------------------------------------------- 

                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/cauliflower.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=80, y=290)
                        vegetables_frame.pack(pady=20)
                        #---------------------------------------------------
                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/pumpkin.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=400, y=290)
                        vegetables_frame.pack(pady=20)
                        #---------------------------------------------------

                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/onion.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=700, y=290)
                        vegetables_frame.pack(pady=20)
                        #------------------------------------------------

                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/broccoli.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=1000, y=290)
                        vegetables_frame.pack(pady=20)
                        #-----------------------------------------------------*
                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/potato.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=80, y=550)
                        vegetables_frame.pack(pady=20)
                        #----------------------------------------------------

                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/garlic.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=400, y=550)
                        vegetables_frame.pack(pady=20)
                        #------------------------------------------------------
                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/eggplant.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=700, y=550)
                        vegetables_frame.pack(pady=20)
                        #----------------------------------------------------------

                        vegetables_frame = tk.Frame(main_frame)
                        image_path = 'vegetables/cucumber.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=1000, y=550)
                        vegetables_frame.pack(pady=20)


                    def fruits_page():
                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/mango.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=80, y=40)
                        fruits_frame.pack(pady=20)

                        #--------------------------------------------------
                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/watermelon.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((150, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=400, y=40)
                        fruits_frame.pack(pady=20)
                        #---------------------------------------------------------

                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/lemon.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=700, y=40)
                        fruits_frame.pack(pady=20)
                        #--------------------------------------------------

                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/strawberry.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=1000, y=40)
                        fruits_frame.pack(pady=20)
                        #------------------------------------------------- 

                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/kiwi.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=80, y=290)
                        fruits_frame.pack(pady=20)
                        #---------------------------------------------------
                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/orange.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=400, y=290)
                        fruits_frame.pack(pady=20)
                        #---------------------------------------------------

                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/apple.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=700, y=290)
                        fruits_frame.pack(pady=20)
                        #------------------------------------------------

                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/ananas.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=1000, y=290)
                        fruits_frame.pack(pady=20)
                        #-----------------------------------------------------*
                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/blueberry.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=80, y=550)
                        fruits_frame.pack(pady=20)
                        #----------------------------------------------------

                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/banane.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=400, y=550)
                        fruits_frame.pack(pady=20)
                        #------------------------------------------------------
                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/pear.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=700, y=550)
                        fruits_frame.pack(pady=20)
                        #----------------------------------------------------------

                        fruits_frame = tk.Frame(main_frame)
                        image_path = 'fruits/avocado.png'  # Replace 'raib.png' with your image path
                        image = Image.open(image_path)
                        resized_image = image.resize((130, 130))  # Resize the image
                        tk_image = ImageTk.PhotoImage(resized_image)  # Convert the resized image to a Tkinter-compatible format

                        image_label = tk.Label(main_frame, image=tk_image, bg=None)  # Display the resized image
                        image_label.image = tk_image  # Keep a reference to the image
                        image_label.place(x=1000, y=550)
                        fruits_frame.pack(pady=20)

                    def hide_indicators():
                        fruits_indicate.config(bg='#458DA2')
                        fruits_indicate.config(bg='#458DA2')
                        broxa_indicate.config(bg='#458DA2')
                        sabosa_indicate.config(bg='#458DA2')
                        madana_indicate.config(bg='#458DA2')
                        Liste_indicate.config(bg='#458DA2')

                    def delete_pages():
                        for  frame in main_frame.winfo_children():
                            frame.destroy()   

                        

                    def indicate(lb, page):

                        hide_indicators()
                        lb.config(bg='#D7D2CE')
                        delete_pages()

                        page()

                    options_frame=tk.Frame(screen , bg='#458DA2')

                    vegetables_btn=tk.Button(options_frame,text='Vegetables',font=('Bold',20),fg='#D7D2CE',bd=0,bg='#458DA2',command=lambda:  indicate(vegetables_indicate,vegetables_page))
                    vegetables_btn.place(x=50,y=50)
                    vegetables_indicate=tk.Label(options_frame,text='',bg='#458DA2')
                    vegetables_indicate.place(x=3,y=50,width=5 ,height=50 )

                    fruits_btn = tk.Button(options_frame,text='Fruits',font=('Bold',20),fg='#D7D2CE',bd=0,bg='#458DA2',command=lambda:  indicate(fruits_indicate,fruits_page))
                    fruits_btn.place(x=50,y=150)
                    fruits_indicate=tk.Label(options_frame,text='',bg='#458DA2')
                    fruits_indicate.place(x=3,y=150,width=5 ,height=50 )

                    broxa_btn = tk.Button(options_frame,text='broxa',font=('Bold',20),fg='#D7D2CE',bd=0,bg='#458DA2',command=lambda:  indicate(broxa_indicate))
                    broxa_btn.place(x=50,y=250)
                    broxa_indicate=tk.Label(options_frame,text='',bg='#458DA2')
                    broxa_indicate.place(x=3,y=250,width=5 ,height=50 )

                    sabosa_btn = tk.Button(options_frame,text='sabosa',font=('Bold',20),fg='#D7D2CE',bd=0,bg='#458DA2',command=lambda:  indicate(sabosa_indicate))
                    sabosa_btn.place(x=50,y=350)
                    sabosa_indicate=tk.Label(options_frame,text='',bg='#458DA2')
                    sabosa_indicate.place(x=3,y=350,width=5 ,height=50 )

                    madana_btn = tk.Button(options_frame,text='madana',font=('Bold',20),fg='#D7D2CE',bd=0,bg='#458DA2',command=lambda:  indicate(madana_indicate))
                    madana_btn.place(x=50,y=450)
                    madana_indicate=tk.Label(options_frame,text='',bg='#458DA2')
                    madana_indicate.place(x=3,y=450,width=5 ,height=50 )

                    Liste_btn = tk.Button(options_frame,text='Liste',font=('Bold',20),fg='#D7D2CE',bd=0,bg='#458DA2',command=lambda:  indicate(Liste_indicate))
                    Liste_btn.place(x=50,y=550)
                    Liste_indicate=tk.Label(options_frame,text='',bg='#458DA2')
                    Liste_indicate.place(x=3,y=550,width=5 ,height=50 )


                    options_frame.pack(side=tk.LEFT)
                    options_frame.pack_propagate(False)
                    options_frame.configure(width=250,height=900)

                    main_frame = tk.Frame(screen)

                    main_frame.pack(side=tk.LEFT)
                    main_frame.pack_propagate(False)
                    main_frame.configure (height=900,width=1300)

                    main_frame_image = tk.PhotoImage(file='SS.png')
                    

                    # Create a label inside main_frame to display the image
                    self.main_frame_image_label = tk.Label(main_frame, image=main_frame_image, bg='#458DA2')
                    self.main_frame_image_label.image = main_frame_image
                    self.main_frame_image_label.pack()

                    screen.mainloop()

                    tk.Label(screen, text='Bonjour', bg='gray', font=('sans serif', 50, 'bold')).pack(expand=tk.YES)

                    # Ajoutez un bouton pour fermer la fenêtre de bienvenue et afficher à nouveau la fenêtre principale
                    tk.Button(screen, text="Fermer", command=lambda: self.close_screen(screen)).pack()

                else:
                    messagebox.showerror("Error", "L'utilisateur n'existe pas !!")

            except mysql.connector.Error as error:
                print("Error connecting to MySQL:", error)
                return False

        # Fonction pour fermer la fenêtre de bienvenue et réafficher la fenêtre principale
            def close_screen(self, screen):
                screen.destroy()  # Fermer la fenêtre de bienvenue
                self.root.deiconify()  # Afficher à nouveau la fenêtre principale



    def add_to_database(self):
        username = self.user.get()
        password = self.password_entry.get()

        user_exists = self.check_user_exists(username)  # Vérifie si l'utilisateur existe déjà

        if user_exists:
            messagebox.showerror('Error', 'Username already exists!')
        else:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="test"
                )

                mycursor = mydb.cursor()

                sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
                val = (username, password)

                mycursor.execute(sql, val)

                mydb.commit()
                mydb.close()

                self.user.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                messagebox.showinfo("","Username and password saved to MySQL!")

            except mysql.connector.Error as error:
                print("Error connecting to MySQL:", error)
        

if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginApp(root)
    root.mainloop()