import pickle
import pymysql

class Customer:
    con = pymysql.connect(host="localhost", user="root", password="span", database="CMS", port=3306)
    mycur = con.cursor()

    def __init__(self):  # constructor
        self.id = "000"
        self.age = '0'
        self.name = "empty"
        self.email = 'example@email.com'
        self.mobile = '9000000000'
        self.city = 'default'
        self.state = 'default'
        self.pinCode = '0'

    def addCust(self):  # use to add customer
        qry = f"insert into cms(age,name,email,mobileno,city,state,pincode) values({self.age},'{self.name}','{self.email}',{self.mobile},'{self.city}','{self.state}',{self.pinCode}) "
        Customer.mycur.execute(qry)
        Customer.con.commit()

    def searchCust(self):  # use to search a particular customer
        qry = f"select * from cms where id = {self.id}"
        Customer.mycur.execute(qry)
        data = Customer.mycur.fetchone()
        return data

    def deleteCust(self):  # use to delete customer
        qry = f"delete from cms where id = {self.id}"
        Customer.mycur.execute(qry)
        Customer.con.commit()

    def modifyCust(self):  # use to modify customer
        qry = f"update cms set age ={self.age},name={self.name},email={self.email},mobileno={self.mobile},city={self.city},state={self.city},pincode={self.pinCode} where id ={self.id}"
        Customer.mycur.execute(qry)
        Customer.con.commit()
    def modifyMobile(self,newMobile):
        data=self.searchByMobile()
        self.id=data[0]
        qry = f"update cms set mobileno='{newMobile}' where id ={self.id}"
        Customer.mycur.execute(qry)
        Customer.con.commit()
    def modifyEmail(self,newEmail):
        data=self.searchByEmail()
        self.id=data[0]
        qry = f"update cms set email='{newEmail}' where id ={self.id}"
        Customer.mycur.execute(qry)
        Customer.con.commit()
    @staticmethod
    def reportFile():
        f = open('customer.txt', "w+")
        qry = "select * from cms"
        Customer.mycur.execute(qry)
        records=Customer.mycur.fetchall()
        for row in records:
            f.write(f'Customer id is: {row[0]} ,age: {row[1]}, name:'
                    f'{row[2]}, email: {row[3]},'
                    f'mobile: {row[4]}, city: {row[5]}'
                    f',state: {row[6]}, pincode: {row[6]}\r\n')
        f.close()


    @staticmethod
    def createFile():
        qry = "select * from cms"
        Customer.mycur.execute(qry)
        records = Customer.mycur.fetchall()
        with open('list_data.pkl', 'wb') as f:
            pickle.dump(records, f)
    def searchById(self):
        qry = f"select * from cms where id = {self.id}"
        Customer.mycur.execute(qry)
        data = Customer.mycur.fetchall()
        return data
    def searchByName(self):
        qry = f"select * from cms where name = '{self.name}'"
        Customer.mycur.execute(qry)
        data = Customer.mycur.fetchall()
        return data
    def searchByCity(self):
        qry = f"select * from cms where city = '{self.city}'"
        Customer.mycur.execute(qry)
        data = Customer.mycur.fetchall()
        return data
    def searchByMobile(self):
        qry = f"select * from cms where mobileno = {self.mobile}"
        Customer.mycur.execute(qry)
        data = Customer.mycur.fetchone()
        return data
    def searchByEmail(self):
        qry = f"select * from cms where email = {self.email}"
        Customer.mycur.execute(qry)
        data = Customer.mycur.fetchone()
        return data
    @staticmethod
    def loadAll():
        qry = f"select * from cms"
        Customer.mycur.execute(qry)
        data = Customer.mycur.fetchall()
        return data
    @staticmethod
    def exit():
        Customer.con.close()
# Pl

def myisalpha(self, word):  # use to check alphabets as well as space " "
        chk = word.lower()
        for letter in word:
            if not letter in "abcdefghijklmnopqrstuvwxyz":
                if not letter in " ":
                    return False
        return True

@property
def emailchecker(self):
    if "@" in self.email:
        if ".com" or ".in" or ".org" or '.' or 'co.in' or '.hm' or '.hu' or '.co.' in self.email:
            if 12 < len(self.email) < 50:
                return True
    else:
        return False



def mobilechecker(self):  # use to check mobile number is in desired formate
    if self.mobile.isnumeric():
        if (len(self.mobile) == 10):
            if not (self.mobile[0] == 0):  # length=10 and not start with 0
                return 1
        else:
            return 0

def agechecker(self):  # use to check age
        if self.age.isnumeric():
            a = int(self.age)
            if a < 100:
                return 1
            else:
                return 0


if __name__=="__main__":
    print("Welcome to Cetpa's CMS")
    while 1:
        print(
            "Press 1 for add customer,2for search ,3 for delete,4 for modify,5 for display all,6 for load in file,"
            "7 for generate report,8 for load from file,9for exit")
        ch = input("Enter your choice: ")
        if ch == "1":
            customer = Customer()

            while 1:
                customer.age = input("Enter customer age: ")
                a = customer.agechecker()
                if a == 1:
                    break
                else:
                    print("age should be in number")
            while 1:
                customer.name = input("Enter customer name: ")
                if customer.myisalpha(customer.name):
                    if len(customer.name) < 40:
                        break
                else:
                    print("Enter you name in proper formate")
            while 1:
                customer.email = input("Enter customer email: ")
                if customer.emailchecker:
                    break
                else:
                    print("Wrong format input as example@example.com")
            while 1:
                customer.mobile = input("Enter mobile number of customer: ")
                a = customer.mobilechecker()
                if a == 1:
                    break
                else:
                    print("Invalid mobile number")
            while 1:
                customer.city = input("Enter city of customer: ")
                if customer.myisalpha(customer.city) and len(customer.city) < 20:
                    break
                else:
                    print("Enter customer city again")
            while 1:
                customer.state = input("Enter state of customer: ")
                if customer.myisalpha(customer.state) and len(customer.state) < 20:
                    break
                else:
                    print("Enter customer state again")
            while 1:
                customer.pinCode = input("Enter pincode of customer: ")
                if customer.pinCode.isnumeric() and len(customer.pinCode) < 10:
                    break
                else:
                    print("Wrong format")
                    print("Enter customer pincode again")
            customer.addCust()

            print("Customer added successfully")
        elif (ch == "2"):
            while 1:
                choice = input(
                    "Enter 1 to search by id,2 for search by name,3 for search by city,4 for search by mobile "
                    "number")
                if (choice == "1"):
                    cus = Customer()
                    while 1:
                        cus.id = input("Enter customer id: ")
                        if cus.id.isnumeric():
                            break
                        else:
                            print("Id should be in numeric")
                    a = cus.searchCust()
                    if a == 1:
                        print(
                            f"""Customer id is: {cus.id}  Customer age is:  {cus.age}  Customer name is: {cus.name}
                                                        Customer number is: {cus.mobile}  Customer email is: {cus.email}
                                                        Customer city is: {cus.city}  Customer state is: {cus.state}
                                                        Customer pincode is: {cus.pinCode}""")
                        break
                    else:
                        print("Id not found")
                elif choice == "2":
                    cus = Customer()
                    while 1:
                        cus.name = input("Enter customer name: ")
                        if cus.myisalpha(cus.name):
                            if len(cus.name) < 40:
                                break
                        else:
                            print("Enter you name in proper format")
                    a = cus.multipleSearch()
                    if a == 1:
                        cus.showCust()
                    else:
                        print("Name not found")
                elif choice == "3":
                    cus = Customer()
                    while 1:
                        cus.city = input("Enter city of customer: ")
                        if cus.myisalpha(cus.city) and len(cus.city) < 20:
                            break
                        else:
                            print("Enter customer city again")
                    a = cus.multipleSearch()
                    if a == 1:
                        cus.showCust()
                    else:
                        print("City not found")
                elif choice == '4':
                    customer = Customer()
                    while 1:
                        customer.mobileno = input("Enter mobile number of customer: ")
                        a = customer.mobilechecker()
                        if a == 1:
                            break
                        else:
                            print('Invalid mobile number')
                    b = customer.searchCust()
                    if b == 1:
                        print(
                            f"""Customer id is: {customer.id}  Customer age is:  {customer.age}  Customer name is: {customer.name}
                            Customer number is: {customer.mobile}  Customer email is: {customer.email}
                            Customer city is: {customer.city}  Customer state is: {customer.state}
                            Customer pincode is: {customer.pinCode}""")
                    else:
                        print("Wrong input")
        elif (ch == '3'):
            print('Enter 1 for delete from id,2 for delete by mobile,3 for delete by email')
            choice = input('Enter your choice')
            if choice == '1':
                cus = Customer()
                while 1:
                    cus.id = input("Enter customer id: ")
                    if cus.id.isnumeric():
                        break
                    else:
                        print("Id should be in numeric")
                a = cus.deleteCust()
                if a == 1:
                    print(f"Customer with id: {cus.id},name: {cus.name} deleted successfully")
                else:
                    print("Id not found")
            elif choice == '2':
                cus = Customer()
                while 1:
                    cus.mobile = input("Enter mobile number of customer: ")
                    a = cus.mobilechecker()
                    if a == 1:
                        break
                    else:
                        print('Invalid mobile number')
                a = cus.deleteCust()
                if a == 1:
                    print(f"Customer with id: {cus.id},name: {cus.name} deleted successfully")
                else:
                    print("mobileno not found")
            elif choice == '3':
                cus = Customer()
                while 1:
                    while 1:
                        cus.email = input("Enter customer email: ")
                        if cus.emailchecker:
                            break
                        else:
                            print("Wrong format input as example@example.com")
                    a = cus.deleteCust()
                    if a == 1:
                        print(f"Customer with id: {cus.id},name: {cus.name} deleted successfully")
                    else:
                        print("email not found")
            else:
                print("Invalid input")
        elif (ch == '4'):
            print('Enter 1 for modify from id,2 for modify by mobile,3 for modify by email')
            choice = input('Enter your choice')
            if choice == '1':
                customer = Customer()
                while 1:
                    customer.id = input("Enter customer id: ")
                    if customer.id.isnumeric():
                        break
                    else:
                        print("Id should be in numeric")
                b = customer.searchCust()
                if b == 1:
                    while 1:
                        customer.age = input("Enter customer age: ")
                        a = customer.agechecker()
                        if a == 1:
                            break
                        else:
                            print("age should be in number")
                    while 1:
                        customer.name = input("Enter customer name: ")
                        if customer.myisalpha(customer.name):
                            if len(customer.name) < 40:
                                break
                        else:
                            print("Enter you name in proper formate")
                    while 1:
                        customer.email = input("Enter customer email: ")
                        if customer.emailchecker:
                            break
                        else:
                            print("Wrong format input as example@example.com")
                    while 1:
                        customer.mobileno = input("Enter mobile number of customer: ")
                        a = customer.mobilechecker()
                        if a == 1:
                            break
                        else:
                            print("Invalid mobile number")
                    while 1:
                        customer.city = input("Enter city of customer: ")
                        if customer.myisalpha(customer.city) and len(customer.city) < 20:
                            break
                        else:
                            print("Enter customer city again")
                    while 1:
                        customer.state = input("Enter state of customer: ")
                        if customer.myisalpha(customer.state) and len(customer.state) < 20:
                            break
                        else:
                            print("Enter customer state again")
                    while 1:
                        customer.pinCode = input("Enter pincode of customer: ")
                        if customer.pinCode.isnumeric() and len(customer.pinCode) < 10:
                            break
                        else:
                            print("Wrong format")
                            print("Enter customer pincode again")
                else:
                    print('Id not found')
                a = customer.modifyCust()
                if a == 1:
                    print(f"Customer with id: {customer.id},name: {customer.name} modified successfully")
                    print("Customer added sucessfully")
                else:
                    print("Id not found")
            elif choice == '2':
                cus = Customer()
                while 1:
                    cus.mobile = input("Enter mobile number of customer: ")
                    a = cus.mobilechecker()
                    if a == 1:
                        break
                    else:
                        print('Invalid mobile number')
                a = cus.searchCust()
                if a == 1:
                    cus.modifyCust()
                    print(f"Customer email {cus.mobile} modified successfully")
                else:
                    print("mobileno not found")

            elif choice == '3':
                cus = Customer()
                while 1:
                    while 1:
                        cus.email = input("Enter customer email: ")
                        if cus.emailchecker:
                            break
                        else:
                            print("Wrong format input as example@example.com")
                    a = cus.searchCust()
                    if a == 1:
                        cus.modifyCust()
                        print(f"Customer email {cus.email} updated successfully")
                    else:
                        print("email not found")
            else:
                print("Invalid input")
        elif ch == '5':
            for index in range(len(Customer.customerList)):
                print(
                    f"Customer id is: {Customer.customerList[index].id}  Customer age is:  {Customer.customerList[index].age}  \n"
                    f"                Customer name is: {Customer.customerList[index].name} Customer number is: {Customer.customerList[index].mobile}  \n"
                    f"            Customer email is: {Customer.customerList[index].email}  Customer city is: \n"
                    f"            {Customer.customerList[index].city}  Customer state is: {Customer.customerList[index].state}  \n"
                    f"            Customer pincode is: {Customer.customerList[index].pinCode} ")
        elif ch == '6':
            Customer.createFile()
            continue
        elif ch == "7":
            Customer.reportFile()
            continue
        elif ch == '8':
            Customer.picload()
        else:
            print("Invalid input")

