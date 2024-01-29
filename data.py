import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error
import customtkinter

class MyApp:
    def __init__(self, root):
        self.root = root
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database_name = "python1"
        self.connection = None
        self.cursor = None

        self.setup_database()
        self.product_quantities = {}


    def setup_database(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database_name
            )
            if self.connection.is_connected():
                print("Connected to the database")
                self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error: {e}")

    def fetch_product_info(self, item):
        # Fetch product information from the database based on the item
        query = "SELECT * FROM product WHERE name = %s"
        self.cursor.execute(query, (item,))
        result = self.cursor.fetchone()

        # Check if the product was found
        if result:
            return result  # Assuming result is a tuple with product information
        else:
            print(f"Product '{item}' not found in the database.")
            return None    

    def buy_product(self, item):
        product_info = self.fetch_product_info(item)
        if product_info:
            print(f"Buy button clicked for {item}. Product info: {product_info}")

            # Calculate total price for the bought product
            total_price = self.product_quantities.get(item, 0) * product_info[2]  # Assuming price is at index 2
            print(f"Total price for {item}: {total_price}")

            # Add the bought product to the list
            if item in self.product_quantities and self.product_quantities[item] > 0:
                bought_products.append({
                    "item": item,
                    "quantity": self.product_quantities[item],
                    "total_price": total_price
                })
                print(f"Quantity of {item} in the cart: {self.product_quantities[item]}")
            else:
                print(f"Cannot add '{item}' to the cart. Quantity is 0.")
        else:
            print(f"Cannot buy '{item}'. Product information not available.")


    def increase_quantity(self, item):
        self.product_quantities[item] = self.product_quantities.get(item, 0) + 1
        print(f"Quantity of {item} increased to {self.product_quantities[item]}")


    def decrease_quantity(self, item):
        if item in self.product_quantities and self.product_quantities[item] > 0:
            self.product_quantities[item] -= 1
            print(f"Quantity of {item} decreased to {self.product_quantities[item]}")
        else:
            print(f"Cannot decrease quantity of {item}. Quantity is already 0.")

    def update_quantity_label(self, label, item_name):
        current_quantity = self.product_quantities.get(item_name, 0)
        label.config(text=str(current_quantity))
    

    def close_connection(self):
            if self.connection.is_connected():
                self.connection.close()
                print("Connection closed")
    

if __name__ == "__main__":
    bought_products=[]
    # Initialize the database connection without creating the main window
    my_app = MyApp(None)

    # Create the main Tkinter app (second window)
    app = customtkinter.CTk()
    app.geometry("1920x1080")
    app.title("categories")
    customtkinter.set_appearance_mode("system")
    app.config(background='#E4F4FF')

    app.resizable(width=True, height=True)


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
    # Add a buy button for each product
    
    buy_button1 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Tomatoes"), bg="#3F7CAC", fg="white")
    buy_button1.place(x=80, y=200)
    quantity_button1 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button1.place(x=180, y=200)
    plus_button1 = tk.Button(main_frame, text="+", command=lambda: (my_app.increase_quantity("Tomatoes"), my_app.update_quantity_label(quantity_button1, "Tomatoes")), bg="#3F7CAC", fg="white")
    plus_button1.place(x=150, y=200)
    # Adjust the coordinates as needed
    minus_button1 = tk.Button(main_frame, text="-", command=lambda: (my_app.decrease_quantity("Tomatoes"),my_app.update_quantity_label(quantity_button1, "Tomatoes")), bg="#3F7CAC", fg="white")
    minus_button1.place(x=200, y=200)

    buy_button2 = tk.Button(main_frame, text="add", command=lambda:my_app.buy_product("green pepper"), bg="#3F7CAC", fg="white")
    buy_button2.place(x=500, y=200)
    quantity_button2 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button2.place(x=580, y=200)
    plus_button2 = tk.Button(main_frame, text="+", command=lambda: (my_app.increase_quantity("green pepper"), my_app.update_quantity_label(quantity_button2, "green pepper")), bg="#3F7CAC", fg="white")
    plus_button2.place(x=550, y=200)
    minus_button2 = tk.Button(main_frame, text="-", command=lambda: (my_app.decrease_quantity("green pepper"), my_app.update_quantity_label(quantity_button2, "green pepper")), bg="#3F7CAC", fg="white")
    minus_button2.place(x=600, y=200)

    buy_button3 = tk.Button(main_frame, text="Buy", command=lambda: my_app.buy_product("carrots"), bg="#3F7CAC", fg="white")
    buy_button3.place(x=900, y=200)
    quantity_button3 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button3.place(x=980, y=200)
    plus_button3 = tk.Button(main_frame, text="+", command=lambda: (my_app.increase_quantity("carrots"),my_app.update_quantity_label(quantity_button3,"carrots")), bg="#3F7CAC", fg="white")
    plus_button3.place(x=950, y=200)

    minus_button3 = tk.Button(main_frame, text="-", command=lambda: (my_app.decrease_quantity("carrots"),my_app.update_quantity_label(quantity_button3,"carrots")), bg="#3F7CAC", fg="white")
    minus_button3.place(x=1000, y=200)

    buy_button4 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("red pepper"), bg="#3F7CAC", fg="white")
    buy_button4.place(x=1300, y=200)
    quantity_button4 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button4.place(x=1380, y=200)
    plus_button4 = tk.Button(main_frame, text="+", command=lambda: (my_app.increase_quantity("red pepper"),my_app.update_quantity_label(quantity_button4,"carrots")), bg="#3F7CAC", fg="white")
    plus_button4.place(x=1350, y=200)

    minus_button4 = tk.Button(main_frame, text="-", command=lambda: (my_app.decrease_quantity("red pepper"),my_app.update_quantity_label(quantity_button4)), bg="#3F7CAC", fg="white")
    minus_button4.place(x=1400, y=200)


    buy_button5 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Cauliflower"), bg="#3F7CAC", fg="white")
    buy_button5.place(x=100, y=470)
    quantity_button5 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button5.place(x=180, y=470)
    plus_button5 = tk.Button(main_frame, text="+", command=lambda: (my_app.increase_quantity("Cauliflower"),my_app.update_quantity_label(quantity_button5)), bg="#3F7CAC", fg="white")
    plus_button5.place(x=150, y=470)

    minus_button5 = tk.Button(main_frame, text="-", command=lambda: (my_app.decrease_quantity("Cauliflower"),my_app.update_quantity_label(quantity_button5)), bg="#3F7CAC", fg="white")
    minus_button5.place(x=200, y=470)

    buy_button6 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Pumpkin"), bg="#3F7CAC", fg="white")
    buy_button6.place(x=500, y=470)
    quantity_button6 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button6.place(x=580, y=470)
    plus_button6 = tk.Button(main_frame, text="+", command=lambda: (my_app.increase_quantity("Pumpkin"),my_app.update_quantity_label(quantity_button6)), bg="#3F7CAC", fg="white")
    plus_button6.place(x=550, y=470)

    minus_button6 = tk.Button(main_frame, text="-", command=lambda:( my_app.decrease_quantity("Pumpkin"),my_app.update_quantity_label(quantity_button6)), bg="#3F7CAC", fg="white")
    minus_button6.place(x=600, y=470)

    buy_button7 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Onions"), bg="#3F7CAC", fg="white")
    quantity_button7 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button7.place(x=980, y=470)
    buy_button7.place(x=900, y=470)
    plus_button7 = tk.Button(main_frame, text="+", command=lambda: (my_app.increase_quantity("Onions"),my_app.update_quantity_label(quantity_button7)), bg="#3F7CAC", fg="white")
    plus_button7.place(x=950, y=470)

    minus_button7 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Onions"), bg="#3F7CAC", fg="white")
    minus_button7.place(x=1000, y=470)

    buy_button8 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Broccoli"), bg="#3F7CAC", fg="white")
    buy_button8.place(x=1300, y=470)
    quantity_button8 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button8.place(x=1380, y=470)
    plus_button8 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Broccoli"), bg="#3F7CAC", fg="white")
    plus_button8.place(x=1350, y=470)
    
    minus_button8 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Broccoli"), bg="#3F7CAC", fg="white")
    minus_button8.place(x=1400, y=470)

    buy_button9 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Potatoes"), bg="#3F7CAC", fg="white")
    buy_button9.place(x=100, y=740)
    quantity_button9 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button9.place(x=180, y=740)
    plus_button9 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Potatoes"), bg="#3F7CAC", fg="white")
    plus_button9.place(x=150, y=740)

    minus_button9 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Potatoes"), bg="#3F7CAC", fg="white")
    minus_button9.place(x=200, y=740)

    buy_button10 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Garlic"), bg="#3F7CAC", fg="white")
    buy_button10.place(x=500, y=740)
    quantity_button10 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button10.place(x=580, y=740)
    plus_button10 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Garlic"), bg="#3F7CAC", fg="white")
    plus_button10.place(x=550, y=740)

    minus_button10 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Garlic"), bg="#3F7CAC", fg="white")
    minus_button10.place(x=600, y=740)

    buy_button11 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Eggplants"), bg="#3F7CAC", fg="white")
    buy_button11.place(x=900, y=740)
    quantity_button11 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button11.place(x=980, y=740)
    plus_button11 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Eggplants"), bg="#3F7CAC", fg="white")
    plus_button11.place(x=950, y=740)

    minus_button11 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Eggplants"), bg="#3F7CAC", fg="white")
    minus_button11.place(x=1000, y=740)

    buy_button12 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Cucumber"), bg="#3F7CAC", fg="white")
    buy_button12.place(x=1300, y=740)
    quantity_button12 = tk.Label(main_frame, text="0", font=('Bold', 12), bg=None)
    quantity_button12.place(x=1380, y=740)
    plus_button12 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Cucumber"), bg="#3F7CAC", fg="white")
    plus_button12.place(x=1350, y=740)

    minus_button12 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Cucumber"), bg="#3F7CAC", fg="white")
    minus_button12.place(x=1400, y=740)

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
    buy_button13 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Mango"), bg="#3F7CAC", fg="white")
    buy_button13.place(x=80, y=200)
    plus_button13 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Mango"), bg="#3F7CAC", fg="white")
    plus_button13.place(x=150, y=200)

    minus_button13 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Mango"), bg="#3F7CAC", fg="white")
    minus_button13.place(x=200, y=200)

    buy_button14 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Watermelon"), bg="#3F7CAC", fg="white")
    buy_button14.place(x=500, y=200)
    plus_button14 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Watermelon"), bg="#3F7CAC", fg="white")
    plus_button14.place(x=550, y=200)

    minus_button14 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Watermelon"), bg="#3F7CAC", fg="white")
    minus_button14.place(x=600, y=200)

    buy_button15 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Lemons"), bg="#3F7CAC", fg="white")
    buy_button15.place(x=900, y=200)
    plus_button15 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Lemons"), bg="#3F7CAC", fg="white")
    plus_button15.place(x=950, y=200)

    minus_button15 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Lemons"), bg="#3F7CAC", fg="white")
    minus_button15.place(x=1000, y=200)

    buy_button16 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Strawberries"), bg="#3F7CAC", fg="white")
    buy_button16.place(x=1300, y=200)
    plus_button16 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Strawberries"), bg="#3F7CAC", fg="white")
    plus_button16.place(x=1350, y=200)

    minus_button16 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Strawberries"), bg="#3F7CAC", fg="white")
    minus_button16.place(x=1400, y=200)

    buy_button17 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Kiwi"), bg="#3F7CAC", fg="white")
    buy_button17.place(x=80, y=470)
    plus_button17 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Kiwi"), bg="#3F7CAC", fg="white")
    plus_button17.place(x=150, y=470)

    minus_button17 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Kiwi"), bg="#3F7CAC", fg="white")
    minus_button17.place(x=200, y=470)

    buy_button18 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Oranges"), bg="#3F7CAC", fg="white")
    buy_button18.place(x=500, y=470)
    plus_button18 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Oranges"), bg="#3F7CAC", fg="white")
    plus_button18.place(x=550, y=470)

    minus_button18 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Oranges"), bg="#3F7CAC", fg="white")
    minus_button18.place(x=600, y=470)

    buy_button19 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Apples"), bg="#3F7CAC", fg="white")
    buy_button19.place(x=900, y=470)
    plus_button19 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Apples"), bg="#3F7CAC", fg="white")
    plus_button19.place(x=950, y=470)

    minus_button19 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Apples"), bg="#3F7CAC", fg="white")
    minus_button19.place(x=1000, y=470)

    buy_button20 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Ananas"), bg="#3F7CAC", fg="white")
    buy_button20.place(x=1300, y=470)
    plus_button20 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Ananas"), bg="#3F7CAC", fg="white")
    plus_button20.place(x=1350, y=470)

    minus_button20 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Ananas"), bg="#3F7CAC", fg="white")
    minus_button20.place(x=1400, y=470)

    buy_button21 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Blueberries"), bg="#3F7CAC", fg="white")
    buy_button21.place(x=80, y=740)
    plus_button21 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Blueberries"), bg="#3F7CAC", fg="white")
    plus_button21.place(x=150, y=740)

    minus_button21 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Blueberries"), bg="#3F7CAC", fg="white")
    minus_button21.place(x=200, y=740)

    buy_button22 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Banana"), bg="#3F7CAC", fg="white")
    buy_button22.place(x=500, y=740)
    plus_button22 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Banana"), bg="#3F7CAC", fg="white")
    plus_button22.place(x=550, y=740)

    minus_button22 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Banana"), bg="#3F7CAC", fg="white")
    minus_button22.place(x=600, y=740)

    buy_button23 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Pear"), bg="#3F7CAC", fg="white")
    buy_button23.place(x=900, y=740)
    plus_button23 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Pear"), bg="#3F7CAC", fg="white")
    plus_button23.place(x=950, y=740)

    minus_button23 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Pear"), bg="#3F7CAC", fg="white")
    minus_button23.place(x=1000, y=740)

    buy_button24 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Avocado"), bg="#3F7CAC", fg="white")
    buy_button24.place(x=1300, y=740)
    plus_button24 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Avocado"), bg="#3F7CAC", fg="white")
    plus_button24.place(x=1350, y=740)

    minus_button24 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Avocado"), bg="#3F7CAC", fg="white")
    minus_button24.place(x=1400, y=740)

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

    buy_button25 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Andros Mojito"), bg="#3F7CAC", fg="white")
    buy_button25.place(x=80, y=200)
    plus_button25 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Andros Mojito"), bg="#3F7CAC", fg="white")
    plus_button25.place(x=150, y=200)

    minus_button25 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Andros Mojito"), bg="#3F7CAC", fg="white")
    minus_button25.place(x=200, y=200)

    buy_button26 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Bioitalia"), bg="#3F7CAC", fg="white")
    buy_button26.place(x=500, y=200)
    plus_button26 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Bioitalia"), bg="#3F7CAC", fg="white")
    plus_button26.place(x=550, y=200)

    minus_button26 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Bioitalia"), bg="#3F7CAC", fg="white")
    minus_button26.place(x=600, y=200)

    buy_button27 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Simply"), bg="#3F7CAC", fg="white")
    buy_button27.place(x=900, y=200)
    plus_button27 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Simply"), bg="#3F7CAC", fg="white")
    plus_button27.place(x=950, y=200)

    minus_button27 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Simply"), bg="#3F7CAC", fg="white")
    minus_button27.place(x=1000, y=200)

    buy_button28 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Power Horse"), bg="#3F7CAC", fg="white")
    buy_button28.place(x=1300, y=200)
    plus_button28 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Power Horse"), bg="#3F7CAC", fg="white")
    plus_button28.place(x=150, y=200)

    minus_button28 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Power Horse"), bg="#3F7CAC", fg="white")
    minus_button28.place(x=200, y=200)

    buy_button29 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Lipton"), bg="#3F7CAC", fg="white")
    buy_button29.place(x=80, y=470)
    plus_button29 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Lipton"), bg="#3F7CAC", fg="white")
    plus_button29.place(x=150, y=470)

    minus_button29 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Lipton"), bg="#3F7CAC", fg="white")
    minus_button29.place(x=200, y=470)

    buy_button30 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Monster energy"), bg="#3F7CAC", fg="white")
    buy_button30.place(x=500, y=470)
    plus_button30 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Monster energy"), bg="#3F7CAC", fg="white")
    plus_button30.place(x=550, y=470)

    minus_button30 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Monster energy"), bg="#3F7CAC", fg="white")
    minus_button30.place(x=600, y=470)

    buy_button31 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Prime"), bg="#3F7CAC", fg="white")
    buy_button31.place(x=900, y=470)
    plus_button31 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Prime"), bg="#3F7CAC", fg="white")
    plus_button31.place(x=950, y=470)

    minus_button31 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Prime"), bg="#3F7CAC", fg="white")
    minus_button31.place(x=1000, y=470)

    buy_button32 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Red Bull"), bg="#3F7CAC", fg="white")
    buy_button32.place(x=1300, y=470)
    plus_button32 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Red Bull"), bg="#3F7CAC", fg="white")
    plus_button32.place(x=1350, y=470)

    minus_button32 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Red Bull"), bg="#3F7CAC", fg="white")
    minus_button32.place(x=1000, y=470)

    buy_button33 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Sprite"), bg="#3F7CAC", fg="white")
    buy_button33.place(x=80, y=740)
    plus_button33 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Sprite"), bg="#3F7CAC", fg="white")
    plus_button33.place(x=150, y=740)

    minus_button33 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Sprite"), bg="#3F7CAC", fg="white")
    minus_button33.place(x=200, y=740)

    buy_button34 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Valencia"), bg="#3F7CAC", fg="white")
    buy_button34.place(x=500, y=740)
    plus_button34 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Valencia"), bg="#3F7CAC", fg="white")
    plus_button34.place(x=550, y=740)

    minus_button34 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Valencia"), bg="#3F7CAC", fg="white")
    minus_button34.place(x=600, y=740)

    buy_button35 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Tropicana"), bg="#3F7CAC", fg="white")
    buy_button35.place(x=900, y=740)
    plus_button35 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Tropicana"), bg="#3F7CAC", fg="white")
    plus_button35.place(x=950, y=740)

    minus_button35 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Tropicana"), bg="#3F7CAC", fg="white")
    minus_button35.place(x=1000, y=740)

    buy_button36 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Vimto"), bg="#3F7CAC", fg="white")
    buy_button36.place(x=1300, y=740)
    plus_button36 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Vimto"), bg="#3F7CAC", fg="white")
    plus_button36.place(x=1350, y=740)

    minus_button36 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Vimto"), bg="#3F7CAC", fg="white")
    minus_button36.place(x=1400, y=740)


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

    buy_button37 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Lay's"), bg="#3F7CAC", fg="white")
    buy_button37.place(x=80, y=200)
    plus_button37 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Lay's"), bg="#3F7CAC", fg="white")
    plus_button37.place(x=150, y=200)

    minus_button37 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Lay's"), bg="#3F7CAC", fg="white")
    minus_button37.place(x=200, y=200)

    buy_button38 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Doritos"), bg="#3F7CAC", fg="white")
    buy_button38.place(x=500, y=200)
    plus_button38 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Doritos"), bg="#3F7CAC", fg="white")
    plus_button38.place(x=550, y=200)

    minus_button38 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Doritos"), bg="#3F7CAC", fg="white")
    minus_button38.place(x=600, y=200)

    buy_button39 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Pringles"), bg="#3F7CAC", fg="white")
    buy_button39.place(x=900, y=200)
    plus_button39 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Pringles"), bg="#3F7CAC", fg="white")
    plus_button39.place(x=950, y=200)

    minus_button39 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Pringles"), bg="#3F7CAC", fg="white")
    minus_button39.place(x=1000, y=200)

    buy_button40 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("KitKat"), bg="#3F7CAC", fg="white")
    buy_button40.place(x=1300, y=200)
    plus_button40 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("KitKat"), bg="#3F7CAC", fg="white")
    plus_button40.place(x=1350, y=200)

    minus_button40 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("KitKat"), bg="#3F7CAC", fg="white")
    minus_button40.place(x=1400, y=200)

    buy_button41 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Nestle Crunch"), bg="#3F7CAC", fg="white")
    buy_button41.place(x=80, y=470)
    plus_button41 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Nestle Crunch"), bg="#3F7CAC", fg="white")
    plus_button41.place(x=150, y=470)

    minus_button41 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Nestle Crunch"), bg="#3F7CAC", fg="white")
    minus_button41.place(x=200, y=470)

    buy_button42 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Snickers"), bg="#3F7CAC", fg="white")
    buy_button42.place(x=500, y=470)
    plus_button42 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Snickers"), bg="#3F7CAC", fg="white")
    plus_button42.place(x=550, y=470)

    minus_button42 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Snickers"), bg="#3F7CAC", fg="white")
    minus_button42.place(x=600, y=470)

    buy_button43 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Ritz"), bg="#3F7CAC", fg="white")
    buy_button43.place(x=900, y=470)
    plus_button43 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Ritz"), bg="#3F7CAC", fg="white")
    plus_button43.place(x=950, y=470)

    minus_button43 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Ritz"), bg="#3F7CAC", fg="white")
    minus_button43.place(x=1000, y=470)

    buy_button44 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Milka"), bg="#3F7CAC", fg="white")
    buy_button44.place(x=1300, y=470)
    plus_button44 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Milka"), bg="#3F7CAC", fg="white")
    plus_button44.place(x=1350, y=470)

    minus_button44 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Milka"), bg="#3F7CAC", fg="white")
    minus_button44.place(x=1400, y=470)

    buy_button45 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Diary Milk"), bg="#3F7CAC", fg="white")
    buy_button45.place(x=80, y=740)
    plus_button45 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Diary Milk"), bg="#3F7CAC", fg="white")
    plus_button45.place(x=150, y=740)

    minus_button45 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Diary Milk"), bg="#3F7CAC", fg="white")
    minus_button45.place(x=200, y=740)

    buy_button46 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Skittles"), bg="#3F7CAC", fg="white")
    buy_button46.place(x=500, y=740)
    plus_button46 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Skittles"), bg="#3F7CAC", fg="white")
    plus_button46.place(x=550, y=740)

    minus_button46 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Skittles"), bg="#3F7CAC", fg="white")
    minus_button46.place(x=600, y=740)

    buy_button47 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("Nerds"), bg="#3F7CAC", fg="white")
    buy_button47.place(x=900, y=740)
    plus_button47 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("Nerds"), bg="#3F7CAC", fg="white")
    plus_button47.place(x=950, y=740)

    minus_button47 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("Nerds"), bg="#3F7CAC", fg="white")
    minus_button47.place(x=1000, y=740)

    buy_button48 = tk.Button(main_frame, text="add", command=lambda: my_app.buy_product("m&m"), bg="#3F7CAC", fg="white")
    buy_button48.place(x=1300, y=740)
    plus_button48 = tk.Button(main_frame, text="+", command=lambda: my_app.increase_quantity("m&m"), bg="#3F7CAC", fg="white")
    plus_button48.place(x=1350, y=740)

    minus_button48 = tk.Button(main_frame, text="-", command=lambda: my_app.decrease_quantity("m&m"), bg="#3F7CAC", fg="white")
    minus_button48.place(x=1400, y=740)


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



app.mainloop()
my_app.close_connection()