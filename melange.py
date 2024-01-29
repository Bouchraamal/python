import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
import customtkinter 
from PIL import Image, ImageTk


class Categories(ctk.CTkFrame):
    def __init__(self, parent, show_main_callback):
        super().__init__(parent)
        
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

        # frame qui emporte les button des categories
        left_frame= customtkinter.CTkFrame(master=app,fg_color="#2D5A80")
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
        Liste_button = customtkinter.CTkButton(left_frame, text="My Liste", fg_color="#2D5A80", corner_radius=10, width=250,height=60,font= ("Arial", 20, "bold"))
        Liste_button.place(x=0, y=470)

        # Créez le bouton "vegetable" et placez-le dans le coin supérieur droit
        Service_button = customtkinter.CTkButton(left_frame, text="Services", fg_color="#2D5A80", corner_radius=10, width=250,height=60,font= ("Arial", 20, "bold"))
        Service_button.place(x=0, y=570)




        main_frame = tk.Frame(app)
        main_frame.configure(bg="#E4F4FF")  # Set the background color to white
        main_frame.pack(side="right", fill="both")  # Change "left" to "right"
        main_frame.pack_propagate(False)
        main_frame.configure(height=1400, width=1600)

        # frame pour l'affichage de l'interface des categories 
        # right_frame= customtkinter.CTkFrame(master=app,fg_color="#E4F4FF")
        # right_frame.configure (height=700,width=1080)
        # right_frame.pack(side="left",fill="both")

        
class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Main Interface')
        self.geometry("1920x1080")
        self.config(background='#E4F4FF')

        self.create_buttons()

    def create_buttons(self):
        # Load your icon images
        icon_categories = self.load_and_resize_image('categorie1.png', (80, 80))
        icon_my_list = self.load_and_resize_image('liste.png', (80, 80))
        icon_history = self.load_and_resize_image('historique.png', (80, 80))
        icon_statistique = self.load_and_resize_image('statistique2.png', (80, 80))

        # Specify the width and height of the button
        button_width = 300
        button_height = 300
        

        # Specify the font size and style
        button_font = ("Arial", 20, "bold")

        # 1st button
        button_categories = ctk.CTkButton(
            master=self,
            text="Categories",
            image=icon_categories,
            compound=ctk.TOP,
            width=button_width,
            height=button_height,
            corner_radius=15,
            font=button_font,
            fg_color="#2D5A80",
            command=self.show_categories_interface  # Call the function when the button is clicked
        )
        button_categories.place(relx=0.14, rely=0.65, anchor=ctk.CENTER)

        # 2nd button
        button_my_list = ctk.CTkButton(
            master=self,
            text="My List",
            image=icon_my_list,
            compound=ctk.TOP,
            width=button_width,
            height=button_height,
            corner_radius=15,
            font=button_font,
            fg_color="#2D5A80",
            command=self.show_my_list_interface  # Call the function when the button is clicked
        )
        button_my_list.place(relx=0.38, rely=0.65, anchor=ctk.CENTER)

        # 3rd button
        button_history_list = ctk.CTkButton(
            master=self,
            text="Historique des listes",
            image=icon_history,
            compound=ctk.TOP,
            width=button_width,
            height=button_height,
            corner_radius=15,
            font=button_font,
            fg_color="#2D5A80",
            command=self.show_history_interface  # Call the function when the button is clicked
        )
        button_history_list.place(relx=0.62, rely=0.65, anchor=ctk.CENTER)

        # 4th button
        button_history_list_2 = ctk.CTkButton(
            master=self,
            text="Statistique de courses",
            image=icon_statistique,
            compound=ctk.TOP,
            width=button_width,
            height=button_height,
            corner_radius=15,
            font=button_font,
            fg_color="#2D5A80",
            bg_color="#FFFFFF",
            command=self.show_statistics_interface  # Call the function when the button is clicked
        )
        button_history_list_2.place(relx=0.86, rely=0.65, anchor=ctk.CENTER)

    def load_and_resize_image(self, image_path, size):
        img = Image.open(image_path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)

    def show_categories_interface(self):
       # Effacez le contenu actuel
        self.create_buttons()

        # Ajoutez le contenu de ReadMoreContent à la fenêtre principale
        self.show_categories_interface_content = Categories(self, self.show_main)
        self.show_categories_interface_content.pack()
        

    def show_my_list_interface(self):
        # Implement your My List Interface here
        print("My List Interface")

    def show_history_interface(self):
        # Implement your History Interface here
        print("History Interface")

    def show_statistics_interface(self):
        # Implement your Statistics Interface here
        print("Statistics Interface")


    def show_main(self):
        # Effacez le contenu actuel
        if hasattr(self, 'show_categories_interface'):
            self.show_categories_interface_content.pack_forget()

        # Ajoutez le contenu initial à la fenêtre principale
        self.create_buttons.pack()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()