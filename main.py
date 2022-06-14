from tkinter import  *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300,height=200)
window.config(padx=50,pady=50)

def mile_km():
    mile = float(entry_mile.get())
    mile_to_km = mile*1.609
    float_km = "{:.2f}".format(mile_to_km)
    return float_km

def mouse_click():
    return km.config(text=mile_km())

#LABEL
label = Label(text="Enter Miles:")
label.config(padx=10,pady=10)
label.grid(row=1,column=1)

#LABEL
label = Label(text="is equal to")
label.config(padx=10,pady=10)
label.grid(row=2,column=1)

#LABEL
label = Label(text="Miles")
label.config(padx=10,pady=10)
label.grid(row=1,column=3)

#LABEL
label = Label(text="Km")
label.config(padx=10,pady=10)
label.grid(row=2,column=3)

#ENTRY OF MILES
entry_mile = Entry(width=10)
entry_mile.insert(END,string="")
entry_mile.grid(row=1,column=2)

#DISPLAY OF KM
km = Label(text=0)
km.grid(column=2,row=2)

#BUTTON
button =Button(text="Calculate",command=mouse_click)
button.config(pady=5,padx=15)
button.grid(row=3,column=2)

window.mainloop()
