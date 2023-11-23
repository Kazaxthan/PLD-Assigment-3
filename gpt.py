import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("system")

# Main Window
window = customtkinter.CTk()
window.title("PLD ASSIGNMENT 3")
window.geometry('1200x1000')

# Main Frame
frame = customtkinter.CTkFrame(window)
frame.pack(expand=True)

# Function to calculate and display results
def enter():
    apple = spinbox_1.get()
    orange = spinbox_2.get()

    sum_apple = 20 * apple
    sum_orange = 25 * orange
    sum_all = sum_apple + sum_orange
    total_apple = f"Total amount of Apple: ₱{sum_apple}"
    total_orange = f"Total amount of Orange: ₱{sum_orange}"
    total_sum = f"Total amount you have to pay: ₱{sum_all}"

    # Result Window
    result_window = customtkinter.CTk()
    result_window.title("RESULT")
    result_window.geometry('600x400')

    result_frame = customtkinter.CTkFrame(result_window)
    result_frame.pack()

    apple_text = customtkinter.CTkLabel(result_frame, text=total_apple)
    apple_text.pack()

    orange_text = customtkinter.CTkLabel(result_frame, text=total_orange)
    orange_text.pack()

    sum_text = customtkinter.CTkLabel(result_frame, text=total_sum)
    sum_text.pack()

    result_window.mainloop()

# Info Frame
info_frame = customtkinter.CTkFrame(frame)
info_frame.pack(ipadx=10, ipady=10, side="top")

# Apple Frame
apple_frame = customtkinter.CTkFrame(frame, corner_radius=10)
apple_frame.pack(padx=10, pady=10, side="right")

# Orange Frame
orange_frame = customtkinter.CTkFrame(frame)
orange_frame.pack(padx=10, pady=10, side="right")

# Photo Frame
photo_frame = customtkinter.CTkFrame(frame)
photo_frame.pack(padx=10, pady=10, side="left")

# GIF
gif_frames = []
frame_delay = 0

def ready_gif():
    global frame_delay
    gif_file = Image.open('PLD.gif')

    for r in range(0, gif_file.n_frames):
        gif_file.seek(r)
        gif_frames.append(gif_file.copy()
    
    frame_delay = gif_file.info['duration']
    play_gif()

def play_gif():
    global frame_count, current_frame

    if frame_count >= len(gif_frames) - 1:
        frame_count = -1
        play_gif()

    else:
        frame_count += 1
        current_frame = ImageTk.PhotoImage(gif_frames[frame_count])
        gif_lb.config(image=current_frame)
        photo_frame.after(frame_delay, play_gif)

gif_lb = tk.Label(photo_frame)
gif_lb.pack()

# Multithreading for GIF
threading.Thread(target=ready_gif).start()
ready_gif()

# Header Label
header_label = customtkinter.CTkLabel(info_frame, text="Enter the amount of Apples and Oranges you want to buy.", font=("Arial", 20))
header_label.grid(row=0, column=0, padx=20, pady=20)

# Apple Label and Entry
apple_label = customtkinter.CTkLabel(apple_frame, text="Apple:")
apple_label.grid(row=1, column=0, padx=20, pady=20)

spinbox_1 = FloatSpinbox(apple_frame, width=150, step_size=1)
spinbox_1.grid(padx=20, pady=20)
spinbox_1.set(0)

# Orange Label and Entry
orange_label = customtkinter.CTkLabel(orange_frame, text="Orange:")
orange_label.grid(row=1, column=0, padx=20, pady=20)

spinbox_2 = FloatSpinbox(orange_frame, width=150, step_size=1)
spinbox_2.grid(padx=20, pady=20)
spinbox_2.set(0)

# Button
button_frame = customtkinter.CTkFrame(frame)
button_frame.pack(ipadx=10, ipady=10, side="bottom")

enter_data = customtkinter.CTkButton(button_frame, text="Submit", command=enter)
enter_data.pack()

window.mainloop()