import tkinter as t
from datetime import date
window = t.Tk()
window.geometry("400x300")
window.title("Welcome App")
def display():
    name = name_entry.get()
    global message
    message = "welcome to the application \n Todays date is :  "
    greet = "hello" +name + "\n"
    display_txtbox.insert(t.END.greet)
    display_txtbox.insert(t.END.message)
    display_txtbox.insert(t.END.today())

main_label=t.Label(window, text= "Hello there!", font = "comicsansms, 12",bg = "Light Blue")
main_label.pack()
name_label = t.Label(window, text="Full name", font = "comicsansms,12",bg="Light blue")
name_label.pack()
name_entry = t.Entry(window,width=30)
name_entry.pack()
btn = t.Button(window, text = "Click Here", font="ALGERIAN,12",bg="Light blue",command=display)
btn.pack()
display_txtbox= t.Text(height=3)
display_txtbox.pack()
t.mainloop()