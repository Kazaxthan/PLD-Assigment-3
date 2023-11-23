import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading



customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("system")

window = customtkinter.CTk()
window.title("PLD ASSIGNMENT 3")
window.geometry('1200x1000')
frame = customtkinter.CTkFrame(window)
frame.pack(expand = True)

# user info framex

def enter():
    
    money = float(money_entry.get())
    price = float(price_entry.get())
    
    quantity_apple = (money//price)
    amount_change = (money - (quantity_apple*price))
   
    total_quantity_apple = f"Total amount of Apple: ₱{quantity_apple}" 
    total_amout_change =  f"Total amount of Orange: ₱{amount_change}"
    
    
    app = customtkinter.CTk()
    app.title("RESULT")
    app.geometry('1200x1000')
    frame = customtkinter.CTkFrame(app)
    frame.pack()
    
    apple_text = customtkinter.CTkLabel(frame, text = total_quantity_apple )
    apple_text.pack()
    orange_text = customtkinter.CTkLabel(frame, text = total_amout_change)
    orange_text.pack()
 
    
    
    
    
info_frame =customtkinter.CTkFrame(frame)
info_frame.pack(ipadx = 10, ipady= 10, side = "top")
price_frame = customtkinter.CTkFrame (frame)
price_frame.pack(padx = 10, pady= 10, side = "right")
money_frame = customtkinter.CTkFrame (frame, corner_radius=10)
money_frame.pack(padx = 10, pady= 10, side = "right")

    
photo_frame = customtkinter.CTkFrame (frame)
photo_frame.pack(padx = 20, pady=10, side = "left")

#GIF
gif_frames = []

frame_delay = 0

def ready_gif():
    global frame_delay
    gif_file = Image.open('PLD.gif')
        
    for r in range(0, gif_file.n_frames):
           
           gif_file.seek(r)
           gif_frames.append(gif_file.copy())
    frame_delay = gif_file.info['duration']
    print('Complete')
    play_gif()

frame_count = -1

def play_gif():
    global frame_count, current_frame
    
    if frame_count >= len(gif_frames) -1:
        frame_count =-1
        play_gif()
    
    else:
        
        frame_count +=1
        
        current_frame = ImageTk.PhotoImage(gif_frames[frame_count])
        gif_lb.config(image=current_frame)
        photo_frame.after (frame_delay, play_gif)

    
    

gif_lb = tk.Label(photo_frame)
gif_lb.pack ()
 
threading.Thread(target=ready_gif).start()
ready_gif() 

#ENTRIES
money_entry = customtkinter.CTkEntry (money_frame, placeholder_text= "Enter Amount" )
money_entry.pack()
price_entry = customtkinter.CTkEntry (price_frame, placeholder_text= "Enter Price" )
price_entry.pack()
info_label = customtkinter.CTkLabel (info_frame, text= "Enter the amount of money you had\n Enter the price of the Apple"  )
info_label.pack()
    

    #BUTTON
button_frame = customtkinter.CTkFrame(frame)
button_frame.pack(ipadx = 10, ipady= 10, side = "bottom",)
enter_data = customtkinter.CTkButton (button_frame, text  = "submit", command= enter)
enter_data.pack()


    



window.mainloop()

