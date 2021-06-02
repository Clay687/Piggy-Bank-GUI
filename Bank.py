from tkinter import *
from tkinter.messagebox import showerror, showinfo
import win32gui,win32con

root = Tk()
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide,win32con.SW_HIDE)

root.iconbitmap("C:\\Users\\prince\\Desktop\\GUI\\Required files\\Bank.ico")
root.title("AlphaX Bank")
root.geometry("400x400")
root.maxsize(400,400)
root.minsize(400,400)

f1 = Frame(root)
f1.pack(side=TOP)

f2 = Frame(root)
f2.pack(side=TOP,anchor="nw")

Label(f1,text="AplhaX Bank",fg="blue",font="lucida 20 underline bold").pack()

l1 = Label(f2,text="Please Select Language : ",font="lucida 15")
l1.pack(padx=20,pady=40)

def balance():
    init_depo = 0
    init_with = 0
    with open("C:\\Users\\prince\\Desktop\\GUI\\Required files\\Bank.txt","r") as f:
        b = f.readlines()
        b.remove("\n")

        for i in b:
            if i.startswith("Deposited"):
                c = i.split("-")
                m = c[1]
                init_depo +=int(m)

            elif i.startswith("Withdraw"):
                c = i.split("-")
                m = c[1]
                init_with +=int(m)
        net_balance = init_depo - init_with
    return net_balance


def hin():
    l1.config(text="")
    hin_btn.destroy()
    eng_btn.destroy()
    
    l2 = Label(root,text="अपना 4 अंकों का पिन दर्ज करें:",font="lucida 15")
    l2.place(x=30,y=70)

    pin = Entry(root,font="lucida 15",width=8)
    pin.place(x=40,y=120)

    def pin_com():
        pin_value = pin.get()
        
        with open("C:\\Users\\prince\\Desktop\\GUI\\Required files\\PIN.txt","r") as f:
            b = f.read()
            f.close()

        if pin_value==b:
            l2.config(text="")
            change_btn.destroy()
            pin.destroy()
            pin_btn.destroy()

            l3 = Label(root,text="मोड का चयन करें:",font="lucida 15")
            l3.pack()

            def deposit_func1():
                withdraw.destroy()
                deposit.destroy()
                check_balance.destroy()

                l3.config(text="")
                de_lbl = Label(root,text="जमा करने के लिए राशि दर्ज करें :",font="lucida 15")
                de_lbl.place(x=50,y=100)

                de_entry = Entry(root,width=15,font="lucida 15")
                de_entry.place(x=70,y=150)

                def de_btn_func():
                    money = str(de_entry.get())
                    if money.isdigit():
                        showinfo("जमा कर दिया",f"प्रिय उपयोगकर्ता आपका ₹{money} सफलतापूर्वक जमा हो गया है")

                        with open("C:\\Users\\prince\\Desktop\\GUI\\Required files\\Bank.txt","a") as f:
                            f.write("\n")
                            f.write("Deposited")
                            f.write("-")
                            f.write(money)
            
                    else:
                        showinfo("गलत जानकारी","कृपया केवल नंबर दर्ज करें")


                deposit_btn = Button(root,text="जमा",font="lucida 15",fg="blue",command=de_btn_func)
                deposit_btn.place(x=295,y=250)

            def withdraw_func1():
                deposit.destroy()
                check_balance.destroy()
                withdraw.destroy()
                l3.config(text="")

                dp_lbl = Label(root,text="वह राशि दर्ज करें जिसे आप निकालना चाहते हैं:",font="lucida 15")
                dp_lbl.place(x=30,y=100)

                dp_entry = Entry(root,width=15,font="lucida 15")
                dp_entry.place(x=70,y=150)

                def dp_btn():
                    money = dp_entry.get()
                    if balance()>int(money):
                        showinfo("निकालना",f"प्रिय उपयोगकर्ता आपका  ₹{money} सफलतापूर्वक निकाल लिया गया है")
                        with open("C:\\Users\\prince\\Desktop\GUI\\Required files\\Bank.txt","a") as f:
                            f.write("\n")
                            f.write("Withdraw")
                            f.write("-")
                            f.write(money)
                            
                    else:
                        showinfo("अपर्याप्त शेषराशि","अपर्याप्त शेषराशि")

                withdraw_btn = Button(root,text="निकालना",font="lucida 15",fg="blue",command=dp_btn)
                withdraw_btn.place(x=295,y=250)
            
            def check1():
                withdraw.destroy()
                deposit.destroy()
                check_balance.destroy()
                l3.config(text="")

                l4 = Label(root,text=f"नेट बैलेंस = ₹{balance()}",font="lucida 20")
                l4.pack()

            withdraw = Button(root,text="निकालना",fg="white",bg="blue",font="lucida 15",command=withdraw_func1)
            withdraw.pack(side=LEFT,anchor="nw",padx=50,pady=30)

            deposit = Button(root,text="जमा",fg="white",bg="blue",font="lucida 15",command=deposit_func1)
            deposit.pack(side=RIGHT,anchor="ne",padx=50,pady=30)

            check_balance = Button(root,text="अपना नेट बैलेंस चेक करें",fg="white",bg="blue",font="lucida 15",command=check1)
            check_balance.place(x=50,y=290)

            quit_btn = Button(root,text="बाहर जाएं",fg="white",bg="red",font="lucida 15",command=exit)
            quit_btn.place(x=300,y=300)

        elif pin_value=="":
            showinfo("शून्य पिन बॉक्स","प्रिय उपयोगकर्ता कृपया अपना 4 अंकों का पिन दर्ज करें, इसे खाली न रखें")

        else:
            showinfo("अमान्य पिन","प्रिय उपयोगकर्ता आपने गलत पिन दर्ज किया है। यदि आप इसे भूल गए हैं तो इसे बदल दें। या फिर से दर्ज करें")
    
    def change1():
        change_btn.destroy()
        l2.config(text="")
        pin.destroy()
        pin_btn.destroy()
        

        q = Label(root,text="अपना पिन बदलने के \nलिए सुरक्षा प्रश्न का उत्तर दें।",font="lucida 15 bold underline")
        q.place(x=30,y=70)  

        q1 = Label(root,text="तुम कहॉ पैदा हुए थे? : ",font="lucida 13")
        q1.place(x=20,y=170)
        q1_entry = Entry(root,font="lucida 15",width=12)
        q1_entry.place(x=250,y=170)

        q2 = Label(root,text="आपका पहला पालतू जानवर\n का नाम क्या है? : ",font="lucida 13")
        q2.place(x=20,y=250)
        q2_entry = Entry(root,font="lucida 15",width=12)
        q2_entry.place(x=250,y=250)


        def submit_func():
            if q1_entry.get()=="Gorakhpur" and q2_entry.get()=="Sheru":
                q.config(text="")
                q1.config(text="")
                q1_entry.destroy()
                q2.config(text="")
                q2_entry.destroy()
                submit.destroy()

                l5 = Label(root,text="अपना नया 4-अंकों का पिन डालें :",font="lucida 15")
                l5.place(x=30,y=70)

                new_pin = Entry(root,font="lucida 15",width=8)
                new_pin.place(x=40,y=120)

                def pin_change():
                    new_pin_text = str(new_pin.get())
                    
                    if new_pin_text.isnumeric():
                        if len(new_pin_text)==4:
                            with open("C:\\Users\\prince\\Desktop\GUI\\Required files\\PIN.txt","w") as f:
                                f.write(new_pin_text)
                                showinfo("पिन सफलतापूर्वक बदल गया",f"प्रिय उपयोगकर्ता अब आपका पिन बदल दिया गया है  {new_pin_text}")
                                f.close()
                        else:
                            showerror("अमान्य","कृपया 4 अंकों का पिन दर्ज करें")

                           
                    else:
                        showerror("अमान्य","प्रिय उपयोगकर्ता कृपया केवल नंबर दर्ज करें")
                                

                set_pin_btn = Button(root,text="अपना नया पिन सेट करें",font="lucida 15",fg="blue",command=pin_change)
                set_pin_btn.place(x=180,y=180)

                quit_btn = Button(root,text="बाहर जाएं",fg="white",bg="red",font="lucida 15",command=exit)
                quit_btn.place(x=300,y=350)

            else:
                showinfo("अमान्य उत्तर","प्रिय उपयोगकर्ता आपने सुरक्षा प्रश्न का गलत उत्तर दिया है। इसलिए आप पिन नहीं बदल सकते")

        submit = Button(root,text="प्रस्तुत",font="lucida 15",fg="blue",command=submit_func)
        submit.place(x=280,y=350)

    change_btn = Button(root,text="अपना पिन बदलें",font="lucida 10 bold",fg="white",bg="red",command=change1)
    change_btn.place(x=250,y=230)

    pin_btn = Button(root,text="आगे बढ़ें",font="lucida 15",fg="blue",command=pin_com)
    pin_btn.place(x=250,y=180)

    

hin_btn = Button(f2,text="हिंदी",font="lucida 15",fg="blue",command=hin)
hin_btn.pack(anchor="nw",padx=40)

def eng():
    l1.config(text="")
    hin_btn.destroy()
    eng_btn.destroy()
    
    l2 = Label(root,text="Enter your 4-Digit PIN :",font="lucida 15")
    l2.place(x=30,y=70)

    pin = Entry(root,font="lucida 15",width=8)
    pin.place(x=40,y=120)

    def pin_com():
        pin_value = pin.get()

        with open("C:\\Users\\prince\\Desktop\\GUI\\Required files\\PIN.txt","r") as f:
            b = f.read()
            f.close()
    
        if pin_value==b:
            l2.config(text="")
            change_btn.destroy()
            pin.destroy()
            
            pin_btn.destroy()

            l3 = Label(root,text="Select the mode : ",font="lucida 15")
            l3.pack()
            
            def deposit_func():
                withdraw.destroy()
                deposit.destroy()
                check_balance.destroy()
                l3.config(text="")
                de_lbl = Label(root,text="Enter the amount to deposit : ",font="lucida 15")
                de_lbl.place(x=50,y=100)

                de_entry = Entry(root,width=15,font="lucida 15")
                de_entry.place(x=70,y=150)

                def de_btn_func():
                    money = str(de_entry.get())
                    if money.isdigit():
                        showinfo("Deposited",f"Dear User your ₹{money} is successfully deposited")

                        with open("C:\\Users\prince\\Desktop\\GUI\\Required files\\Bank.txt","a") as f:
                            f.write("\n")
                            f.write("Deposited")
                            f.write("-")
                            f.write(money)
            
                    else:
                        showinfo("Invalid Data","Please enter only numbers")


                deposit_btn = Button(root,text="Deposit",font="lucida 15",fg="blue",command=de_btn_func)
                deposit_btn.place(x=295,y=250)

            def withdraw_func():
                deposit.destroy()
                check_balance.destroy()
                withdraw.destroy()
                
                l3.config(text="")

                dp_lbl = Label(root,text="Enter the amount you want to withdraw : ",font="lucida 15")
                dp_lbl.place(x=30,y=100)

                dp_entry = Entry(root,width=15,font="lucida 15")
                dp_entry.place(x=70,y=150)

                def dp_btn():
                    money = dp_entry.get()
                    if balance()>int(money):
                        showinfo("Withdraw",f"Dear User your ₹{money} is successfully withdraw")
                        with open("C:\\Users\\prince\\Desktop\GUI\\Required files\\Bank.txt","a") as f:
                            f.write("\n")
                            f.write("Withdraw")
                            f.write("-")
                            f.write(money)
                            
                    else:
                        showinfo("Insufficient Balance","Insufficient Balance")

                withdraw_btn = Button(root,text="Withdraw",font="lucida 15",fg="blue",command=dp_btn)
                withdraw_btn.place(x=295,y=250)

            withdraw = Button(root,text="Withdraw",fg="white",bg="blue",font="lucida 15",command=withdraw_func)
            withdraw.pack(side=LEFT,anchor="nw",padx=50,pady=30)

            deposit = Button(root,text="Deposit",fg="white",bg="blue",font="lucida 15",command=deposit_func)
            deposit.pack(side=RIGHT,anchor="ne",padx=50,pady=30)

            def check():
                withdraw.destroy()
                deposit.destroy()
                check_balance.destroy()
                l3.config(text="")

                l4 = Label(root,text=f"Net Balance = ₹{balance()}",font="lucida 20")
                l4.pack()

            check_balance = Button(root,text="Check your net Balance",fg="white",bg="blue",font="lucida 15",command=check)
            check_balance.place(x=50,y=290)

            quit_btn = Button(root,text="Exit",fg="white",bg="red",font="lucida 15",command=exit)
            quit_btn.place(x=330,y=350)

        elif pin_value=="":
            showinfo("Void PIN Box","Dear user please enter your 4-digit PIN don't leave it blank")

        else:
            showinfo("Invalid PIN","Dear User you have entered wrong pin.Change it now if you forget it or re-enter it.")

    def change():
        change_btn.destroy()
        l2.config(text="")
        pin.destroy()
        pin_btn.destroy()
        

        q = Label(root,text="Answer the Security Question to \nchange your PIN.",font="lucida 15 bold underline")
        q.place(x=30,y=70)  

        q1 = Label(root,text="Where you were Born : ",font="lucida 13")
        q1.place(x=20,y=170)
        q1_entry = Entry(root,font="lucida 15",width=12)
        q1_entry.place(x=250,y=170)

        q2 = Label(root,text="What is your first pet name : ",font="lucida 13")
        q2.place(x=20,y=250)
        q2_entry = Entry(root,font="lucida 15",width=12)
        q2_entry.place(x=250,y=250)


        def submit_func():
            if q1_entry.get()=="Gorakhpur" and q2_entry.get()=="Sheru":
                q.config(text="")
                q1.config(text="")
                q1_entry.destroy()
                q2.config(text="")
                q2_entry.destroy()
                submit.destroy()

                l5 = Label(root,text="Enter your new 4-Digit PIN :",font="lucida 15")
                l5.place(x=30,y=70)

                new_pin = Entry(root,font="lucida 15",width=8)
                new_pin.place(x=40,y=120)

                def pin_change():
                    new_pin_text = str(new_pin.get())
                    
                    if new_pin_text.isnumeric():
                        if len(new_pin_text)==4:
                            with open("C:\\Users\\prince\\Desktop\\GUI\\Required files\\PIN.txt","w") as f:
                                f.write(new_pin_text)
                                showinfo("PIN changed successfully",f"Dear user now your PIN is changed to {new_pin_text}")
                                f.close()

                        else:
                            showerror("Invalid","Please enter 4 digit PIN")
                           
                    else:
                        showerror("Invalid","Dear user please only enter numbers")
                                

                set_pin_btn = Button(root,text="Set your new PIN",font="lucida 15",fg="blue",command=pin_change)
                set_pin_btn.place(x=200,y=180)

                quit_btn = Button(root,text="Exit",fg="white",bg="red",font="lucida 15",command=exit)
                quit_btn.place(x=330,y=350)

            else:
                showinfo("Invalid Answers","Dear user you have entered wrong answer of security question. So you cannot change the PIN")

        submit = Button(root,text="Submit",font="lucida 15",fg="blue",command=submit_func)
        submit.place(x=280,y=350)


            
    change_btn = Button(root,text="Change your PIN",font="lucida 10 bold",fg="white",bg="red",command=change)
    change_btn.place(x=250,y=230)

    pin_btn = Button(root,text="Proceed",font="lucida 15",fg="blue",command=pin_com)
    pin_btn.place(x=250,y=180)

eng_btn = Button(f2,text="English",font="lucida 15",fg="blue",command=eng)
eng_btn.pack(anchor="nw",padx=40,pady=20)

root.mainloop()
