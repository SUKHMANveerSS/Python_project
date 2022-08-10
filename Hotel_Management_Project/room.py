from tkinter import*
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+240+220")

        #=====variables====
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_actualtotal=StringVar()
        self.var_taxes=StringVar()
        self.var_total=StringVar()


        #=========Title================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("Bahnschrift SemiBold",20,),bg="black",fg="tan",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=58)

        #======= labelFrame =====
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #======== labels and entrys =======
        #CustContact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
       
        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",12,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)

        #Fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_Contact,text="Fetch Data",font=("arial",10,"bold"),bg="black",fg="tan",width=8)
        btnFetchData.place(x=340,y=4)

        #Check_In Date
        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_In Date: ",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #Check_Out Date
        lbl_Check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_Out Date:",padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txt_Check_out.grid(row=2,column=1)

        #Room Type
        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        rows1=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=rows1
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Available room
        lblRoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Available Room:",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        #txtRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        #Meal
        lblMeal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)

        #No Of days
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="No. Of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        #Sub Total
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="SubTotal:",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)

        #taxes
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Taxes:",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_taxes,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)

        #Total Cost
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        #===Bill button===
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="tan",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        #===== btns =====
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=48)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.Update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #======== tabel frame search system==========
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIew Deatils And Seaarch System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid (row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_Serach=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Serach["value"]=("Contact","Room")
        combo_Serach.current(0)
        combo_Serach.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

         #======== Show data Table =======
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)  

        scroll_x.config(command=self.room_table.xview)    
        scroll_y.config(command=self.room_table.yview)    
        self.room_table['columns']=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays")
        self.room_table.heading("contact",text="Contact")   
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No.")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")
       
        

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
    #======Add data========
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
          messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                    self.var_contact.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get()

                                                                                       ))
                                                                                    
                conn.commit()
                self.fetch_data()
                conn.close()                                                                    
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)  
    #====Fetch data====
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()    
        conn.close()   
    
    #getcursor
    def get_cuersor(self,event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]    

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])   

    #==Update Function========
    def Update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
            my_cursor=conn.cursor()
            my_cursor.execute("Update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                                
                                                                                                                
                                                                                                                self.var_checkin.get(),
                                                                                                                self.var_checkout.get(),
                                                                                                                self.var_roomtype.get(),
                                                                                                                self.var_roomavailable.get(),
                                                                                                                self.var_meal.get(),
                                                                                                                self.var_noofdays.get(),
                                                                                                                self.var_contact.get()
                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details has been Updated successfully",parent=self.root)

    #===Delete Function=======
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do You Want To Delete this Customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()        

    #====Reset Function=====
    def reset(self):  
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")  
        self.var_actualtotal.set("")
        self.var_taxes.set("")
        self.var_total.set("") 
  
                  
    
        
    #============All Data fetch=========
    def Fetch_Contact(self):
      if self.var_contact.get()=="":
          messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        
      else:
          conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
          my_cursor=conn.cursor()      
          query=("select name from customer where mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()

          if row==None:
             messagebox.showerror("Error","This Number not Found",parent=self.root)
          else:
             conn.commit()
             conn.close()

             showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)  
             showDataframe.place(x=450,y=55,width=300,height=180)

             lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
             lblName.place(x=0,y=0)

             lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
             lbl.place(x=90,y=0)

             #==gender====
             conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
             my_cursor=conn.cursor()      
             query=("select gender from customer where mobile=%s")
             value=(self.var_contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()

             lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
             lblGender.place(x=0,y=30)

             lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
             lbl2.place(x=90,y=30)
             
             #===email=====
             conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
             my_cursor=conn.cursor()      
             query=("select email from customer where mobile=%s")
             value=(self.var_contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()

             lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
             lblEmail.place(x=0,y=60)

             lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
             lbl3.place(x=90,y=60)

             #====nationality======
             conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
             my_cursor=conn.cursor()      
             query=("select nationality from customer where mobile=%s")
             value=(self.var_contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()

             lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
             lblNationality.place(x=0,y=90)

             lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
             lbl4.place(x=90,y=90)

             #====address=====
             conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
             my_cursor=conn.cursor()      
             query=("select address from customer where mobile=%s")
             value=(self.var_contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()

             lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
             lbladdress.place(x=0,y=120)

             lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
             lbl5.place(x=90,y=120)

    #search system
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_manage")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()    
        conn.close()    
                  

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury Suite"):
            q1=float(1000)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_taxes.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(400)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_taxes.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)    

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_taxes.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)        
            






             


            
if __name__ == "__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()

