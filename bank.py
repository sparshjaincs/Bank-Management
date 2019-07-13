from tkinter import *
import json as js
from tkinter import messagebox as mb
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
class interface:
    i=1
    j=0
    closing=""
    def __init__(self):
        interface.i=2
        interface.j=float(10000)
        interface.closing=""
        self.dictionary=dict()
        self.accno="AOJPJ201900"
    def master(self):
        self.top=Tk()
        self.top.configure(background='#111')
        self.top.geometry("1350x730+0+0")
        self.top.resizable(False,False)
        self.top.title("Bank Application")
        obj1.frame()
        obj1.label()
        obj1.button()
        
        obj1.logsin()
        obj1.text()
       
        self.top.mainloop()
    def frame(self):
        self.frame1=Frame(self.top,width=1350,height=70,bg="#A17C46",bd=0)
        self.frame1.place(relx=0,rely=0)
    def label(self):
        for i in range(1,4):
            self.labeli=Label(self.top,width=1350,height=4,bd=0,bg="#333")
            self.labeli.place(relx=0,rely=.17*i+.17)
            
            self.label5=Label(self.top,width=45,height=25,bd=0,bg="#A17C46")
            self.label5.place(relx=.6,rely=.295)
            
            self.label6=Label(self.frame1,width=45,bd=0,bg="#A17C46",fg="#111",text="BANK MANAGEMENT",font=("arial",30,"bold"))
            self.label6.place(relx=.1,rely=.2)
            
    def button(self):
        # img1=PhotoImage(file="images/Login_25px.png")
        self.button1=Button(self.top,text="SIGN IN",font=("arial",20,"bold"),bd=1,bg="#111",width=7,fg="white",activebackground="#A17C46",command=obj1.signin,cursor="arrow")
        self.button1.place(relx=.02,rely=.12)
        
         # img2=PhotoImage(file="images/Signin_25px.png")
        self.button2=Button(self.top,text="LOG IN",bd=1,bg="#111",width=7,font=("arial",20,"bold"),fg="white",activebackground="#A17C46",command=obj1.login,cursor="arrow")
        self.button2.place(relx=.13,rely=.12)

        self.button4=Button(self.top,text="SUBMIT",bd=1,bg="#A17C46",width=7,height=1,font=("arial",16,"bold"),fg="#222",activebackground="#111",command=obj1.file_login,cursor="arrow")
        self.button4.place(relx=.68,rely=.72)
    def login(self):
        interface.i=1
        
        obj1.logsin()
        
        self.text9.delete("1.0",END)
        self.text9.insert(END,"LOG IN")
        
        self.text12.delete("1.0",END)
        self.text12.insert(END,"         EMAIL ID")
        
        self.text13.delete("1.0",END)
        self.text13.insert(END,"PHONE NUMBER")
        
        self.text14.delete("1.0",END)
        self.text14.insert(END,"\t\t\tINFORMATION")
        self.text14.delete("1.0",END)
        self.text14.insert(END,"\t\t\tINFORMATION")
        obj1.reset()

        
    def signin(self):
        interface.i=2
        
        obj1.logsin()
        
        self.text9.delete("1.0",END)
        self.text9.insert(END,"SIGN IN")
        
        self.text12.delete("1.0",END)
        self.text12.insert(END,"ACCOUNT NUMBER")
        
        self.text13.delete("1.0",END)
        self.text13.insert(END,"        EMAIL ID")

        self.text14.delete("1.0",END)
        self.text14.insert(END,"\t\t\tINFORMATION+\n\t")

        self.text14.delete("1.0",END)
        self.text14.insert(END,"\t\t\tINFORMATION")
        obj1.reset()
    def logsin(self):
        if interface.i==1:
            self.text1=Entry(self.top,width=17,bd=0,bg="#111",fg="#666",font=("arial",20),cursor="arrow")
            self.text1.place(relx=.623,rely=.35)
          
            self.text2=Entry(self.top,width=17,bd=0,bg="#111",fg="#666",text="PASSWORD",font=("arial",20),show="*",cursor="arrow")
            self.text2.place(relx=.623,rely=.45)
            
            self.text3=Entry(self.top,width=17,bd=0,bg="#111",fg="#666",text="EMAIL ID",font=("arial",20),cursor="arrow")
            self.text3.place(relx=.623,rely=.55)
            
            self.text4=Entry(self.top,width=17,bd=0,bg="#111",fg="#666",text="PHONE NUMBER",font=("arial",20),cursor="arrow")
            self.text4.place(relx=.623,rely=.65)
         
            self.labellog1=Label(self.top,width=30,bd=0,bg="#111",height=2)
            self.labellog1.place(relx=.623,rely=.82)
        elif interface.i==2:
            self.text5=Entry(self.top,width=17,bd=0,bg="#111",fg="#666",text="USERNAME",font=("arial",20),cursor="arrow")
            self.text5.place(relx=.623,rely=.35)
            
            self.text6=Entry(self.top,width=17,bd=0,bg="#111",fg="#666",text="PASSWORD",font=("arial",20),show="*",cursor="arrow")
            self.text6.place(relx=.623,rely=.45)
            
            self.text7=Entry(self.top,width=17,bd=0,bg="#111",fg="#666",text="ACCOUNT MUNBER",font=("arial",20),cursor="arrow")
            self.text7.place(relx=.623,rely=.55)
            
            self.text8=Entry(self.top,width=17,bd=0,bg="#111",fg="#666",text="EMAIL ID",font=("arial",20),cursor="arrow")
            self.text8.place(relx=.623,rely=.65)
           
            self.button3=Button(self.top,cursor="arrow",text="FORGOT PASSWORD?",bd=0,bg="#111",\
                                width=18,font=("arial",10,"bold underline"),fg="#A17C46",activebackground="#A17C46",command=obj1.forgot_password)
            self.button3.place(relx=.66,rely=.82)
           
            
    def  text(self):
        
        self.text9=Text(self.top,width=10,height=1,bg="#111",fg="#A17C46",bd=0,font=("arial",24,"bold "))
        self.text9.place(relx=.67,rely=.24)
        self.text9.insert(END,"SIGN IN")
        
        self.text10=Text(self.top,width=20,height=1,bg="#A17C46",fg="#111",bd=0,font=("arial",12,"bold "),)
        self.text10.place(relx=.68,rely=.32)
        self.text10.insert(END,"USERNAME")
        
        self.text11=Text(self.top,width=20,height=1,bg="#A17C46",fg="#111",bd=0,font=("arial",12,"bold "))
        self.text11.place(relx=.68,rely=.42)
        self.text11.insert(END,"PASSWORD")
        
        self.text12=Text(self.top,width=20,height=1,bg="#A17C46",fg="#111",bd=0,font=("arial",12,"bold "))
        self.text12.place(relx=.66,rely=.52)
        self.text12.insert(END,"ACCOUNT NUMBER")
        
        self.text13=Text(self.top,width=20,height=1,bg="#A17C46",fg="#111",bd=0,font=("arial",12,"bold "))
        self.text13.place(relx=.665,rely=.62)
        self.text13.insert(END,"        EMAIL ID")

        self.text14=Text(self.top,width=60,height=5,bg="#111",fg="#666",bd=2,font=("arial",12,"bold "),relief=RAISED)
        self.text14.place(relx=.25,rely=.88)
        self.text14.insert(END,"\t\t\tINFORMATION")


    def forgot_password(self):
        pass
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def file_login_system(self):
                                self.fp1=open("file/login_info.db")
                                self.read=js.load(self.fp1)
                                key=list(self.read.keys())
                                
                                value=int(key[-1])
                                self.fp1.close()
                                for i in key:
                                    if self.read[i]['Name']==self.text1.get():
                                        self.flag=1
                                        break
                                    else:
                                        self.flag=0
                                        continue
                                if self.flag==0:
                                        self.fp1=open("file/login_info.db","wb")
                                        self.x1=self.text1.get()
                                        self.x2=self.text2.get()
                                        self.x3=self.text3.get()
                                        self.x4=self.text4.get()
                                        self.x5="AOJPJ201900"+str(value+1)
                                        self.samp={    'Name':self.x1,
                                                                                'Password':self.x2,
                                                                                'Email id':self.x3,
                                                                                 'Phone Number':self.x4,
                                                                                'Account_Number': self.x5,
                                                                                'Opening_Balance':interface.j,
                                                       'Closing_Balance':interface.closing
                                                       
                                                             }
                                        self.read[str(value+1)]=self.samp
                                    
                                        js.dump(self.read,self.fp1)
                                        self.fp1.close()
                                        mb.showinfo("","ACCOUNT CREATED.")
                                        obj1.reset()
                                        obj1.info()
                                if self.flag==1:
                                        mb.showwarning("WARNING!!!","USERNAME ALREADY EXISTS!!")
                                                                            

        
    def file_login(self):
        self.text14.delete("1.0",END)
        self.text14.insert(END,"\t\t\tINFORMATION")
        if interface.i==1:
            if self.text1.get()!="":
                if self.text2.get()!="":
                    if self.text3.get()!="":
                        if self.text4.get()!="":
                                obj1.file_login_system()
                                
                                
                        else:
                            mb.showwarning("WARNING!!!","EMPTY PHONE NUMBER FIELD!")
                    else:
                             mb.showwarning("WARNING!!!","EMPTY EMAIL ID FIELD!")
                else:
                    mb.showwarning("WARNING!!!","EMPTY PASSWORD FIELD!")
            else:
                mb.showwarning("WARNING!!!","EMPTY USERNAME FIELD!")
        elif interface.i==2:
            self.fp1=open("file/login_info.db")
            self.read1=js.load(self.fp1)
            self.fp1.close()
            self.bunch=list(self.read1.keys())
            for i in self.bunch:
                if self.text5.get()==self.read1[i]['Name']:
                    if self.text6.get()==self.read1[i]['Password']:
                        if self.text7.get()==self.read1[i]['Account_Number']:
                            if self.text8.get()==self.read1[i]['Email id']:
                                    self.count=i
                                    mb.showinfo("INFO!!!!","SUCCESSFULLY DONE!!!!!")
                                    self.top.withdraw()
                                    obj1.mainpage()
                                    
                                    obj1.reset()
                            else:
                                mb.showwarning("WARNING!!!","INVALID EMAIL ID!")
                        else:
                                 mb.showwarning("WARNING!!!","INVALID ACCOUNT NUMBER!")
                    else:
                        mb.showwarning("WARNING!!!","INVALID PASSWORD!")
                else:
                    if i==self.bunch[-1]:
                        mb.showwarning("WARNING!!!","INVALID USERNAME!")
                
                
    def info(self):
        string="\n -_-  Your Account has been Created.\n -_- Your Account Number Is {} \n\t\t^_^Thank You for using our Services.^_^".format(self.x5)
        
        self.text14.insert(END,string)
    def reset(self):
        if interface.i==1:
            self.text1.delete(0,END)
            self.text2.delete(0,END)
            self.text3.delete(0,END)
            self.text4.delete(0,END)
        elif interface.i==2:
            self.text5.delete(0,END)
            self.text6.delete(0,END)
            self.text7.delete(0,END)
            self.text8.delete(0,END)
        
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def mainpage(self):
        
        self.top1=Tk()
        self.top1.configure(background='#111')
        self.top1.geometry("1350x730+0+0")
        self.top1.resizable(False,False)
        self.top1.title("Bank Application")
        obj1.main_frame()
        obj1.main_label()
        obj1.main_text()
        obj1.main_entry()
        obj1.main_button()
        obj1.retrival()
        self.top1.mainloop()
    def main_frame(self):
        self.mframe1=Frame(self.top1,width=1350,height=70,bg="#A17C46",bd=0)
        self.mframe1.place(relx=0,rely=0)
    def main_label(self):
        self.mlabel6=Label(self.mframe1,width=45,bd=0,bg="#A17C46",fg="#111",text="BANK MANAGEMENT",font=("arial",30,"bold"))
        self.mlabel6.place(relx=.1,rely=.2)
        for i in range(1,4):
            self.mlabeli=Label(self.top1,width=7,height=60,bd=0,bg="#333")
            self.mlabeli.place(relx=.08*i+.65,rely=.1)

        

        self.mlabel6=Label(self.top1,width=45,height=25,bd=0,bg="#A17C46")
        self.mlabel6.place(relx=.71,rely=.295)

        self.mlabel7=Label(self.top1,text="NAME                           :",width=17,height=2,bd=1,bg="#111",fg="#A17C46",font=("arial",12,"bold"))
        self.mlabel7.place(relx=.07,rely=.31)

        self.mlabel8=Label(self.top1,text="PASSWORD               :",width=17,height=2,bd=1,bg="#111",fg="#A17C46",font=("arial",12,"bold"))
        self.mlabel8.place(relx=.070,rely=.36)

        self.mlabel9=Label(self.top1,text="EMAIL ID                      :",width=17,height=2,bd=1,bg="#111",fg="#A17C46",font=("arial",12,"bold"))
        self.mlabel9.place(relx=.069,rely=.41)

        self.mlabel10=Label(self.top1,text="PHONE NUMBER      :",width=17,height=1,bg="#111",bd=0,fg="#A17C46",font=("arial",12,"bold"))
        self.mlabel10.place(relx=.07,rely=.47)

        self.mlabel11=Label(self.top1,width=17,text="ACCOUNT NUMBER :",height=1,bg="#111",bd=0,fg="#A17C46",font=("arial",12,"bold"))
        self.mlabel11.place(relx=.07,rely=.52)

        self.mlabel12=Label(self.top1,width=17,text="OPENING BALANCE :",height=1,bg="#111",bd=0,fg="#A17C46",font=("arial",12,"bold"))
        self.mlabel12.place(relx=.07,rely=.57)

        self.mlabel13=Label(self.top1,width=17,text="CLOSING BALANCE :",height=1,bg="#111",bd=0,fg="#A17C46",font=("arial",12,"bold"))
        self.mlabel13.place(relx=.07,rely=.62)

        self.mlabel14=Label(self.top1,width=17,text="DEBIT",height=1,fg="#111",bd=0,bg="#A17C46",font=("arial",12,"bold underline"))
        self.mlabel14.place(relx=.76,rely=.32)

        self.mlabel15=Label(self.top1,width=17,text="DEPOSIT",height=1,fg="#111",bd=0,bg="#A17C46",font=("arial",12,"bold underline"))
        self.mlabel15.place(relx=.76,rely=.44)

    def main_text(self):
        self.mtext14=Text(self.top1,width=60,height=5,bg="#111",fg="#666",bd=2,font=("arial",12,"bold "),relief=RAISED)
        self.mtext14.place(relx=.25,rely=.88)
        self.mtext14.insert(END,"\t\t\tINFORMATION\n\n 1. Opening Balance should not be less than INR 10,000.\n")

        self.mtext15=Text(self.top1,width=28,height=1,bg="#111",fg="#666",bd=0,font=("arial",12,"bold "),relief=RAISED)
        self.mtext15.place(relx=.23,rely=.31)
        self.mtext16=Text(self.top1,width=28,height=1,bg="#111",fg="#666",bd=0,font=("arial",12,"bold "),relief=RAISED)
        self.mtext16.place(relx=.23,rely=.36)
        self.mtext17=Text(self.top1,width=28,height=1,bg="#111",fg="#666",bd=0,font=("arial",12,"bold "),relief=RAISED)
        self.mtext17.place(relx=.23,rely=.41)
        self.mtext18=Text(self.top1,width=28,height=1,bg="#111",fg="#666",bd=0,font=("arial",12,"bold "),relief=RAISED)
        self.mtext18.place(relx=.23,rely=.47)
        self.mtext19=Text(self.top1,width=28,height=1,bg="#111",fg="#666",bd=0,font=("arial",12,"bold "),relief=RAISED)
        self.mtext19.place(relx=.23,rely=.52)
        self.mtext20=Text(self.top1,width=28,height=1,bg="#111",fg="#666",bd=0,font=("arial",12,"bold "),relief=RAISED)
        self.mtext20.place(relx=.23,rely=.57)
        self.mtext21=Text(self.top1,width=28,height=1,bg="#111",fg="#666",bd=0,font=("arial",12,"bold "),relief=RAISED)
        self.mtext21.place(relx=.23,rely=.62)
    def main_entry(self):
        self.mentry1=Entry(self.top1,width=28,fg="#666",bg="#111",bd=2,font=("arial",14,"bold "),relief=RAISED)
        self.mentry1.place(relx=.712,rely=.36)

        self.mentry2=Entry(self.top1,width=28,fg="#666",bg="#111",bd=2,font=("arial",14,"bold "),relief=RAISED)
        self.mentry2.place(relx=.712,rely=.48)
    def main_button(self):
        self.mbutton1=Label(self.top1,width=12,text="CHECKOUT",height=2,relief="raised",bd=2,fg="#111",bg="#A17C46",font=("arial",14,"bold underline"))
        self.mbutton1.place(relx=.77,rely=.55)

        self.mbutton3=Button(self.top1,cursor="arrow",text="FORGOT PASSWORD?",bd=0,bg="#A17C46",width=18,font=("arial",10,"bold underline"),fg="#111",\
                             activebackground="#111",command=obj1.forgot_password)
        self.mbutton3.place(relx=.78,rely=.77)
    def retrival(self):
         self.fp1=open("file/login_info.db")
         self.fpread=js.load(self.fp1)
         self.fp1.close()
         
         self.mtext15.insert(END,self.fpread[self.count]['Name'])
         self.mtext16.insert(END,self.fpread[self.count]['Password'])
         self.mtext17.insert(END,self.fpread[self.count]['Email id'])
         self.mtext18.insert(END,self.fpread[self.count]['Phone Number'])
         self.mtext19.insert(END,self.fpread[self.count]['Account_Number'])
         self.mtext20.insert(END,self.fpread[self.count]['Opening_Balance'])
         self.mtext21.insert(END,self.fpread[self.count]['Closing_Balance'])
         
obj1=interface()
obj1.master()

