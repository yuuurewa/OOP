from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from datetime import datetime
from dateutil.relativedelta import relativedelta

def clicked():
    date1 = datetime.now().date()
    date2 = date1 + relativedelta(months=+int(spin.get()))
    T = (date2 - date1).days
    K = int(combo.get())
    P = int(txt.get())
    stavka = txt1.get()

    if ',' in stavka:
        stavka=stavka.replace(',', '.')

    I = float(stavka)
    S = (P * I * (T / K)) / 100
    messagebox.showinfo('Доход', 'Доход по вкладу будет составлять %.3f руб.' % S)

window = Tk()
window.title("Счетчик дохода по вкладу")
icon = PhotoImage(file = "icon.png")
window.iconphoto(True, icon)
window.geometry('500x400+500+200')

lbl = Label(window, text='Выберите количество месяцев вклада:')
lbl.grid(column=0, row=0, pady=10)
spin = Spinbox(window, from_=1, to=12, width=10)
spin.grid(column=1, row=0, pady=10)

lbl1 = Label(window, text='Выберите количество дней в текущем году:')
lbl1.grid(column=0, row=1, pady=10, padx=10)
combo = Combobox(window)
combo['values'] = (365, 366)
combo.current(0)
combo.grid(column=1, row=1, pady=10)

lbl2 = Label(window, text='Введите сумму вложений (руб.):')
lbl2.grid(column=0, row=2, pady=10)
txt = Entry(window,width=10)
txt.grid(column=1, row=2, pady=10)

lbl3 = Label(window, text='Введите процентную ставку:')
lbl3.grid(column=0, row=3, pady=10)
txt1 = Entry(window,width=10)
txt1.grid(column=1, row=3, pady=30)

btn = Button(window, text="Расчитать доход", bg="blue", fg="white", command=clicked)
btn.grid(column=1, row=4, pady=10)

window.mainloop()
