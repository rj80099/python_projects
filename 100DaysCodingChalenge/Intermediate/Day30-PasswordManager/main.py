from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','v','w','x','y','z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','#','$','&','(','*','+']

    #chose an integer number between a range
    nr_letters=random.randint(8,10)
    nr_symbols=random.randint(2,4)
    nr_numbers=random.randint(2,4)

    #empty list to store random password
    password_list =[]

    #get a random choice for the number in range
    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    #concatinate strings of password and append in password list.
    password_list=password_letters+password_symbols+password_numbers

    #shuffle and get the completely new password on every new click on generate password
    random.shuffle(password_list)

#password =""
#for char in password_list:
    #password +=char

    #alternately we can also do this using join method
    password="".join(password_list)
    #insert the generated password on the password entries.
    password_entry.insert(0, password)

    #copy the password on the clipboard using pyperclip python library
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

#save the details enter in all the entry fields..no empty fields allowed to save
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    #if empty field found show a message box
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields")
    else:
        is_ok=messagebox.askokcancel(title=website, message=f"This are the details entered:\nEmail:{email}"
                                                     f"\nPassword:{password}\nIs this ok to save?")
        #on sucessful validation save/append all the data in data.text file
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}|{email}|{password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

#window setup
window =Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

#canvas and logo image setup
canvas =Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)         #if not using grid view alternate is using...canvas.pack()
canvas.grid(column=1,row=0)

#labels
website_label=Label(text="website:")
email_label =Label(text="Email/Username:")
password_label=Label(text="Password:")

website_label.grid(column=0,row=1)
email_label.grid(column=0,row=2)
password_label.grid(column=0,row=3)


#Entries
website_entry=Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)
email_entry.insert(0,"rj@gamil.com")

#Buttons
generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

#make the window availble infinitely
window.mainloop()