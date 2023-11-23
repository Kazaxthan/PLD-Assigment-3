import customtkinter
import tkinter
from tkinter import ttk


customtkinter.set_default_color_theme("blue")
    
customtkinter.set_appearance_mode("system")

def enter_data():
    
     
    #user info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()    
    title = title_combobox.get()
    age = age_entry.get()
    # Address
    street = Street_entry.get()
    subd = subd_entry.get()
    muni = muni_entry.get()
    city = city_entry.get()
    province = province_entry.get()
        
    userinfo= title + firstname + " " + lastname
    
    address= street +","+ subd+","+muni+","+city+","+province
    if firstname and lastname and street and muni and city and province:
        if  firstname and lastname:  str.isalpha( ) == False
    
        window = customtkinter.CTk()
        window.title("User Information")
        window.geometry("1200x600x`")
        result = customtkinter.CTkFrame(window)
        result.pack( padx=20, pady=20, expand=True,)
        
        info = customtkinter.CTkLabel(master= result, text= userinfo, font = ("Roboto", 36),text_color="#ADD8E6"  )
        info.grid (row=1, column=0)
        info = customtkinter.CTkLabel(master= result, text= age, font = ("Roboto", 36),text_color="#ADD8E6"  )
        info.grid (row=3, column=0)
        info = customtkinter.CTkLabel(master= result, text= address, font = ("Roboto", 36),text_color="#ADD8E6")
        info.grid (row=5, column=0)
        info = customtkinter.CTkLabel(master= result, text= "You're name is", font = ("Roboto", 24),text_color="#CF9FFF"  )
        info.grid (row=0, column=0)
        info = customtkinter.CTkLabel(master= result, text= "You're age is", font = ("Roboto", 24),text_color="#CF9FFF"  )
        info.grid (row=2, column=0)
        info = customtkinter.CTkLabel(master= result, text= "You're from", font = ("Roboto", 24),text_color="#CF9FFF")
        info.grid (row=4, column=0)
        
        
        window.mainloop()
    else:
        tkinter.messagebox.showwarning(title="error", message= "you have not filled out the form correctly.")
      
    
    

window = customtkinter.CTk()
window.title("PLD ASSIGNMENT 2")

frame = customtkinter.CTkFrame(window)
frame.pack()

window.configure(fg_color = "red")
# user info frame
user_info_frame =customtkinter.CTkFrame(frame)
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)




first_name_entry= customtkinter.CTkEntry (user_info_frame, placeholder_text= "First Name")
last_name_entry= customtkinter.CTkEntry (user_info_frame, placeholder_text= "Last Name")
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
title_label = customtkinter.CTkLabel(user_info_frame, text="User Infomation", fg_color="gray", corner_radius=34)
title_combobox= customtkinter.CTkComboBox(user_info_frame, values=["Mr.", "Ms.","Mrs."] )
title_label.grid (row=0, column=1)
title_combobox.grid (row=1, column=2)

age_entry = customtkinter.CTkEntry(user_info_frame, placeholder_text="Age")
age_entry.grid (row= 3, column =1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# ADDRESS
address_frame = customtkinter.CTkFrame(frame)
address_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
street_name_label =customtkinter.CTkLabel(address_frame, text="Address", fg_color="gray", corner_radius=34)
street_name_label.grid(row=0, column=2)


Street_entry =customtkinter.CTkEntry (address_frame, placeholder_text="Floor/Street")
Street_entry.grid (row =1, column=0)
subd_entry =customtkinter.CTkEntry (address_frame, placeholder_text="Subd./bldg.")
subd_entry.grid (row=1, column=1)
muni_entry =customtkinter.CTkEntry (address_frame, placeholder_text="Municipality")
muni_entry.grid (row= 1 , column= 2)
city_entry =customtkinter.CTkEntry (address_frame, placeholder_text="City")
city_entry.grid (row=1, column= 3)
province_entry =customtkinter.CTkEntry (address_frame, placeholder_text="Province")
province_entry.grid (row= 1 , column= 4)

for widget in address_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)




# enter data button
button_frame = tkinter.Frame(frame)
button_frame.grid (row=2, column=0, sticky="news", padx=20, pady=20)
button_label = customtkinter.CTkButton(frame, text = "Enter data",fg_color= ("#DB3E39", "#821D1A"), hover_color="lightblue", command= enter_data)
button_label.grid (row=2, column= 0,sticky="news", padx=10, pady=10)





window.mainloop()


