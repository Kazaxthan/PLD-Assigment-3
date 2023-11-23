import customtkinter
customtkinter.set_default_color_theme("blue")
    
customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.title ("PLD ASSIGNMENT 2")

frame = customtkinter.CTkFrame(master = root)
 # FRAME
user_info_frame = customtkinter.CTkFrame(master = frame)
user_info_frame.grid(row=0, column=0, padx = 20, pady = 10, ) 
user_info_frame.pack(pady= 100, padx= 100, fill="both", expand= True,)

first_name_label =customtkinter.CTkLabel(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label =customtkinter.CTkLabel(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry= customtkinter.CTkEntry (user_info_frame)
last_name_entry= customtkinter.CTkEntry (user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_entry.grid(row=1, column=1)
title_label = customtkinter.CTkLabel(user_info_frame, text="TITLE")
title_combobox= customtkinter.CTkComboBox(user_info_frame, values=["", "Mr.", "Ms."] )
title_label.grid (row=0, column=2)
title_combobox.grid (row=1, column=2)

age_label =customtkinter.CTkLabel(user_info_frame, text= "Age")
age_spinbox = customtkinter.CTkSlider(user_info_frame, from_= 12, to= 110)
age_label.grid  (row=2, column=1, padx = 10)
age_spinbox.grid (row= 2, column =1)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# ADDRESS
address_frame = customtkinter.CTkLabel(master = root, text="Address")
address_frame.grid(row=5, column=4, padx=20, pady=10)
street_name_label =customtkinter.CTkLabel(address_frame, text="Floor/Street")
street_name_label.grid(row=5, column=0)
subd_name_label =customtkinter.CTkLabel(address_frame, text="Subd./bldg./")
subd_name_label.grid(row=5, column=1)
muni_name_label =customtkinter.CTkLabel(address_frame, text="Municipality")
muni_name_label.grid(row=5, column=2)
city_name_label =customtkinter.CTkLabel(address_frame, text="City")
city_name_label.grid(row=5, column=3)
province_name_label =customtkinter.CTkLabel(address_frame, text="Province")
province_name_label.grid(row=5, column=4)

Street_entry =customtkinter.CTkEntry (address_frame)
Street_entry.grid (row =6, column=0)
subd_entry =customtkinter.CTkEntry (address_frame)
subd_entry.grid (row=6, column=1)
muni_entry =customtkinter.CTkEntry (address_frame)
muni_entry.grid (row= 6 , column= 2)
city_entry =customtkinter.CTkEntry (address_frame)
city_entry.grid (row=6, column= 3)
province_entry =customtkinter.CTkEntry (address_frame)
province_entry.grid (row= 6 , column= 4)

for widget in address_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)




# enter data button
button_frame = customtkinter.CTkFrame(master = root)
button_frame.grid (row=7, column=0, padx=20, pady=20)
button_label = customtkinter.CTkButton(master = root, text = "Enter data",)
button_label.grid (row=7, column= 0, padx=10, pady=10)







root.mainloop()