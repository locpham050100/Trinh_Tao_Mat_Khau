# them thu vien 
from tkinter import*
import random, string 
import pyperclip 

# tao cua so 
root = Tk() 
root.geometry("400x400")
root.resizable(0,0)
root.title("Trình Tạo Mật Khẩu")

# edit tieu de
heading = Label(root, text='TẠO MẬT KHẨU', font='arial 15 bold').pack()
Label(root, text='LocCute', font='arial 15 bold').pack(side=BOTTOM) 

# chon do dai mat khau 
pass_label = Label(root, text='ĐỘ DÀI MẬT KHẨU', font='arial 10 bold').pack() 
pass_len = IntVar() 
lenght = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

# tao mat khau 
pass_str = StringVar()
def Generator():
    password = ''
    for x in range(0,4):   
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()-4):
        password = password+random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
    pass_str.set(password)

# nut nhan 
Button(root, text='TẠO MẬT KHẨU', command=Generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()

# ham copy mat khau
def Copy_password():
    pyperclip.copy(pass_str.get())

# tao nut copy 
Button(root, text='CHÉP VÀO KHAY NHỚ TẠM', command=Copy_password).pack(pady=5) 

# vong lap chuong trinh 
root.mainloop() 
