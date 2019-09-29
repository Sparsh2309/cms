from tkinter import *
from tkinter import messagebox
import Cms
def showCust_search(data):
    root1 = Tk()
    root1.title("Customer Management System")
    lblId1 = Label(root1, text="Customer ID", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",
                   fg='mint cream')
    lblId1.grid(row=0, column=0)
    lblAge1 = Label(root1, text="Customer Age", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",
                    fg='mint cream')
    lblAge1.grid(row=0, column=1)
    lblName1 = Label(root1, text="Customer Name", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",
                     fg='mint cream')
    lblName1.grid(row=0, column=2)
    lblEmail1 = Label(root1, text="Customer Email", font=('Comic Sans MS', 10, 'bold', 'italic'), width=30, bg="blue",
                      fg='mint cream')
    lblEmail1.grid(row=0, column=3)
    lblMobile1 = Label(root1, text="Customer Mobile Number", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20,
                       bg="blue", fg='mint cream')
    lblMobile1.grid(row=0, column=4)
    lblCity1 = Label(root1, text="Customer City", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",
                     fg='mint cream')
    lblCity1.grid(row=0, column=5)
    lblState1 = Label(root1, text="Customer State", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",
                      fg='mint cream')
    lblState1.grid(row=0, column=6)
    lblPincode1 = Label(root1, text="Customer Pincode", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20,
                        bg="blue", fg='mint cream')
    lblPincode1.grid(row=0, column=7)
    i = 1
    for e in data:
        lblId2 = Label(root1, text=e[0], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',
                       fg='blue')
        lblId2.grid(row=i, column=0)
        lblAge2 = Label(root1, text=e[1], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',
                        fg='blue')
        lblAge2.grid(row=i, column=1)
        lblName2 = Label(root1, text=e[2], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',
                         fg='blue')
        lblName2.grid(row=i, column=2)
        lblEmail2 = Label(root1, text=e[3], font=('Comic Sans MS', 10, 'bold', 'italic'), width=30, bg='mint cream',
                          fg='blue')
        lblEmail2.grid(row=i, column=3)
        lblMobile2 = Label(root1, text=e[4], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',
                           fg='blue')
        lblMobile2.grid(row=i, column=4)
        lblCity2 = Label(root1, text=e[5], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',
                         fg='blue')
        lblCity2.grid(row=i, column=5)
        lblState2 = Label(root1, text=e[6], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',
                          fg='blue')
        lblState2.grid(row=i, column=6)
        lblPincode2 = Label(root1, text=e[7], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',
                            fg='blue')
        lblPincode2.grid(row=i, column=7)
        i += 1


def CmsMain_exit():
    root.destroy()


def CmsAddCus():
    cus = Cms.Customer()
    def cmsMain():
        root2.destroy()

    def SumbitBtn():
        cus1 = Cms.Customer()
        cus1.age = varAge.get()
        cus1.name = varName.get()
        cus1.email = varEmail.get()
        cus1.mobile = varMobile.get()
        cus1.city = varCity.get()
        cus1.state = varState.get()
        cus1.pinCode = varPincode.get()
        cus1.addCust()
        messagebox.showinfo("CMS", "Cust Added Successfully")

    root2 = Toplevel()
    root2.geometry("600x400")
    root2.title('ADD NEW CUSTOMER')
    root2.config(bg='steel blue2')
    lblName = Label(root2, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 7, "bold",))
    lblName.grid(row=0, column=1)

    lblAge = Label(root2, text="Enter Your Age:", font=16, bg='steel blue2', fg='black')
    lblAge.grid(row=1, column=0)
    varAge = StringVar()
    entryAge = Entry(root2, font=16, textvariable=varAge)
    entryAge.grid(row=1, column=1)

    lblName = Label(root2, text="Enter Your Name:", font=16, bg='steel blue2', fg='black')
    lblName.grid(row=2, column=0)
    varName = StringVar()
    entryName = Entry(root2, font=16, textvariable=varName)
    entryName.grid(row=2, column=1)

    lblEmail = Label(root2, text="Enter Your Email:", font=16, bg='steel blue2', fg='black')
    lblEmail.grid(row=3, column=0)
    varEmail = StringVar()
    entryEmail = Entry(root2, font=16, textvariable=varEmail)
    entryEmail.grid(row=3, column=1)

    lblMobile = Label(root2, text="Enter Your Mobile:", font=16, bg='steel blue2', fg='black')
    lblMobile.grid(row=4, column=0)
    varMobile = StringVar()
    entryMobile = Entry(root2, font=16, textvariable=varMobile)
    entryMobile.grid(row=4, column=1)

    lblCity = Label(root2, text="Enter Your City:", font=16, bg='steel blue2', fg='black')
    lblCity.grid(row=5, column=0)
    varCity = StringVar()
    entryCity = Entry(root2, font=16, textvariable=varCity)
    entryCity.grid(row=5, column=1)

    lblState = Label(root2, text="Enter Your State:", font=16, bg='steel blue2', fg='black')
    lblState.grid(row=6, column=0)
    varState = StringVar()
    entryState = Entry(root2, font=16, textvariable=varState)
    entryState.grid(row=6, column=1)

    lblPincode = Label(root2, text="Enter Your pincode:", font=16, bg='steel blue2', fg='black')
    lblPincode.grid(row=7, column=0)
    varPincode = StringVar()
    entryPincode = Entry(root2, font=16, textvariable=varPincode)
    entryPincode.grid(row=7, column=1)

    btnSubmit = Button(root2, text="Submit", font=16, bg='green', fg="black", command=SumbitBtn)
    btnSubmit.grid(row=8, column=1)
    btnSubmit = Button(root2, text="Back to menu", font=16, bg='green', fg="black", command=cmsMain)
    btnSubmit.grid(row=8, column=0)
    lblName = Label(root2, text="Created by Sparsh & team", font=('Arial', 7, 'bold'))
    lblName.grid(row=9, column=1)

    root2.mainloop()

def searchById_click():
    def searchById():
        cus = Cms.Customer()
        cus.id = int(varId2.get())
        data=cus.searchById()
        showCust_search(data)
    def exitToMenu():
        root2.destroy()

    root2 = Toplevel()
    root2.geometry("600x500")
    root2.title('SEARCH CUSTOMER BY ID')
    root2.config(bg='steel blue2')
    lblName3 = Label(root2, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 8, "bold"),fg='steel blue2')
    lblName3.grid(row=0, column=1)

    lblId2 = Label(root2, text="Enter the id:", font=16, bg='steel blue2', fg='black')
    lblId2.grid(row=1, column=0)
    varId2 = StringVar()
    entryId2 = Entry(root2, font=16, textvariable=varId2)
    entryId2.grid(row=1, column=1)
    btnSubmit4 = Button(root2, text="SUBMIT", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='light coral', command=searchById)
    btnSubmit4.grid(row=2, column=1)
    btnSubmit4.config(height=2, width=15)
    btnSubmit4 = Button(root2, text="EXIT TO MAIN MENU", font=('Comic Sans MS', 8, 'bold', 'italic'), bg='orange red2',
                        fg='light coral', command=exitToMenu)
    btnSubmit4.grid(row=2, column=0)
    btnSubmit4.config(height=2, width=15)
    lblName = Label(root2, text="Created by Sparsh & team", font=('Arial', 8, 'bold'),fg='steel blue2')
    lblName.grid(row=3, column=1)
    root2.config(bg='steel blue2')
def searchByName_click():
    def searchName():
        cus = Cms.Customer()
        cus.name = varId2.get()
        data=cus.searchByName()
        showCust_search(data)
    def exitToMenu():#debug
        root2.destroy()

    root2 = Toplevel()
    root2.geometry("600x500")
    root2.title('SEARCH CUSTOMER BY NAME')
    root2.config(bg='steel blue2')
    lblName3 = Label(root2, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 8, "bold"),fg='steel blue2')
    lblName3.grid(row=0, column=1)

    lblId2 = Label(root2, text="Enter Name of customer:", font=16, bg='steel blue2', fg='black')
    lblId2.grid(row=1, column=0)
    varId2 = StringVar()
    entryId2 = Entry(root2, font=16, textvariable=varId2)
    entryId2.grid(row=1, column=1)
    btnSubmit4 = Button(root2, text="SUBMIT", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=searchName)
    btnSubmit4.grid(row=2, column=1)
    btnSubmit4.config(height=2, width=15)
    btnSubmit4 = Button(root2, text="EXIT TO MAIN MENU", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='orange red2',
                        fg='light coral', command=exitToMenu)
    btnSubmit4.grid(row=3, column=1)
    btnSubmit4.config(height=2, width=15)
    lblName = Label(root2, text="Created by Sparsh & team", font=('Arial', 8, 'bold'))
    lblName.grid(row=4, column=1)
    root2.config(bg='steel blue2')
def searchByCity_click():
    def searchCity():
        cus = Cms.Customer()
        cus.city = varId2.get()
        data=cus.searchByCity()
        showCust_search(data)
    def exitToMenu():
        root2.destroy()

    root2 = Toplevel()
    root2.geometry("600x500")
    root2.title('SEARCH CUSTOMER BY CITY')
    root2.config(bg='steel blue2')
    lblName3 = Label(root2, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 16, "bold"),fg='steel blue2')
    lblName3.grid(row=0, column=1)

    lblId2 = Label(root2, text="Enter the city of customer:", font=16, bg='steel blue2', fg='black')
    lblId2.grid(row=1, column=0)
    varId2 = StringVar()
    entryId2 = Entry(root2, font=16, textvariable=varId2)
    entryId2.grid(row=1, column=1)
    btnSubmit4 = Button(root2, text="SUBMIT", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=searchCity)
    btnSubmit4.grid(row=2, column=1)
    btnSubmit4.config(height=3, width=25)
    btnSubmit4 = Button(root2, text="EXIT TO MAIN MENU", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='orange red',
                        fg='light coral', command=exitToMenu)
    btnSubmit4.grid(row=3, column=1)
    btnSubmit4.config(height=2, width=15)
    lblName = Label(root2, text="Created by Sparsh & team", font=('Arial', 8, 'bold'),fg='steel blue2')
    lblName.grid(row=4, column=1)
    root2.config(bg='steel blue2')

def btnSearchCust_click():
    def Main_back():
        root3.destroy()
    root3 = Toplevel()
    root3.geometry('500x450+50+50')
    root3.title("Delete Customer")
    lblName1 = Label(root3, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 16, "bold"),fg='steel blue2')
    lblName1.grid(row=0, column=5)
    lblName2 = Label(root3, text=" SELECT A OPTION TO DELETE CUSTOMER ", font=("Arial", 16, "bold"), fg="red")
    lblName2.grid(row=1, column=5)
    btnSubmit1 = Button(root3, text="Search by id", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=searchById_click)
    btnSubmit1.grid(row=2, column=5)
    btnSubmit1.config(height=3, width=25)
    btnSubmit2 = Button(root3, text="Search by name", font=('Comic Sans MS', 10, 'bold', 'italic'),
                        bg='mint cream',
                        fg='steel blue2',command=searchByName_click)
    btnSubmit2.grid(row=3, column=5)
    btnSubmit2.config(height=3, width=25)
    btnSubmit3 = Button(root3, text="search by city", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2',command=searchByCity_click)
    btnSubmit3.grid(row=4, column=5)
    btnSubmit3.config(height=3, width=25)
    btnSubmit4 = Button(root3, text="BACK TO MENU", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='orange red2',
                        fg='light coral', command=Main_back)
    btnSubmit4.grid(row=5, column=5)
    btnSubmit4.config(height=3, width=25)
    lblName = Label(root3, text="Created by Sparsh & team", font=('Arial', 16, 'bold'))
    lblName.grid(row=6, column=5)
    root3.config(bg='steel blue2')
    root3.mainloop()


def updatedAllId_click():
    def modifyById():
        cus = Cms.Customer()
        cus.id = varId2.get()
        cus.modifyCust()
        messagebox.showinfo("CMS", f"Customer updated Successfully")
    def exitToMenu():
        root2.destroy()

    root2 = Toplevel()
    root2.geometry("800x700")
    root2.title('UPDATE CUSTOMER BY ID')
    root2.config(bg='steel blue2')
    lblName3 = Label(root2, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 7, "bold"),fg='steel blue2')
    lblName3.grid(row=0, column=1)

    lblId2 = Label(root2, text="Enter the id:", font=16, bg='steel blue2', fg='black')
    lblId2.grid(row=1, column=0)
    varId2 = StringVar()
    entryId2 = Entry(root2, font=16, textvariable=varId2)
    entryId2.grid(row=1, column=1)
    lblAge = Label(root2, text="Enter Your Age:", font=16, bg='steel blue2', fg='black')
    lblAge.grid(row=2, column=0)
    varAge = StringVar()
    entryAge = Entry(root2, font=16, textvariable=varAge)
    entryAge.grid(row=2, column=1)

    lblName = Label(root2, text="Enter Your Name:", font=16, bg='steel blue2', fg='black')
    lblName.grid(row=3, column=0)
    varName = StringVar()
    entryName = Entry(root2, font=16, textvariable=varName)
    entryName.grid(row=3, column=1)

    lblEmail = Label(root2, text="Enter Your Email:", font=16, bg='steel blue2', fg='black')
    lblEmail.grid(row=4, column=0)
    varEmail = StringVar()
    entryEmail = Entry(root2, font=16, textvariable=varEmail)
    entryEmail.grid(row=4, column=1)

    lblMobile = Label(root2, text="Enter Your Mobile:", font=16, bg='steel blue2', fg='black')
    lblMobile.grid(row=5, column=0)
    varMobile = StringVar()
    entryMobile = Entry(root2, font=16, textvariable=varMobile)
    entryMobile.grid(row=5, column=1)

    lblCity = Label(root2, text="Enter Your City:", font=16, bg='steel blue2', fg='black')
    lblCity.grid(row=6, column=0)
    varCity = StringVar()
    entryCity = Entry(root2, font=16, textvariable=varCity)
    entryCity.grid(row=6, column=1)

    lblState = Label(root2, text="Enter Your State:", font=16, bg='steel blue2', fg='black')
    lblState.grid(row=7, column=0)
    varState = StringVar()
    entryState = Entry(root2, font=16, textvariable=varState)
    entryState.grid(row=7, column=1)

    lblPincode = Label(root2, text="Enter Your pincode:", font=16, bg='steel blue2', fg='black')
    lblPincode.grid(row=8, column=0)
    varPincode = StringVar()
    entryPincode = Entry(root2, font=16, textvariable=varPincode)
    entryPincode.grid(row=8, column=1)

    btnSubmit = Button(root2, text="Submit", font=16, bg='light green', fg="white", command=modifyById)
    btnSubmit.grid(row=9, column=1)
    btnSubmit = Button(root2, text="Back to menu", font=16, bg='orange red2', fg="white", command=exitToMenu)
    btnSubmit.grid(row=9, column=0)
    lblName = Label(root2, text="Created by Sparsh & team", font=('Arial', 7, 'bold'),fg='steel blue2')
    lblName.grid(row=10, column=1)

def modifyByMobile_click():
    def modifyMobile():
        cus = Cms.Customer()
        cus.mobile = varOldMN.get()
        MN=varNewMN.get()
        cus.modifyMobile(MN)
        messagebox.showinfo("CMS", f"Mobile Number Updated Successfully")
    def exitToMenu():
        root2.destroy()

    root2 = Toplevel()
    root2.geometry("600x500")
    root2.title('MODIFY CUSTOMER"S MOBILE NUMBER')
    root2.config(bg='steel blue2')
    lblName3 = Label(root2, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 8, "bold"),fg='steel blue2')
    lblName3.grid(row=0, column=1)

    lblOldMN = Label(root2, text="Enter old mobile number:", font=16, bg='steel blue2', fg='black')
    lblOldMN.grid(row=1, column=0)
    varOldMN = StringVar()
    entryOldMN = Entry(root2, font=16, textvariable=varOldMN)
    entryOldMN.grid(row=1, column=1)
    lblNewMn = Label(root2, text="Enter new mobile number:", font=16, bg='steel blue2', fg='black')
    lblNewMn.grid(row=2, column=0)
    varNewMN = StringVar()
    entryNewMN = Entry(root2, font=16, textvariable=varNewMN)
    entryNewMN.grid(row=2, column=1)
    btnSubmit4 = Button(root2, text="SUBMIT", font=('Comic Sans MS', 8, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=modifyMobile)
    btnSubmit4.grid(row=3, column=1)
    btnSubmit4.config(height=2, width=15)
    btnSubmit4 = Button(root2, text="EXIT TO MAIN MENU", font=('Comic Sans MS', 6, 'bold', 'italic'), bg='orange red2',
                        fg='white', command=exitToMenu)
    btnSubmit4.grid(row=4, column=1)
    btnSubmit4.config(height=2, width=15)
    lblName = Label(root2, text="Created by Sparsh & team", font=('Arial', 8, 'bold'),fg='steel blue2')
    lblName.grid(row=5, column=1)
    root2.config(bg='steel blue2')
def modifyByEmail_click():
    def updateEmail():
        cus = Cms.Customer()
        cus.email = varEmailOld.get()
        newEmail = varEmailNew
        cus.modifyEmail(newEmail)
        messagebox.showinfo("CMS", f"Email modified Successfully")
    def exitToMenu():
        root2.destroy()

    root2 = Toplevel()
    root2.geometry("600x500")
    root2.title('MODIFY CUSTOMER"S EMAIL')
    root2.config(bg='steel blue2')
    lblName3 = Label(root2, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 8, "bold"),fg='steel blue2')
    lblName3.grid(row=0, column=1)

    lblId2 = Label(root2, text="Enter the old email:", font=16, bg='steel blue2', fg='black')
    lblId2.grid(row=1, column=0)
    varEmailOld = StringVar()
    entryId2 = Entry(root2, font=16, textvariable=varEmailOld)
    entryId2.grid(row=1, column=1)
    lblId3 = Label(root2, text="Enter new email:", font=16, bg='steel blue2', fg='black')
    lblId2.grid(row=2, column=0)
    varEmailNew = StringVar()
    entryId2 = Entry(root2, font=16, textvariable=varEmailNew)
    entryId2.grid(row=2, column=1)
    btnSubmit4 = Button(root2, text="SUBMIT", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=updateEmail)
    btnSubmit4.grid(row=3, column=1)
    btnSubmit4.config(height=2, width=15)
    btnSubmit4 = Button(root2, text="EXIT TO MAIN MENU", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='orange red2',
                        fg='steel blue2', command=exitToMenu)
    btnSubmit4.grid(row=3, column=0)
    btnSubmit4.config(height=2, width=15)
    lblName = Label(root2, text="Created by Sparsh & team", font=('Arial', 8, 'bold'),fg='steel blue2')
    lblName.grid(row=4, column=1)
    root2.config(bg='steel blue2')

def btnModifyCust_click():
    def Main_back():
        root3.destroy()
    root3 = Toplevel()
    root3.geometry('500x450+50+50')
    root3.title("Delete Customer")
    lblName1 = Label(root3, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 16, "bold"),fg='steel blue2')
    lblName1.grid(row=0, column=5)
    lblName2 = Label(root3, text=" SELECT A OPTION TO MODIFY CUSTOMER ", font=("Arial", 16, "bold"), fg="red")
    lblName2.grid(row=1, column=5)
    btnSubmit1 = Button(root3, text="Modify all data by id", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=updatedAllId_click)
    btnSubmit1.grid(row=2, column=5)
    btnSubmit1.config(height=3, width=25)
    btnSubmit2 = Button(root3, text="Modify email", font=('Comic Sans MS', 10, 'bold', 'italic'),
                        bg='mint cream',
                        fg='steel blue2',command=modifyByEmail_click)
    btnSubmit2.grid(row=3, column=5)
    btnSubmit2.config(height=3, width=25)
    btnSubmit3 = Button(root3, text="Modify mobile number", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2',command=modifyByMobile_click)
    btnSubmit3.grid(row=4, column=5)
    btnSubmit3.config(height=3, width=25)
    btnSubmit4 = Button(root3, text="BACK TO MENU", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='orange red2',
                        fg='white', command=Main_back)
    btnSubmit4.grid(row=5, column=5)
    btnSubmit4.config(height=3, width=25)
    lblName = Label(root3, text="Created by Sparsh & team", font=('Arial', 16, 'bold'),fg='steel blue2')
    lblName.grid(row=6, column=5)
    root3.config(bg='steel blue2')
    root3.mainloop()


def deleteById_click():
    def DeleteId():
        cus = Cms.Customer()
        cus.id = varId2.get()
        cus.deleteCust()
        messagebox.showinfo("CMS", f"Customer deleted Successfully")
    def exitToMenu():
        root2.destroy()

    root2 = Toplevel()
    root2.geometry("600x500")
    root2.title('DELETE CUSTOMER BY ID')
    root2.config(bg='steel blue2')
    lblName3 = Label(root2, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 16, "bold"),fg='steel blue2')
    lblName3.grid(row=0, column=1)

    lblId2 = Label(root2, text="Enter the id:", font=16, bg='steel blue2', fg='black')
    lblId2.grid(row=1, column=0)
    varId2 = StringVar()
    entryId2 = Entry(root2, font=16, textvariable=varId2)
    entryId2.grid(row=1, column=1)
    btnSubmit4 = Button(root2, text="SUBMIT", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=DeleteId)
    btnSubmit4.grid(row=2, column=1)
    btnSubmit4.config(height=3, width=25)
    btnSubmit4 = Button(root2, text="EXIT TO MAIN MENU", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='orange red2',
                        fg='steel blue2', command=exitToMenu)
    btnSubmit4.grid(row=3, column=1)
    btnSubmit4.config(height=3, width=25)
    lblName = Label(root2, text="Created by Sparsh & team", font=('Arial', 16, 'bold'),fg='steel blue2')
    lblName.grid(row=4, column=1)
    root2.config(bg='steel blue2')
def deleteByMobile_click():
    def DeleteId():
        cus = Cms.Customer()
        cus.mobile = varId2.get()
        cus.searchByMobile()
        cus.deleteCust()
        messagebox.showinfo("CMS", f"Customer deleted Successfully")
    def exitToMenu():
        root2.destroy()

    root2 = Toplevel()
    root2.geometry("600x500")
    root2.title('DELETE CUSTOMER BY ID')
    root2.config(bg='steel blue2')
    lblName3 = Label(root2, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 16, "bold"),fg='steel blue2')
    lblName3.grid(row=0, column=1)

    lblId2 = Label(root2, text="Enter Mobile number of customer:", font=16, bg='steel blue2', fg='black')
    lblId2.grid(row=1, column=0)
    varId2 = StringVar()
    entryId2 = Entry(root2, font=16, textvariable=varId2)
    entryId2.grid(row=1, column=1)
    btnSubmit4 = Button(root2, text="SUBMIT", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=DeleteId)
    btnSubmit4.grid(row=2, column=1)
    btnSubmit4.config(height=3, width=25)
    btnSubmit4 = Button(root2, text="EXIT TO MAIN MENU", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='orange red2',
                        fg='steel blue2', command=exitToMenu)
    btnSubmit4.grid(row=3, column=1)
    btnSubmit4.config(height=3, width=25)
    lblName = Label(root2, text="Created by Sparsh & team", font=('Arial', 16, 'bold'))
    lblName.grid(row=4, column=1)
    root2.config(bg='steel blue2')
def deleteByEmail_click():
    def DeleteId():
        cus = Cms.Customer()
        cus.email = varId2.get()
        cus.searchByEmail()
        cus.deleteCust()
        messagebox.showinfo("CMS", f"Customer deleted Successfully")
    def exitToMenu():
        root2.destroy()

    root2 = Toplevel()
    root2.geometry("600x500")
    root2.title('DELETE CUSTOMER BY ID')
    root2.config(bg='steel blue2')
    lblName3 = Label(root2, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 16, "bold"),fg='steel blue2')
    lblName3.grid(row=0, column=1)

    lblId2 = Label(root2, text="Enter the email of customer:", font=16, bg='steel blue2', fg='black')
    lblId2.grid(row=1, column=0)
    varId2 = StringVar()
    entryId2 = Entry(root2, font=16, textvariable=varId2)
    entryId2.grid(row=1, column=1)
    btnSubmit4 = Button(root2, text="SUBMIT", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=DeleteId)
    btnSubmit4.grid(row=2, column=1)
    btnSubmit4.config(height=3, width=25)
    btnSubmit4 = Button(root2, text="EXIT TO MAIN MENU", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='orange red2',
                        fg='steel blue2', command=exitToMenu)
    btnSubmit4.grid(row=3, column=1)
    btnSubmit4.config(height=3, width=25)
    lblName = Label(root2, text="Created by Sparsh & team", font=('Arial', 16, 'bold'))
    lblName.grid(row=4, column=1)
    root2.config(bg='steel blue2')

def btnDeleteCust_click():
    def Main_back():
        root3.destroy()
    root3 = Toplevel()
    root3.geometry('500x450+50+50')
    root3.title("Delete Customer")
    lblName1 = Label(root3, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 16, "bold"),fg='steel blue2')
    lblName1.grid(row=0, column=5)
    lblName2 = Label(root3, text=" SELECT A OPTION TO DELETE CUSTOMER ", font=("Arial", 16, "bold"), fg="red")
    lblName2.grid(row=1, column=5)
    btnSubmit1 = Button(root3, text="Delete by id", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=deleteById_click)
    btnSubmit1.grid(row=2, column=5)
    btnSubmit1.config(height=3, width=25)
    btnSubmit2 = Button(root3, text="Delete by mobile number", font=('Comic Sans MS', 10, 'bold', 'italic'),
                        bg='mint cream',
                        fg='steel blue2',command=deleteByMobile_click)
    btnSubmit2.grid(row=3, column=5)
    btnSubmit2.config(height=3, width=25)
    btnSubmit3 = Button(root3, text="Delete by email", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='orange red2',
                        fg='light coral',command=deleteByEmail_click)
    btnSubmit3.grid(row=4, column=5)
    btnSubmit3.config(height=3, width=25)
    btnSubmit4 = Button(root3, text="BACK TO MENU", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=Main_back)
    btnSubmit4.grid(row=5, column=5)
    btnSubmit4.config(height=3, width=25)
    lblName = Label(root3, text="Created by Sparsh & team", font=('Arial', 16, 'bold'),fg='steel blue2')
    lblName.grid(row=6, column=5)
    root3.config(bg='steel blue2')
    root3.mainloop()


def btnDisplayAllCust_Click():
    root1 = Tk()
    root1.title("Customer Management System")
    lblId1 = Label(root1, text="Customer ID", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",fg='mint cream')
    lblId1.grid(row=0, column=0)
    lblAge1 = Label(root1, text="Customer Age", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",fg='mint cream')
    lblAge1.grid(row=0, column=1)
    lblName1 = Label(root1, text="Customer Name", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",fg='mint cream')
    lblName1.grid(row=0, column=2)
    lblEmail1 = Label(root1, text="Customer Email", font=('Comic Sans MS', 10, 'bold', 'italic'), width=30, bg="blue",fg='mint cream')
    lblEmail1.grid(row=0, column=3)
    lblMobile1 = Label(root1, text="Customer Mobile Number", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",fg='mint cream')
    lblMobile1.grid(row=0, column=4)
    lblCity1 = Label(root1, text="Customer City", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",fg='mint cream')
    lblCity1.grid(row=0, column=5)
    lblState1 = Label(root1, text="Customer State", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",fg='mint cream')
    lblState1.grid(row=0, column=6)
    lblPincode1 = Label(root1, text="Customer Pincode", font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg="blue",fg='mint cream')
    lblPincode1.grid(row=0, column=7)
    i = 1
    data = Cms.Customer.loadAll()
    for e in data:
        lblId2 = Label(root1, text=e[0], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',fg='blue')
        lblId2.grid(row=i, column=0)
        lblAge2 = Label(root1, text=e[1], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',fg='blue')
        lblAge2.grid(row=i, column=1)
        lblName2 = Label(root1, text=e[2], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',fg='blue')
        lblName2.grid(row=i, column=2)
        lblEmail2 = Label(root1, text=e[3], font=('Comic Sans MS', 10, 'bold', 'italic'), width=30, bg='mint cream',fg='blue')
        lblEmail2.grid(row=i, column=3)
        lblMobile2 = Label(root1, text=e[4], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',fg='blue')
        lblMobile2.grid(row=i, column=4)
        lblCity2 = Label(root1, text=e[5], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',fg='blue')
        lblCity2.grid(row=i, column=5)
        lblState2 = Label(root1, text=e[6], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',fg='blue')
        lblState2.grid(row=i, column=6)
        lblPincode2 = Label(root1, text=e[7], font=('Comic Sans MS', 10, 'bold', 'italic'), width=20, bg='mint cream',fg='blue')
        lblPincode2.grid(row=i, column=7)
        i += 1


def LoadInFile_click():
    Cms.Customer.createFile()
    messagebox.showinfo("Customer Management System", "File Loaded In File Successfully")


def GenReport_Click():
    Cms.Customer.reportFile()
    messagebox.showinfo("Customer Management System", "Report Generated Successfully")


def btnExit_Click():
    messagebox.showinfo("My CMS", "Thanks for using my CMS")
    Cms.Customer.exit()
    root.destroy()

if __name__ == "__main__":
    root = Tk()
    root.geometry('695x720+50+50')
    root.title("Customer Management System")
    lblName = Label(root, text=" WELCOME TO CUSTOMER MANAGEMENT SYSTEM ", font=("Arial", 20, "bold"),fg='steel blue2')
    lblName.grid(row=0, column=5)
    btnSubmit1 = Button(root, text="Add Customer", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=CmsAddCus)
    btnSubmit1.grid(row=1, column=5)
    btnSubmit1.config(height=3, width=25)
    btnSubmit2 = Button(root, text="Search Customer", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2',command=btnSearchCust_click)
    btnSubmit2.grid(row=2, column=5)
    btnSubmit2.config(height=3, width=25)
    btnSubmit3 = Button(root, text="Delete Customer", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2', command=btnDeleteCust_click)
    btnSubmit3.grid(row=3, column=5)
    btnSubmit3.config(height=3, width=25)
    btnSubmit4 = Button(root, text="Modify Customer", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='mint cream',
                        fg='steel blue2',command=btnModifyCust_click)
    btnSubmit4.grid(row=4, column=5)
    btnSubmit4.config(height=3, width=25)

    btnSubmit5 = Button(root, text="Display All Customer", font=('Comic Sans MS', 10, 'bold', 'italic'),
                        bg='mint cream',
                        fg='steel blue2', command=btnDisplayAllCust_Click)
    btnSubmit5.grid(row=5, column=5)
    btnSubmit5.config(height=3, width=25)
    btnSubmit6 = Button(root, text="Load Customers In File", font=('Comic Sans MS', 10, 'bold', 'italic'),
                        bg='mint cream',
                        fg='steel blue2', command=LoadInFile_click)
    btnSubmit6.grid(row=6, column=5)
    btnSubmit6.config(height=3, width=25)
    btnSubmit7 = Button(root, text="Generate Customer Report", font=('Comic Sans MS', 10, 'bold', 'italic'),
                        bg='mint cream', fg='steel blue2', command=GenReport_Click)
    btnSubmit7.grid(row=7, column=5)
    btnSubmit7.config(height=3, width=25)
    btnSubmit9 = Button(root, text="EXIT", font=('Comic Sans MS', 10, 'bold', 'italic'), bg='orange red2',
                        fg='mint cream'
                        , command=btnExit_Click)
    btnSubmit9.grid(row=8, column=5)
    btnSubmit9.config(height=3, width=25)
    lblName = Label(root, text="Created by Sparsh & team", font=('Arial', 20, 'bold'),fg='steel blue2')
    lblName.grid(row=9, column=5)
    root.config(bg='steel blue2')
    root.mainloop()
