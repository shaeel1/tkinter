# Question  # 3
# Create car automation system, Insert 5 car records with following field.Car Name, Car ID, Car Manufacturing Name,
# Car Model, Car Engine No, Car Manufacturing Date, Car Color, Car Authorized Dealer, Car City, Car Price etc.
# Insert a statement if user selects more than one car than calculate some discount on Car Price(or you may
# calculate discount on Car Manufacturing Name).You need to insert all records in one sheet / text file and in 2 nd sheet
# (name all sheet appropriately) create a proper form with all fields, when user select Car ID through drop down list
# then all other fields will automatically fill.


from tkinter import *
import time
import random
import tkinter.messagebox
import openpyxl as xl

# ..............................Welcome Window..............................................
welcome = Tk()
welcome.attributes('-fullscreen', True)
welcome.title("Car Automation System")
hydra = PhotoImage(file="bg.png")
Label(welcome, image=hydra).place(relwidth=1, relheight=1)
Label(welcome,  text="Welcome to Car Automation System",
      font=('arial', 30, "bold")).pack(side=TOP)

welcome.after(2000, lambda: welcome.destroy())

welcome.mainloop()

# ................................Main Window................................................

root = Tk()
root.attributes('-fullscreen', True)
root.title("Car Automation System")
root.configure(background='sky blue')
hydra = PhotoImage(file="bg.png")
Label(root, image=hydra).place(relwidth=1, relheight=1)

# .................................( IMPORTING EXCEL FILE).......................................


def car_list(name):
    wb = xl.load_workbook('car.xlsx')
    sheet = wb['Sheet1']
    cell = sheet[name]
    return(cell.value)


# .................................... ( FUNCTIONS AND VARIABLES)................................
prices = {
    "corolla": car_list("i2"),
    "pajero": car_list("i3"),
    "tesla": car_list("i4"),
    "audi": car_list("i5"),
    "phantom": car_list("i6")
}


service_charge = 5000
tax = 0.15
discount = 0.1


def total(name):
    price = int(prices[name])
    dp = price * 0.1
    dp1 = price - dp
    dp2 = dp1 + service_charge
    return (f"Rs {(dp2 * tax) + dp2}")


def func(value1):
    if value1 == car_list("b2"):
        car_name.set(car_list("b2"))
        car_manufacturing_name.set(car_list("c2"))
        car_model.set(car_list("d2"))
        car_city.set(car_list("h2"))
        car_manufacturing_date.set(car_list("f2"))
        car_color.set(car_list("g2"))
        car_id.set(car_list("a2"))
        car_price.set(f"Rs {car_list('i2')}")
        ServiceCharge.set(f"Rs {service_charge}")
        PaidTax.set("15 %")
        TotalCost.set(total('corolla'))
        Discount.set("10 % OFF")

    elif value1 == car_list("b3"):
        car_name.set(value1)
        car_manufacturing_name.set(car_list("c3"))
        car_model.set(car_list("d3"))
        car_city.set(car_list("h3"))
        car_manufacturing_date.set(car_list("f3"))
        car_color.set(car_list("g3"))
        car_id.set(car_list("a3"))
        car_price.set(f"Rs {car_list('i3')}")
        ServiceCharge.set("Rs 5000")
        PaidTax.set("15 %")
        TotalCost.set(total("pajero"))
        Discount.set("10 % OFF")

    elif value1 == car_list("b4"):
        car_name.set(value1)
        car_manufacturing_name.set(car_list("c4"))
        car_model.set(car_list("d4"))
        car_city.set(car_list("h4"))
        car_manufacturing_date.set(car_list("f4"))
        car_color.set(car_list("g4"))
        car_id.set(car_list("a4"))
        car_price.set(f"Rs {car_list('i4')}")
        ServiceCharge.set("Rs 5000")
        PaidTax.set("15 %")
        TotalCost.set(total("tesla"))
        Discount.set("10 % OFF")

    elif value1 == car_list("b5"):
        car_name.set(value1)
        car_manufacturing_name.set(car_list("c5"))
        car_model.set(car_list("d5"))
        car_city.set(car_list("h5"))
        car_manufacturing_date.set(car_list("f5"))
        car_color.set(car_list("g5"))
        car_id.set(car_list("a5"))
        car_price.set(f"Rs {car_list('i5')}")
        ServiceCharge.set("Rs 5000")
        PaidTax.set("15 %")
        TotalCost.set(total("audi"))
        Discount.set("10 % OFF")

    elif value1 == car_list("b6"):
        car_name.set(value1)
        car_manufacturing_name.set(car_list("c6"))
        car_model.set(car_list("d6"))
        car_city.set(car_list("h6"))
        car_manufacturing_date.set(car_list("f6"))
        car_color.set(car_list("g6"))
        car_id.set(car_list("a6"))
        car_price.set(f"Rs {car_list('i6')}")
        ServiceCharge.set("Rs 5000")
        PaidTax.set("15 %")
        TotalCost.set(total("phantom"))
        Discount.set("10 % OFF")

    else:
        car_name.set("")
        car_manufacturing_name.set("")
        car_model.set("")
        car_city.set("")
        car_manufacturing_date.set("")
        car_color.set("")
        car_id.set("")
        car_price.set("")
        ServiceCharge.set("")
        PaidTax.set("")
        TotalCost.set("")
        Discount.set("")


Date_of_Order = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Discount = StringVar()
Total_of_Car = StringVar()
ServiceCharge = StringVar()
text_Input = StringVar()
operator = ""

car_name = StringVar()
car_manufacturing_name = StringVar()
car_model = StringVar()
car_city = StringVar()
car_manufacturing_date = StringVar()
car_color = StringVar()
car_id = StringVar()
car_price = StringVar()

Date_of_Order.set(time.strftime("%y/%m/%d"))
# ...................................................................................................


# .....................................( DROP MENU)..........................................
options = [
    "Select Car",
    car_list("b2"),
    car_list("b3"),
    car_list("b4"),
    car_list("b5"),
    car_list("b6"),
]

clicked = StringVar()
clicked.set(options[0])

list = OptionMenu(root, clicked, *options,
                  command=func).place(x=1100, y=70, width=150)


# ...................................( FRAMES )..................................................

ReceiptCal_Function = Frame(root, bg="#c7c1c1")
ReceiptCal_Function.pack(side=BOTTOM, anchor="sw")

Receipt_Function = Frame(
    ReceiptCal_Function)
Receipt_Function.pack(side=BOTTOM)

Buttons_Function = Frame(
    ReceiptCal_Function, bg="#c7c1c1")
Buttons_Function.pack(side=TOP)


# .................................( FUNCTION DECLERATION )......................................

def iExit():
    iExit = tkinter.messagebox.askyesno(
        "Exit", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return


def Reset():
    textReceipt.delete("1.0", END)
    car_name.set("")
    car_manufacturing_name.set("")
    car_model.set("")
    car_city.set("")
    car_manufacturing_date.set("")
    car_color.set("")
    car_id.set("")
    car_price.set("")
    ServiceCharge.set("")
    PaidTax.set("")
    TotalCost.set("")
    Discount.set("")
    clicked.set(options[0])


def Receipt():
    textReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill No. " + randomRef)

    textReceipt.insert(END, 'Receipt Ref:\t\t\t' +
                       Receipt_Ref.get() + '\t' + Date_of_Order.get() + '\n')
    textReceipt.insert(END, 'Car Name:\t\t\t\t' + car_name.get() + '\n')
    textReceipt.insert(END, 'Car Manufacturing Name:\t\t\t\t' +
                       car_manufacturing_name.get()+'\n')
    textReceipt.insert(END, 'Car Model:\t\t\t\t' +
                       car_model.get()+'\n')
    textReceipt.insert(END, 'Car City:\t\t\t\t' +
                       car_city.get()+'\n')
    textReceipt.insert(END, 'Car Manufacturing Date:\t\t\t\t' +
                       car_manufacturing_date.get()+'\n')
    textReceipt.insert(END, 'Car Color:\t\t\t\t' +
                       car_color.get()+'\n')
    textReceipt.insert(END, 'Car ID:\t\t\t\t' + car_id.get()+'\n')
    textReceipt.insert(END, 'Car Price:\t\t\t\t' + car_price.get()+'\n')
    textReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get() +
                       '\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")

# .................................... ( LABELS )...........................................


lbl_select_car = Label(root, text="Select the Car", font=(
    'arial', 16, 'bold')).place(x=1100, y=30)


CarID = Label(root, bg="#db030a", text=car_list("a1"), font=(
    'arial', 12, 'bold')).place(x=40, y=30)

carName = Label(root, bg="#db030a", text='Car Name', font=(
    'arial', 12, 'bold')).place(x=40, y=70)

carModel = Label(root, bg="#da030a", text=car_list("d1"), font=(
    'arial', 12, 'bold')).place(x=40, y=110)

carCity = Label(root, bg="#da030a", text=car_list("h1"), font=(
    'arial', 12, 'bold')).place(x=40, y=150)

carManufacturingDate = Label(root, text=car_list(
    "f1"), bg="#c70309", font=('arial', 12, 'bold')).place(x=500, y=30)

carColor = Label(root, text=car_list("g1"), bg="#c70309", font=(
    'arial', 12, 'bold')).place(x=500, y=70)

carManufacturingName = Label(root, text=car_list(
    'c1'), bg="#c70309", font=('arial', 12, 'bold')).place(x=500, y=110)

carPrice = Label(root, text=car_list("i1"), bg="#c70309",  font=(
    'arial', 12, 'bold')).place(x=500, y=150)

# ....................................( ENTRY ).......................................

textCarId = Entry(root, font=('arial', 16, 'bold'),
                  width=20, justify=LEFT, state=DISABLED, textvariable=car_id)
textCarId.place(x=150, y=30)

textCar_name = Entry(root, font=('arial', 16, 'bold'),
                     width=20, justify=LEFT, state=DISABLED, textvariable=car_name)
textCar_name.place(x=150, y=70)

textCarModel = Entry(root, font=('arial', 16, 'bold'),
                     width=20, justify=LEFT, state=DISABLED, textvariable=car_model)
textCarModel.place(x=150, y=110)

textCarCity = Entry(root, font=('arial', 16, 'bold'),
                    width=20, justify=LEFT, state=DISABLED, textvariable=car_city)
textCarCity.place(x=150, y=150)

textCarManufacturingDate = Entry(root, font=('arial', 16, 'bold'),
                                 width=20, justify=LEFT, state=DISABLED, textvariable=car_manufacturing_date)
textCarManufacturingDate.place(x=720, y=30)


textCarColor = Entry(root, font=('arial', 16, 'bold'),
                     width=20, justify=LEFT, state=DISABLED, textvariable=car_color)
textCarColor.place(x=720, y=70)

textCarManufacturingName = Entry(root, font=('arial', 16, 'bold'),
                                 width=20, justify=LEFT, state=DISABLED, textvariable=car_manufacturing_name)
textCarManufacturingName.place(x=720, y=110)


textCarPrice = Entry(root, font=('arial', 16, 'bold'),
                     width=20, justify=LEFT, state=DISABLED, textvariable=car_price)
textCarPrice.place(x=720, y=150)

# ...............................( LABELS AND ENTRY )....................................................

lblServiceCharge = Label(root, bg="#d3d3d1", font=(
    'arial', 14, 'bold'), text='Service Charge', fg='black', justify=CENTER)
lblServiceCharge.place(x=450, y=550)
txtServiceCharge = Entry(root, font=(
    'arial', 14, 'bold'), justify=LEFT, state=DISABLED, textvariable=ServiceCharge)
txtServiceCharge.place(x=450, y=580, width=150, height=29)

lblDiscount = Label(root, bg="#d6d5d3", font=(
    'arial', 14, 'bold'), text='Discount', fg='black', justify=CENTER)
lblDiscount.place(x=830, y=550)
txtDiscount = Entry(root, font=(
    'arial', 14, 'bold'), insertwidth=2, justify=LEFT, state=DISABLED, textvariable=Discount)
txtDiscount.place(x=830, y=580, width=90, height=29)
# Payment information

lblPaidTax = Label(root, bg="#beb6b3", font=('arial', 14, 'bold'),
                   text='Paid Tax', fg='black')
lblPaidTax.place(x=1220, y=550)
textPaidTax = Entry(root, font=(
    'arial', 14, 'bold'), insertwidth=2, justify=LEFT, state=DISABLED, textvariable=PaidTax)
textPaidTax.place(x=1220, y=580, width=88, height=29)


lblTotalCost = Label(root, bg="#b9b3b5", font=('arial', 20, 'bold'),
                     text='Total', fg='black', justify=CENTER)
lblTotalCost.place(x=630, y=660, width=200)
textTotalCost = Entry(root, font=(
    'arial', 20, 'bold'), insertwidth=2, justify=CENTER, state=DISABLED, textvariable=TotalCost)
textTotalCost.place(x=880, y=660, width=200)

# ......................................( RECEIPT )..........................................

textReceipt = Text(Receipt_Function, width=46, height=12,
                   bg='white', bd=4, font=('arial', 12, 'bold'))
textReceipt.pack(side=RIGHT)

# .........................................( BUTTONS )..........................................

buttonReceipt = Button(Buttons_Function, padx=16, pady=1, font=(
    'arial', 12, 'bold'), width=4, text='Receipt', activebackground="gray64", command=Receipt).pack(side=LEFT)
buttonReset = Button(Buttons_Function, padx=16, font=(
    'arial', 12, 'bold'), width=4, text='Reset', activebackground="gray64",  command=Reset).pack(side=LEFT)
buttonExit = Button(Buttons_Function, padx=16, pady=1, font=(
    'arial', 12, 'bold'), width=4, text='Exit', activebackground="gray64",  command=iExit).pack(side=LEFT)


root.mainloop()
