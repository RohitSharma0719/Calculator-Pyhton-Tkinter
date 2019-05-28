import tkinter as tk

# mainwindow=tk.Tk()
# mainwindow.title("simple window")
#
# heading_label=tk.Label(mainwindow,text='Hello World')
# heading_label.pack()
#
# name_field=tk.Entry(mainwindow)
# name_field.pack()
#
# def takeValueInput():
#     name=name_field.get()
#     print(name)
#
# button=tk.Button(mainwindow,text='Get Value',command=lambda :takeValueInput())
# button.pack()
#
# mainwindow.mainloop()


mainwindow=tk.Tk()
mainwindow.title("Calculator")

headinhlabel=tk.Label(mainwindow,text='Enter first number',pady=(10))
headinhlabel.pack()
first_value=tk.Entry(mainwindow)
first_value.pack()
headinhlabel=tk.Label(mainwindow,text='Enter second number',pady=(10))
headinhlabel.pack()
secondvalue=tk.Entry(mainwindow)
secondvalue.pack()

def add():
    first=int(first_value.get())
    second=int(secondvalue.get())
    # print(first+second)
    result_label.config(text="Operation Result is:"+str(first+second))

def sub():
    first = int(first_value.get())
    second = int(secondvalue.get())
    # print('Subtraction:',first-second)
    result_label.config(text="Operation Result is:" + str(first - second))

def multiply():
    first = int(first_value.get())
    second = int(secondvalue.get())
    # print('Multiply:',first*second)
    result_label.config(text="Operation Result is:" + str(first * second))

def divide():
    first = int(first_value.get())
    second = int(secondvalue.get())
    # print('Divide:',first/second)
    result_label.config(text="Operation Result is:" + str(first / second))


headinhlabel=tk.Label(mainwindow,text='Operations')
headinhlabel.pack()
button=tk.Button(mainwindow,text='Addition',command=lambda :add())
button.pack()

button=tk.Button(mainwindow,text='Subtraction',command=lambda :sub())
button.pack()

button=tk.Button(mainwindow,text='Multiply',command=lambda :multiply())
button.pack()

button=tk.Button(mainwindow,text='Divide',command=lambda :divide())
button.pack()

result_label=tk.Label(mainwindow,text='Operation Result is:')
result_label.pack()
mainwindow.mainloop()