import tkinter as tk
from tkinter import messagebox
import datetime

root=tk.Tk()

result_label = tk.Label(root, text="")
result_label.pack()

# Function to retrieve the birthdate from the user and format it as a string
def get_birthdate():
    try:
        birthdate = datetime.datetime(
            int(birth_year_var.get()),
            int(birth_month_var.get()),
            int(birth_day_var.get()),
        )
        birthdate_str = birthdate.strftime("%m-%d-%Y")
        result_label.config(text=f"Your birthdate is: {birthdate_str}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root.mainloop()