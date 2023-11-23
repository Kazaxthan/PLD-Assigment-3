
import tkinter as tk
from tkinter import messagebox


def display_output():
    surname = surname_entry.get()
    first_name = first_name_entry.get()
    middle_initial = middle_initial_entry.get()
    suffix = suffix_entry.get()
    age = age_entry.get()
    address = address_entry.get()

    while all((surname.isalpha() or surname.isspace()) for surname in surname) == False:
        messagebox.showwarning("Error", "Please enter valid surname")
        return
    
    while all((first_name.isalpha() or first_name.isspace()) for first_name in first_name) == False:
        messagebox.showwarning("Error", "Please enter valid first_name")
        return

    while all(middle_initial.isalpha() for middle_initial in middle_initial) == False:
        messagebox.showwarning("Error", "Please enter valid middle_initial")
        return
    
    while all((suffix.isalpha() or suffix.isnumeric()) for suffix in suffix) == False:
        messagebox.showwarning("Error", "Please enter valid suffix")
        return

    while all(age.isdigit() for age in age) == False:
        messagebox.showwarning("Error", "Please enter a valid age.")
        return
    
    if not surname or not first_name or not age or not address:
        messagebox.showwarning("Error", "Please fill in all fields.")
        return


    
    output_title = f"------------------------------------------------------------------------------------------------------------------------------------------------------------------Thank You for Answering------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n"
    output_text = f"It's All About You!☟\n"
    name_title = f"Your name is"
    name_text = f"{first_name} {middle_initial}. {surname}, {suffix}"
    age_title = f"You are"
    age_text = f"{age} years old"
    address_title = f"You are currently living in"
    address_text = f"{address}"

    output_window = tk.Toplevel()
    output_window.title("Output")
    output_window.geometry("1280x720")
    output_window.configure(bg="#000000")
    
    output_title_label = tk.Label(output_window, text=output_title, fg="lime",bg="#000000", font=("Times", "15","bold italic"))
    output_title_label.pack()

    output_text_label = tk.Label(output_window, text=output_text, fg="lime",bg="#000000", font=("Times", "55","bold italic"))
    output_text_label.pack()

    name_title_label = tk.Label(output_window, text=name_title, fg="yellow green",bg="#000000", font=("verdana","15"))
    name_title_label.pack()

    name_text_label = tk.Label(output_window, text=name_text, fg="lime",bg="#000000", font=("Times","30"))
    name_text_label.pack()

    age_title_label = tk.Label(output_window, text=age_title, fg="yellow green",bg="#000000", font=("verdana","15"))
    age_title_label.pack()

    age_text_label = tk.Label(output_window, text=age_text, fg="lime",bg="#000000", font=("Times","30"))
    age_text_label.pack()

    address_title_label = tk. Label(output_window, text=address_title, fg="yellow green",bg="#000000", font=("verdana","15"))
    address_title_label.pack()

    address_text_label = tk.Label(output_window, text=address_text, fg="lime",bg="#000000", font=("Times","30"))
    address_text_label.pack()



window = tk.Tk()
window.title("Personal Information")

window.configure(bg="#000000")

window.geometry("520x320")

label = tk.Label(window, text="Please Fill-up The Information Below:", font=("Times", "24","bold italic"), bg="#000000", fg="lime").grid(row=0, column=0, sticky=tk.W)

tk.Label(window, text="Surname:", font=("Helvetica", 12), bg="#000000", fg="lime").grid(row=2, column=0, sticky=tk.W)
surname_entry = tk.Entry(window, width=21, font=("Helvetica", 12))
surname_entry.grid(row=2, column=0, pady=5)

tk.Label(window, text="First Name:", font=("Helvetica", 12), bg="#000000", fg="lime").grid(row=3, column=0, sticky=tk.W)
first_name_entry = tk.Entry(window, width=21, font=("Helvetica", 12))
first_name_entry.grid(row=3, column=0, pady=5)

tk.Label(window, text="Middle Initial:(leave it\nblank if not applicable)", font=("Helvetica", 12), bg="#000000", fg="lime").grid(row=4, column=0, sticky=tk.W)
middle_initial_entry = tk.Entry(window, width=21, font=("Helvetica", 12))
middle_initial_entry.grid(row=4, column=0, pady=5)

tk.Label(window, text="Suffix:(leave it blank\nif not applicable)", font=("Helvetica", 12), bg="#000000", fg="lime").grid(row=5, column=0, sticky=tk.W)
suffix_entry = tk.Entry(window, width=21, font=("Helvetica", 12))
suffix_entry.grid(row=5, column=0, pady=5)

tk.Label(window, text="Age:", font=("Helvetica", 12), bg="#000000", fg="lime").grid(row=6, column=0, sticky=tk.W)
age_entry = tk.Entry(window, width=21, font=("Helvetica", 12))
age_entry.grid(row=6, column=0, pady=5)

tk.Label(window, text="Address:", font=("Helvetica", 12), bg="#000000", fg="lime").grid(row=7, column=0, sticky=tk.W)
address_entry = tk.Entry(window, width=21, font=("Helvetica", 12))
address_entry.grid(row=7, column=0, pady=1)


submit_button = tk.Button(window, text="Submit your Information", command=display_output, font=("Times", "14","bold italic"), bg="lime", fg="black", padx=20, pady=10)
submit_button.grid(row=8, column=0, columnspan=2, pady=10)


for i in range(9, 10):
    tk.Label(window, text="", bg="#000000").grid(row=i, column=0)


window.mainloop()
