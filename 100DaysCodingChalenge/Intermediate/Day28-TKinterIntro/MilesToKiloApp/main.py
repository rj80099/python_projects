# import tkinter
#
# window=tkinter.Tk()
# window.title("Miles to Kilo")
# window.minsize(width=500,height=300)
# window.config(padx=20,pady=20)
#
# def clicked_it():
#     print("You clicked me")
#
# #label
# label=tkinter.Label(text="label",font=("Arial",24,"bold"))
# label.grid(column=0,row=0)
# label.config(padx=20,pady=20)
#
# #Button
# new_button=tkinter.Button(text="New Button",command=clicked_it)
# new_button.grid(column=2,row=0)
#
# click_me=tkinter.Button(text="Click me",command=clicked_it)
# click_me.grid(column=1,row=1)
# #Entry

# input=tkinter.Entry(width=10)
# input.get()
# input.grid(column=3, row=2)
# window.mainloop()


#Miles to Kilo Mini App

import tkinter


def miles_to_km():
    miles=float(miles_input.get())
    km=miles * 1.609
    label_answer.config(text=f"{km}")
#create a window of size 300x100 as main widget GUI
window=tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=150,height=100)
window.config(padx=20,pady=20)
#Get the input from user and validate
miles_input=tkinter.Entry(width=10)
#keep the cursor on the input widget
miles_input.focus()
miles_input.grid(column=1,row=0)

label_mile=tkinter.Label(text="Miles")
label_mile.grid(column=2,row=0 )


label_equalto=tkinter.Label(text="is equal to")
label_equalto.grid(column=0,row=1 )

label_answer=tkinter.Label(text="0",width=10)
label_answer.grid(column=1,row=1 )

label_km=tkinter.Label(text="Km")
label_km.grid(column=2,row=1 )


#button
calcluate_btn=tkinter.Button(text="Calculate",command=miles_to_km)
calcluate_btn.grid(column=1,row=2)
#keep the screen active
window.mainloop()


