from currency_converter import CurrencyConverter
# a=CurrencyConverter()
# print(a.convert(12,"USD","INR"))
from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("Currency Converter")
a=CurrencyConverter()
def click():
    amount=int(e1.get())
    currency1=e2.get()
    currency2=e3.get()
    data=a.convert(amount,currency1,currency2)
    l5=Label(root,text=data,font=("Times new roman", 12, "bold")).place(x=200,y=290)
    



label=Label(root, text="Currency Converter", font=("Times new roman", 25, "bold")).place(x=100,y=30)
l1=Label(root, text="Enter amount here:", font=("Times new roman", 15, "bold")).place(x=50,y=100)
e1=Entry(root)
e1.place(x=230, y=105)
l2=Label(root, text="Enter Currency:", font=("Times new roman", 15, "bold")).place(x=50,y=150)
e2=Entry(root)
e2.place(x=230, y=155)
l3=Label(root, text="Enter Req Currency:", font=("Times new roman", 15, "bold")).place(x=50,y=200)
e3=Entry(root)
e3.place(x=230, y=205)
Button(root,text="Convert", command=click).place(x=230,y=240)


root.mainloop()