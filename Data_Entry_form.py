"""
    Code By: Salman Mallah: 22BSCYS021
    final Project (Data Entry Form application)
    tkinter [1] Create GUI
    Pronunciation:
    ~tee-kinter
    ~kt-inter
    ~kinter
"""
# starter code
import tkinter as tk
from tkinter import ttk
from csv import DictWriter

win = tk.Tk()
win.title("Gui Project")
win.geometry('800x350')

# Create Labels
name_label = ttk.Label(win, text='Enter your name : ')
name_label.grid(row=0, column=0, sticky=tk.W)

email_label = ttk.Label(win, text='Enter your email : ')
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(win, text='Enter your age : ')
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text='Enter your Gender : ')
gender_label.grid(row=3, column=0, sticky=tk.W)

# Create Entry Box
name_var = tk.StringVar()
name_entry = tk.Entry(win, width=20, bg='#ffd749', bd=4, textvariable=name_var)
name_entry.grid(row=0, column=1)
name_entry.focus()

email_var = tk.StringVar()
email_entry = tk.Entry(win, width=20, bg='#ffd749', bd=4, textvariable=email_var)
email_entry.grid(row=1, column=1)

age_var = tk.StringVar()
age_entry = tk.Entry(win, width=20, bg='#ffd749', bd=4, textvariable=age_var)
age_entry.grid(row=2, column=1)

# Create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=18, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.grid(row=3, column=1)
gender_combobox.current(0)

# Create Radio Button
# Student | Teacher
usertype = tk.StringVar()
radio_button1 = ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radio_button1.grid(row=4, column=0)


radio_button2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radio_button2.grid(row=4, column=1)

# Create Check Button
check_button_value = tk.IntVar()
check_button = ttk.Checkbutton(win, text="Agree & Continue Please read all!", variable=check_button_value)
check_button.grid(row=5, columnspan=3)


def action():
    name = name_var.get()
    email = email_var.get()
    age = age_var.get()
    gender = gender_var.get()
    user_type = usertype.get()
    if check_button_value.get() == 0:
        agreed = "NO"
    else:
        agreed = 'Yes'

    # write to csv file
    with open('userdata.csv', 'a', newline="") as wf:
        dict_writer = DictWriter(wf, fieldnames=['UserName', 'UserEmail', 'UserAge', 'UserGender', 'UserType', 'UserAgreed'])
        if os.stat('userdata.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'UserName': name,
            'UserEmail': email,
            'UserAge': age,
            'UserGender': gender,
            'UserType': user_type,
            'UserAgreed': agreed,
        })

    
    # delete EntryBox data after submit
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# submit button
submit_button = ttk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, column=0)

win.mainloop()
