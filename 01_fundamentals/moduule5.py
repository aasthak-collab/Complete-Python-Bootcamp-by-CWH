# 1
# fom tkinter import *
# top = Tk()
# top.geometry("450x300")
# user_name = Label(top,
#                   text = "Username").place(x=40,
#                                            y=60)
# user_password = Label(top,
#                       text = "Password").place(x = 40,
#                                                y = 100)
# submit_button = Button(top,
#                        text = "Submit").place(x = 40,
#                                               y = 130)
# user_name_input_area = Entry(top,
#                              width=30).place(x=110,
#                                              y=60)
# user_password_entry_area = Entry(top,
#                                  width = 30).place(x=110,
#                                                    y=100)
# top.mainloop()
# 2
# from tkinter import *
# master = Tk()
# w = Canvas(master, width=40, height=60)
# w.pack()
# canvas_height=20
# canvas_width=200
# y = int(canvas_height / 2)
# w.create_line(0,y,canvas_width, y)
# mainloop
import tkinter as tk

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

# Create the main window
cal = tk.Tk()
cal.geometry("400x560")
cal.title("Super Calculator")

# Screen
scvalue = tk.StringVar()
scvalue.set("")
screen = tk.Entry(cal, font="lucida 45 bold", bg="lightblue", textvar=scvalue)
screen.pack(pady=10)

# Button Frame
button_frame = tk.Frame(cal)
button_frame.pack()

# Buttons
button_texts = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
    ("C", 4, 0)
]

for (text, row, col) in button_texts:
    button = tk.Button(button_frame, text=text, font="lucida 25 bold", padx=20, pady=20, bg="grey")
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)

# Start the Tkinter event loop
cal.mainloop()
